# T-PR-17 — Prompt 序列消融：decomp + 缺口

**发起**: 2026-11-22 D 新 idea（原话）："在不同prompt（也就是不同完成度的checkpoint）基础上渐进消融查看prompt序列是否影响最终结果"
**落点**: modules/B-pipeline-ablation/（消融模块）+ experiments/stage-ablation/（执行脚本）
**前置**: 本地覆盖检查已完成——t26-prompt-style-research.md 覆盖 prompt **风格**（情绪/PUA，19 篇），不覆盖 prompt **序列/顺序** → 真缺口，非重复。

## 实验语义（对齐）

SM 生产路径有固定 prompt 序列：P1_L1_SKELETON → P1H_INDEX（逐层 decompose）→ P3_VERIFY → P4_SYNTHESIZE。
实验 = 从**同一中间状态**（checkpoint）出发，用**不同后续 prompt 序列**继续，比较最终 depth。

**核心问题**：路径依赖——同一 checkpoint 下，不同序列 → 同一终态（序列只是搬运工，checkpoint 决定一切）还是不同终态（顺序效应真实存在，序列本身携带信息）？

**为什么值得做**（与主线 goal 的关系）：
- 若序列无影响 → 可以简化 pipeline（砍 verify/换顺序省 token），且 checkpoint 成为完整状态（可任意续跑/换策略）
- 若序列有影响 → 序列是隐式控制变量，当前固定序列可能是（偶然）最优，需要显式优化；且 resume 语义要包含"从哪段序列继续"

## 分解树

```
T-PR-17 prompt 序列消融
├── F1. 本地覆盖检查 ✅（t26=风格不序列；resume 机制已有 gpu-resume 先例）
├── F2. 文献滚雪球（arena T-PR-17 派发）✅ 交付 81cc016dc（sha256 核验过，7 ID 全过 abs 页，OpenReview API 2 次可用）
│   ├── C1. 多阶段 LLM pipeline 的 prompt/instruction 顺序效应先例？
│   │   → 部分有先例 conf 0.62：阶段"有/无/粒度/结构搜索"都有研究（PIVOT 2605.11225 逐阶段消融、STIG 2601.09728 粒度、AFlow 2410.10762 结构搜索）；
│   │     但"内容固定、只置换阶段顺序"的对照未找到（conf 0.55）→ 我们的增量空间
│   ├── C2. 从中间状态用不同后续序列续跑、比终态的先例？（path dependence）
│   │   → 强同构 conf 0.80：Handoff Tax 2608.24358（固定 repository 状态 W_K，变交接接口，比终态+成本；
│   │     结论：full-trajectory 升级只回收 <50% 质量差且付成本溢价；最优接口随方向反转 → checkpoint 不能混池统计）
│   ├── C3. 机制层：长上下文中指令位置效应（lost-in-middle 家族）
│   │   → 三条传导路径：位置（2307.03172 U 型 / 2406.16008 calibration 抵消 +15pp）、
│   │     长度（2510.05381 纯长度 −13.9%~−85%）、顺序（KDD 2025 Workshop Order Effect −13.95%）
│   │   → 关键警告：当前 4 臂设计里内容/长度/位置未分离，"顺序置换臂"很可能只是复现已发表的位置/长度效应
│   └── D 收敛假说（2026-11-22 追加）："prompt 初始只是先验，递归分解/信息足够全面应收敛到同一上界"
│       → 数学根基 = 贝叶斯先验不敏感性（后验敏感度随证据→∞ 衰减）；条件"信息→∞"在我们系统不满足
│         （源限制 + 注意力衰减 = 信息收集有界）→ 先验影响永不消失
│       → 无现成定理直接覆盖：Banach 压缩（要求确定性算子，我们 temp=0.7 随机）；
│         遍历马尔可夫链（要求有限状态，我们连续无限）
│       → 实证反证（自家数据）：K7 同序列同预算 run 间 depth 方差 ~0.1（391 节点 0.5184 vs 392 节点 0.4300）
│         → 若收敛假说成立，同算子迭代后方差应→0，它没有
│       → 本实验 = 该假说的直接检验（见 F3 null control）
├── F3. 实验设计（F2 结果已定对照组；arena 5 条硬建议已并入）
│   ├── 变量1: checkpoint 深度（L1/L2/L3 完成态，同一 seed 同一题）
│   │   来源: K7 budget-719-r1 归档 sm-gpu-r1/r2/r3（SM 每轮落盘，r1=L1完成 r2=L2 r3=L3）
│   ├── 变量2: 后续序列变体（见下"序列维度重定义"）
│   ├── 固定: 题（gpu）、seed、max_depth=5、prompt 内容（只动顺序/取舍）
│   ├── ⚠ 序列维度重定义（2026-11-22 读 s5_state_machine.run() 后修正）:
│   │   SM 主循环 = 每轮 decompose→verify→rework→contradiction 交替（非"4 独立大阶段"）。
│   │   字面"阶段顺序置换"语义不通：verify 依赖本轮 decompose 产出，提前则无新节点可验。
│   │   可操作的序列维度 = ①verify 有/无 ②verify 时机（每轮/最后统一）③rework 有/无
│   │   ④state 块顺序（null）。arena C3 警告"顺序置换臂复现位置/长度效应"的具体化。
│   ├── 4 臂定义（一期 3 臂，verify-late 二期）:
│   │   ├── canonical: decompose→verify→rework→contradiction（现状，基线）
│   │   ├── verify-off: decompose→rework→contradiction（patch _verify_batch 直接标 verified，
│   │   │   不核验直接接受 → rework 不触发，语义干净）
│   │   ├── null-control: canonical 序列 + 每轮喂 LLM 的 state 块（confirmed/已有节点）随机重排
│   │   │   （纯扰动，测位置效应 X；序列效应必须 > X 才算真 = D 收敛假说直接检验）
│   │   └── [二期] verify-late: 先全 decompose 后统一 verify（需改主循环结构，monkey-patch 难）
│   ├── 实现 = monkey-patch（固化约束：不改 s5_state_machine.py，K7 进程已加载旧代码）
│   │   verify-off = patch _verify_batch; null-control = patch state 块排序
│   │   ✅ null-control patch 点已核验（2026-11-22 读源码）: confirmed_block 在
│   │   _decompose_layer 内联构造（self.confirmed[-40:]，无独立方法可 patch）→
│   │   方案 = ShuffledList 包装 self.confirmed（切片返回 shuffle 副本, append 正常）
│   │   → _decompose_layer 与 judge_necessary_batch 都看到乱序 state 块，纯位置扰动
│   └── 控制臂（arena C3 硬建议，防位置/长度效应冒充序列效应）:
│       ├── 长度匹配: 各臂喂 synthesize 的 state token 数 ±10% 内（2510.05381）
│       ├── 位置旋转: 同一 state 块 头/中/尾 三位置，位置当随机因子（2307.03172/2406.16008）
│       ├── null control（必做）: 不换阶段、只随机重排 state 块 → 测纯扰动 X；序列效应必须 > X 才算真
│       │   （= D 收敛假说的直接检验: 效应≈X → 序列只是搬运工, 假说成立, pipeline 可简化）
│       ├── 每臂 n≥5 + CI（已知合成方差 ~0.1, n=3 会出假阳性）
│       └── checkpoint 分开统计（Handoff Tax: 效应随方向反转, 不混池）
├── F4. 执行（等 K7 完成释放 vLLM；每 cell ≥3 reps）
└── F5. 分析（depth 差异 + Welch/MWU + 效应量；与 K7 的节点数轴正交性核对）
```

## F2b 滚雪球新增设计约束（11-24 文献滚雪球 T-PR-17-result.md，commit 81cc016dc）

今日滚雪球确认新颖性弱（"未找到完全同构先例" conf ≤0.55；强近邻 Handoff Debt / HSC-Bench / PIVOT），并给出 8 条方法学建议。其中 4 条是 decomp 尚未覆盖的真缺口，现并入设计（执行前必须落实）：

1. **先定义估计量（别把 4 臂当同一单因子）**：
   - *operational total effect* = 删 verify / 换序列后质量 + token + 工具调用一起变 → 回答"能否简化 pipeline 省预算"（本 goal 真正要的）。
   - *sequence-mechanism effect* = 阶段语义 / 次序本身的作用 → 需额外控制 token 长度 / 指令位置 / evidence / 预算。
   - 两种分开报告，不混成一个笼统"序列效应"。
2. **verify-off 的证据集混杂**：verify 会联网 / 过滤 / 改写节点，删它不只是删文字——会改变 evidence 集与树状态（未验证节点被直接接受）。当前 monkey-patch `_verify_batch` 标 verified 属"保留复合干预"，必须在分析里报 tool calls / evidence delta，不能把效应只归因"少了 verify 语义"；若要识别纯序列作用，需冻结同一 evidence snapshot replay 工具返回。
3. **多指标判分（depth 单独会奖励浅树 / 节点膨胀）**：并列报 depth + 节点覆盖 / precision + parent-link 正确率 + verified 比例 + 重复 / 缺失 + 失败率；盲化评分 + 估 judge 噪声。depth 只是其一，不能单指标下结论。
4. **KV-cache 声明边界**：本实验 treatment = "同一 text / SM checkpoint 重建续跑"，不是恢复完全相同的隐状态 / KV（Stage-Replay 2607.28495 警示：同 token prefix 的 fresh prefill vs retained cache 后缀可能不同）。claim 不得说"恢复了相同隐状态"。

**对外 claim 收窄**（snowball §claim 建议）：写成"stateful pipeline suffix-ablation 设计"，不写"首次证明 LLM 顺序效应" / "此前无 checkpoint continuation 实验"。

**统计补充**：若要声称"序列无影响"，需预设最小重要效应 + 等效性检验，不能用"不显著"代替"相同"（原 n≥5 + CI 保留，加等效性检验）。

## 缺口清单

| 子项 | 缺什么 | 补法 |
|---|---|---|
| F2 文献 | ✅ 已交付 81cc016dc（C1 conf 0.62 / C2 conf 0.80 / C3 机制映射） | 方法学缺口已记录：OpenReview 仅 2 次关键词检索非逐 venue 扫描；ACL Anthology 未查；PIVOT/STIG 数字为摘录级 |
| F3 序列变体 | ✅ 变体区分度已由 C1 定：verify 删除=内容效应（位置解释不了，conf 0.65 真实）；顺序置换=位置效应重灾区（conf 0.60 可冒充）；minimal=长度效应中等（conf 0.55） | null control 分离 |
| F3 checkpoint 恢复 | resume 是否完整保留状态（parent_ids 持久化 bug 已知，T5 未修） | 核验 checkpoint json 字段完整性，[待核验] |
| F4 资源 | vLLM 被 q7 719 队列占用（r2 进行中 ETA ~22:20，r3 ~24:15 完）；watcher 已挂自动 post-run | vLLM 释放后串行（单变量原则：同负载）；设计已含 F2b 4 条新约束，释放即按强化设计跑 |
| F5 判分 | judge 噪声 ~0.1 比预期效应可能更大 | **n≥5**（arena 硬建议，原 n≥3 不够）+ bootstrap CI；若效应 <judge 噪声 → 结论=不可检测而非无影响 |

## 任务表（派发只执行表内条目）

| # | 任务 | 状态 | 备注 |
|---|---|---|---|
| T1 | 定位 3 checkpoint（719-r1 归档 sm-gpu-r1/r2/r3）+ preflight（JSON schema + parent-link 完整性，重点核验 T5 parent_ids 持久化 bug） | ✅ 11-24 21:07 完成 (3e3859d31, Lead 核验过) | r1=33/r2=132/r3=381 节点, dangling=0, T5 全命中（r1 5 个=gap_check 补充, r2/r3 亦命中）, 3/3 pass |
| T2 | 写 tpr17 runner（canonical/verify-off/null-control 3 臂，monkey-patch，不改 s5_state_machine.py）+ 每 call 记录 token/tool calls/evidence delta（F2b 1/2/3） | ✅ 同上 | tpr17_runner.py 448 行, s5_state_machine.py 0 改动 |
| T3 | 冒烟测试（dry-run：patch 加载 + checkpoint 加载 + 首个 prompt 可构造，不发 LLM 调用） | ✅ 同上 | 9/9 全过（3 臂 × 3 ckpt）, smoke_matrix.json 独立复算确认 |
| T4 | 正式配对 run（分级：先 pilot 再 scale，见下） | 🔒 vLLM 阻塞 | 队列 r2 ~22:40 / r3 ~00:55（22:11 双轨核验: 线性外推 22:46 + 周期模式 22:35-22:45; LLM call 节奏是"峰→谷→峰→尾"周期性非劣化, r2 第二峰 22:00-22:15=360 calls 与 r1 第二峰 378 几乎重合, r3 预期同 ~114-120min） |
| T5 | 分析（多指标 + 等效性检验 + bootstrap CI） | 🔒 依赖 T4 | F2b 3 |

**T4 分级执行计划（11-24 21:10 Lead 核算，pace=6.31 nodes/min 来自 719-r1 实测 114min/719 节点；checkpoint 实际节点数来自 preflight 3e3859d31：r1(L1)=33 / r2(L2)=132 / r3(L3)=381）**：

| 档 | 规格 | 时长估算 | 决策规则 |
|---|---|---|---|
| pilot | 3 臂 × L3 ckpt(381) × n=3，budget=719（new≈338 节点/run ≈0.89h） | ~8h | vLLM 释放后第一个跑（~00:55 起，~09:00 完；22:11 双轨 ETA） |
| scale | 3 臂 × 3 ckpt(33/132/381) × n=5，budget=719 | ~64h（过夜+次日+次晨） | pilot 效应 > judge 噪声(~0.1) 且方向稳定 → 起 scale |
| 停 | — | — | pilot 效应 < 噪声 → 结论="不可检测"（F5 既定语义），不烧 64h |

**budget=719 而非 300（勘误 21:10）**：初版计划写 budget=300 + L3(122)，两处皆错——L3 实际 381 节点（122 是 idea2 budget-150 批的 sm-gpu-r2，张冠李戴），300 < 381 则 cap 小于已有节点数、续跑无意义。改 budget=719 = 源 run（budget-719-r1）原生预算，同 regime 混淆最小，且 Q7 曲线显示 719 档 cov 仍在涨（0.3269），序列效应在深树上更有检出空间。

理由（时长为 21:12 代码复算值，非心算）：全规格 3arm×3ckpt×n5@719 = 45 runs ≈ 64h（初版 63h 基于错误的 122 节点数，数值巧合接近但推导错）；scale 64h 太长，若 pilot 通过可考虑降 n=3（27 runs ≈ 26h）或只跑 L2+L3 两档（30 runs ≈ 42h）——pilot 结果出来再定；n=3 pilot 低于 arena 硬建议 n≥5，但 pilot 的目的只是"可检测性门控"，scale 档仍守 n≥5；L3 先行因 Handoff Tax 效应随方向反转 → L3 是最深 ckpt、剩余序列最短、效应最集中处，先在这里看有没有信号最省钱。

**waiter 链路核验（21:37 Lead 端到端过完，commit 3b4691138，明早勿重跑）**：DONE 检测✓（queue.sh L66 同文件同串）/ 健康端点✓（/health 与 /v1/models 均 200）/ 9-cell 命令参数✓（与 runner argparse 对齐，seed 默认 42）/ 落盘文件名✓（`{arm}_r3_r{rep}.json` 无 tpr17- 前缀，与 runner L435 一致）/ sanity floor 381✓（preflight r3=381）/ 报告 metric key✓（n_nodes/depth/verified_ratio/tokens_total/n_llm_calls/tool_calls/evidence_delta_chars/parent_link_accuracy 均在 compute_metrics 顶层返回）/ fail-fast✓（rc≠0 或 n_nodes<381 → break 2 中止整批）/ python 解释器✓（裸 python3 与 /usr/bin/python3 同为 3.9.6）/ 模块 import✓（py_compile + exec_module OK）/ rep 独立性✓（subagent 已修 run_arm 漏传 rep → null-control 臂跨 rep shuffle 流独立，n=3 CI 不虚窄）。残留风险：waiter 跑工作树非 commit，若 subagent 24:15 前改了 runner 引入语法错 → 首个 cell rc≠0 fail-fast，损失 ~10min，报告可查。

## 正交性自检

- F2（文献）vs F4（实验）：一个查先例一个跑数据，不重叠 ✓
- 与 K7（预算轴）：K7 动 max_nodes，本实验动序列，不同变量 ✓
- 与 K6（merge 消融）：K6 动 synth 内部 merge on/off，本实验动跨阶段序列，不同层级 ✓

## 完备性自检

D 的 idea 三要素 = ①不同完成度 checkpoint（F3 变量1）②渐进消融（F3 变量2 序列变体）③prompt 序列是否影响最终结果（F5 分析）。全覆盖。
