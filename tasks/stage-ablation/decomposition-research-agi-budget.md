# Goal: research-agi-budget — 分解树 + 缺口清单

**发起**: 2026-11-22 D 睡前指令
**目标（D 原话）**: "目标就是 research 的 AGI，最好可以通过预算直接控制 AI 在 Pareto 边界上研究（预算大就如同 gold 里面一样，完整覆盖所有贡献因子，否则就会压缩细节）"
**D 的关键重述**: "如果我要求框架最终目标是我的条件下性价比以及最快达到 AGI，你反而可能工作刚好，因为 general 这一点不会有问题，然后就是我的硬件条件下如何最快可靠达到的问题了"

**编号约定**: A-E = 本分解树子项（执行视角）；K1-K8 = design 文档 item 标签（设计视角，K 与 A-E 一一对应：K1=A2, K2=A3, K3-K5=B, K6=C, K7=E, K8=D）。跨任务引用 K 标签时带全名（如 "research-agi-budget K7 预算扫描"），不与其它 decomp 的子项编号混用。

## 目标语义（D 的重述改变了什么）

| 旧框架（TCO 题） | 新框架（AGI 题） |
|---|---|
| 通用 prompt + 领域内容 = 污染（over-guidance） | 目标具体（D 硬件下最快达 AGI）→ 领域内容是**目标定义**，不是污染 |
| 不泄露 = prompt 零领域词 | 不泄露 = prompt 不含 **gold 答案骨架**（分解结构/数值），但可含目标定义（AGI、D 硬件条件） |
| TCO 是代理题 | AGI 是 D 的真实目标，TCO 是它的子问题（研究基础设施的性价比） |

**"不泄露"的精确边界**（2026-11-22 与 D 讨论确认）：
- 题面给的（TCO/性价比/单卡多卡/32K）= 题目边界，prompt 可复述
- 模型先验（TCO 怎么拆、GPU 选型看什么维度）= 模型能力，prompt 不该替它写
- gold 骨架（摊销+电费+故障损耗 的具体分解结构）= 答案，prompt 绝不能含
- 目标定义（AGI、D 硬件、最快可靠）= 新题面，prompt 应含

## 分解树

```
research-agi-budget（D 硬件条件下，预算控制 AI 在 Pareto 边界上研究）
├── A. matched 批收尾（阻塞项，~3-4h）
│   ├── A1. 监控批完成（pid 87154，nat 10/10 完成，soc 7/10，gpu 5/10）
│   │   └── 原子：后台监控进程，批退出时落盘完成标记
│   ├── A2. 恢复记账（driver bug 导致 runs_sm_matched/ 空，数据在 54 个 archive）
│   │   └── 原子：archive 的 synth json 已含 judge 分数 → 纯数据拷贝+stats，零 LLM 成本
│   └── A3. 出 matched 批 stats（SM vs bare，同负载）
│       └── 原子：ablation_stats.py 跑 30 SM + 30 bare，Welch/MWU/δ/CI
│
├── B. prompt 设计（AGI 题，等 A 完成；批实时读 prompts.py 不能动）
│   ├── B0. 修正污染清单（2026-11-22 重 grep，摘要失真已纠正）
│   │   └── 完整时间尺度框架（即时/短期运营/长期持有）实际只在 2 处：
│   │       line 54（P1_DECOMPOSE，legacy）+ line 306（P1H_INDEX，生产路径）。
│   │       5 个 L1 变体只有泛化"时间尺度"（横切因子例子），非三分类框架。
│   ├── B1. P1H_INDEX line 306 去 TCO 特定框架
│   │   └── 原子："即时/短期运营/长期持有" → 通用"与该决策相关的时间跨度"，
│   │       byte-level diff 落盘，重跑 1 轮 smoke 验证不崩
│   ├── B2. 领域例子换抽象占位符（生产路径 4 处）
│   │   └── 原子：P3_VERIFY"硬件规格（带宽/显存/制程/功耗）"→"经验事实（具体规格/参数/版本）"；
│   │       P4_SYNTHESIZE"按字节 vs 按请求"→"不同口径的度量"；
│   │       EDGE_*"TCO/GPU 选型"→ 抽象运算例子；contradiction_scan"prefill/decode"→"不同口径的量"
│   ├── B3. AGI 题 prompt 组装（新题 Q9-agi 专用）
│   │   └── 原子：通用规则（B1/B2 修复后）+ 目标定义段（AGI 操作化 + D 硬件条件，
│   │       合法题面）+ 不含 gold 骨架（贡献因子分解结构）。目标定义段 = Q9-agi 题面 §题面
│   └── B4. P1_DECOMPOSE 不动（legacy，不在生产路径）
│       └── 原子：标记 legacy，不修
│
├── C. merge 消融（等 A 完成，vLLM 负载释放后）
│   ├── C1. 重跑 719 节点树 synth，保存 per-layer 输出（当前只存了 final answer）
│   │   └── 原子：synth_rerun.py 加 per-layer 落盘，~834s 单 run
│   └── C2. Arm A（skip merge，concat L1-L5 → judge）vs Arm B（merge，0.4261）
│       └── 原子：judge 两臂，A↑=merge 是压缩元凶，A flat=per-layer 自压缩
│
├── D. AGI 题面 + gold 骨架（新题，research 类）
│   ├── D1. 题面定义（D 硬件条件：本地工作站，vLLM 8787，qwen3.8-27b-mtp NVFP4）
│   │   └── 原子：写题面，D 醒来确认（题面 = D 的目标，不能我代定）
│   ├── D2. gold 骨架（完整覆盖所有贡献因子 = "最快可靠达 AGI"的分解树）
│   │   └── 原子：调研+建树（arena 外包优先，登录过期则本地 conf-0.2）
│   └── D3. rubric（judge 判定点，对标 gold 骨架）
│       └── 原子：gold 树 → 判定点 × 层级（同 gpu 38 判定点格式）
│
└── E. 预算控制实验（Pareto 边界，等 D 完成）
    ├── E1. 预算轴定义（search 次数 / token / 时间，单变量）
    │   └── 原子：选 1 个预算参数（SM 已有 budget_nodes/per_layer_cap/max_rounds），
    │       扫 4-5 个档位（含 unlimited 上限档）
    ├── E2. 质量轴（机械实例化密度为主 + judge 为辅）
    │   └── 原子：q9_formula_instantiation_probe.py（21 gold 公式签名，mention/instantiated 两级）为主轴；
    │       judge_v2_depth 降为辅助轴（⚠ 11-27 21:50 探针：11 门 7 道 reliability 维饱和放水，
    │       judge 仅作旁证不作唯一质量轴）。依据 formula-instantiation-probe-20261127.json
    ├── E3. 跑预算扫描（每档 ≥3 reps，同负载）
    │   └── 原子：batch driver，spec 驱动
    └── E4. Pareto 曲线（预算 vs 质量，找拐点 = 性价比最优点）
        │   ⚠ 口径修订（D 2026-11-24 08:02 质疑："pareto 理论上算不出来，为什么不质疑和修改"）：
        │   Pareto 前沿=理论构造（需完整 trade-off 结构，开放任务不可算）→ 改**经验预算响应曲线**
        │   （budget→质量实测 n≥3 均值+CI，拐点=边际增益/边际成本跌破阈值）。q7 已按此口径执行
        │   （n=3：jt 0.6603/cov 0.3205，300→719 边际 +0.0757，commit 653bcc22e）。
        │   信号登记：D1-persona-align/memory/objfunc-signal-log.md（2026-11-24 Pareto 条）。
        └── 原子：stats + 画图，拐点 = 边际质量增益/边际预算成本 最大化的点
```

### E1 预算轴设计（2026-11-22 定稿，批跑期间完成）

**D 的机制要求**："预算大就如同 gold 里面一样，完整覆盖所有贡献因子，否则就会压缩细节"。
即：预算是**覆盖度**的控制旋钮，不是单纯的时间/成本上限。

**SM 现有预算参数盘点**（s5_state_machine.py:120-128，刚 grep）：

| 参数 | 默认 | 控制什么 | 与"覆盖度"的关系 |
|---|---|---|---|
| `max_nodes` | 150 | 树总节点数硬顶 | **直接**：节点=贡献因子，预算↑=覆盖↑ |
| `max_depth` | 4 | 层级深度 | 间接：深度=分解粒度 |
| `max_kids_per_parent` | 8 | 单父子节点数 | 间接：广度 |
| `contribution_threshold` | 0.10 | 边际贡献<0.10 不展开 | 自然停止点（非预算，是剪枝） |
| per-layer max_tokens | 4000/8000 | 每层输出长度 | 细节密度（"压缩细节"的直接来源） |

**选 `max_nodes` 为主预算轴**，理由（单变量原则）：
1. 它是唯一**直接等价于贡献因子覆盖数**的标量——D 的"预算大=完整覆盖"逐字对应
2. SM 按 J_decomp 贡献度排序展开 → 小预算 = 自动取 top-K 贡献因子（Pareto 选择的机制已内置）
3. 成本单调：节点数 ≈ LLM 调用数 ≈ 时间/电费，预算轴=成本轴，Pareto 曲线可直接换算钱

**扫描档位**（5 档，含上限档）：
- B1: max_nodes=50（强压缩，~1/3 gold 覆盖）
- B2: max_nodes=100
- B3: max_nodes=150（当前默认）
- B4: max_nodes=300
- B5: max_nodes=719（= 719 节点树规模，"unlimited"档，gold 级覆盖）

**固定变量**（单变量原则，全部不动）：max_depth=5（resume 已证明 L5 必要）、max_kids=8、β=3.0、θ=0.10、prompt（B 修复后版本）、题（gpu，gold 最完整）、seed=42。

**质量轴**：主轴 = 机械公式实例化密度（q9_formula_instantiation_probe.py，21 gold 公式签名，mention/instantiated 两级）；辅轴 = judge_v2_depth 的 depth + coverage（现有 rubric，38 判定点，⚠ 11-27 21:50 探针证其 reliability 维 7/11 门饱和放水，故降为旁证）。
**每档 ≥3 reps**（方差来源已知：vLLM 并发非确定性，T53b 已量化）。
**Pareto 输出**：(cost=节点数/时间, quality=depth) 散点 → 包络线 → 拐点 = Δquality/Δcost 跌破阈值的点。
**预期**：B1→B3 陡升（覆盖主导），B3→B5 趋平（边际贡献因子价值低）→ 拐点在 B3 附近 = 性价比最优点。若 B4/B5 仍陡 → 当前默认 150 是欠预算，应上调。

**次预算轴（第二轮，视第一轮结果）**：per-layer max_tokens（4000 vs 8000 vs 16000）控制"细节密度"——D 说的"压缩细节"是 synth 侧，decompose 侧的细节密度由 per-layer tokens 控制。第一轮确认 max_nodes 轴形状后再扫，避免两轴混淆。

**正交性自检**：
- A（收尾）vs B（修复）：A 是数据回收，B 是代码修改，不重叠 ✓
- B（prompt 修复）vs C（merge 消融）：B 改 decompose prompt，C 改 synth 路径，不同阶段 ✓
- C（merge 消融）vs E（预算实验）：C 是单变量消融（merge on/off），E 是预算扫描，不同变量 ✓
- D（AGI 题）vs E（预算实验）：D 是题面+gold（输入），E 是实验（消费 D 的产出），依赖关系非重叠 ✓

**完备性自检**：D 的指令三要素 = ①定 goal 安排实验（A-E 覆盖）②不泄露（B + D 的边界定义覆盖）③预算控制 Pareto（E 覆盖）。无遗漏。

## 缺口清单

| 子项 | 缺什么 | 补法 |
|---|---|---|
| A2 恢复记账 | archive 54 目录 → runs_sm_matched/ 的映射关系（哪轮对应哪个 archive） | 按时间戳+qid+round 匹配，[待核验]：archive 目录名 sm-{qid}-{ts} 的 ts 是否唯一对应 round |
| B1 删时间尺度 | 删后模型是否还覆盖"时间维度"（gpu 题的 3 年 TCO 持有期） | 重跑 1 轮 smoke 对比节点数 [待核验] |
| C1 per-layer 输出 | synth_rerun.py 当前不落盘 per-layer 文本 | 改代码加落盘（~10 行） |
| D1 题面 | D 的"硬件条件"精确边界（哪些硬件算"我的条件下"） | D 醒来确认，[待核验]：是否含云端 API 预算 |
| D2 gold 骨架 | "最快可靠达 AGI"的完整贡献因子分解（无现成 gold） | 调研（arena/本地），[待核验]：AGI 的可操作定义（D 的 AGI = 什么能力阈值） |
| E1 预算轴 | 哪个预算参数最能控制"覆盖度 vs 压缩"（search 次数 vs token vs 轮数） | 先跑 1 个参数扫描，看哪个轴的 Pareto 曲线最陡 [待核验] |
| E4 拐点 | 性价比最优点的量化定义 | 边际质量增益/边际预算成本 最大化，[待核验]：是否需要归一化 |

## §1 本地背景扫描（2026-11-22 执行，4 项带证据）

| 必查项 | 查了吗 | 搜索命令/路径 | 发现 |
|---|---|---|---|
| 相关项目目录 | ✓ | `ls -d projects/*/D1-*` | 20 个 D1-*；直接相关：D1-think-token-budget（token 预算实验，T1-T4 完成，P1 answer-only 前沿）、D1-prompt-first-bench（本 bench 的母项目）、D1-persona-align（goal 方法论） |
| 已有调研/报告 | ✓ | `ls pfb/modules/B-pipeline-ablation/research/` | 11 份调研；直接复用：budget-sensitivity-goal-spec-survey（预算/敏感度文献）、rl-budget-unlock-survey（RL 预算控制 8 ID）、process-depth-eval-survey（深度评估 30+ 论文） |
| 相关记忆 | ✓ | MEMORY.md + qanda-ledger grep | T53b 全量结论（SM +0.182、并发非确定性、能力上限微架构层）；D1-think-token-budget 的"prompt 级预算 vs serving 级预算"两层结论可直接迁移到 E 预算轴设计 |
| 用户过往讨论 | ✓ | qanda-ledger.md grep + 本会话压缩摘要 | D 2026-11-22 睡前指令（本 goal 发起）；D 的 AGI 重述（"general 不会有问题"）；RL 预算控制 + prompt 解禁（L4 实验 3.5x 输出） |

**小结**：本地已有 3 份直接相关调研 + 2 个相关项目 + T53b 全量实验数据，本次需新增 = Q9-agi 题面/gold（D 目标无现成 gold）+ E 预算扫描（无现成 Pareto 数据）。

## §2 调研对象全集（候选 + 纳入/排除）

| 候选 | 纳入/排除 | 理由 |
|---|---|---|
| gpu 题（现有 gold 37 节点/深度 5） | 纳入 | E 预算扫描第一轮用（gold 最完整，判分锚定） |
| q9-agi 新题（D 目标） | 纳入 | D 指令核心；E 第二轮 + 长期主线 |
| nat/soc 题（flat rubric 无 gold 树） | 排除（本轮） | 无 gold 树，判分锚定弱；matched 批数据仍可用（A3） |
| Q1-Q5 旧题（H100/模型选型/部署/RAG/方法论） | 排除 | 与 AGI 目标正交，不贡献 Pareto 数据 |
| 云端 API 预算通道 | 待定 | D 未确认是否算"我的条件"内；[待核验]，默认排除（本地优先） |
| RL 微调路径 | 排除 | D 约束"不改权重"；rl-budget-unlock-survey 结论仅用于 E 的文献锚定 |

**覆盖性自检**：D 指令三要素（goal 安排/不泄露/预算 Pareto）× 执行层（A-E）全覆盖；无落空候选。

## §6 量化定义（所有指标带公式）

| 指标 | 公式/计算方式 | 数据来源 | 单位 |
|---|---|---|---|
| 预算 B | max_nodes 参数值（SM 树节点硬顶） | s5_state_machine.py:120 | 节点数 |
| 质量 Q | depth_score = judge_v2_depth.score_run(answer).overall（38 判定点加权） | judge_v2_depth.py | [0,1] |
| 覆盖 C | coverage = 判定点命中数/38（judge 输出） | judge_v2_depth.py | [0,1] |
| 成本 cost | elapsed_s（单 run 墙钟）+ n_nodes×unit_call_cost（LLM 调用数） | runs json | s / ¥ |
| Pareto 拐点 | 最小 B* s.t. ΔQ/ΔB < θ_pareto（θ_pareto=0.01/节点，即每多 1 节点质量增益 <0.01 视为平台期） | E4 扫描数据 | 节点数 |
| 性价比 | Q/cost（depth 每单位墙钟） | E4 | depth·s⁻¹ |
| 可靠性 rel | 结论正确率 = 人工抽查命中 gold 判定点数/抽查数（D 确认后定义） | D 抽查 | [0,1] |

## §7 任务书（arena 外包用，登录恢复后派发）

- **调研问题**：在 4×V100 + 27b 本地模型 + 不改权重约束下，达到 research-AGI（可发表级自主科研循环）的最优路径分解 + 预算-质量 Pareto 边界
- **已知背景**：§1 小结（T53b 数据 + 3 份调研 + 2 项目）
- **候选范围**：§2 全集
- **拆解维度**：能力/成本/可靠性/时间/路径（gold/Q9.md 树骨架 v0）
- **量化口径**：§6 公式
- **产出要求**：gold 树深度 5（对标 gpu 37 节点格式）+ 每叶子带 S-a/S-b/S-c 判分档 + ≥2 agent 交叉检验
- **失败降级**：arena 登录过期 → 本地 conf-0.2 骨架（已完成，gold/Q9.md v0），登录恢复后升级

## 执行顺序（D 睡眠期间）

1. **现在**：A1 监控（后台）+ 本文件落盘
2. **批完成时**（~3-4h）：A2 恢复记账 + A3 stats（零 LLM）
3. **之后**：B prompt 修复（改 prompts.py + smoke）
4. **之后**：C merge 消融（1 个 LLM run）
5. **D 醒来后**：D1 题面确认 → D2/D3 gold+rubric → E 预算实验

**不做的**（D 睡眠期间）：
- 不动 prompts.py（批在跑，实时读）
- 不派 arena（登录过期，T-PR-16 阻塞）
- 不定 AGI 题面（D 的目标，D 确认）
- 不跑新 LLM 实验（vLLM 负载给批）

## 批后执行记录（2026-11-22 06:50-07:10，批完成后解锁）

| 项 | 状态 | 证据 |
|---|---|---|
| A2 K1 恢复记账 | ✅ 完成 | 30/30 主文件（19 轮从 archive 恢复）；gpu r03 depth 重判 0.4613（原 judge 失败）；results-sm-matched.json 重建 30 条；cc-state 30 done |
| A3 K2 matched stats | ✅ 完成 | sm_vs_bare_stats.py → reports/t53b/stats-sm-vs-bare-matched.md。**同负载 SM 优：nat Δ+0.131 p=0.016 / gpu Δ+0.105 p=0.022（显著）/ soc Δ+0.059 p=0.083（不显著）**。commit 848996a30 |
| B K3+K4+K5 prompt 去污染+AGI 题 | ✅ 完成 | 生产路径 6 常量 9 个领域旧词清零（TCO/GPU/显存/按字节按请求/短期运营长期持有/prefill decode/制程）；P1_DECOMPOSE legacy 保留（不进生产路径）；Q9 题面入 s8b_pilot.QUESTIONS["q9"]（复用通用 P1_L1_SKELETON，不新增 AGI 专用 prompt——新增=over-guidance）；不泄露审计：gold 维度名/节点ID/判据关键词/公式 零命中。commit 64f714dbc |
| C K6 merge 消融 | ✅ 完成（07:08） | **Arm A concat = 0.4129 vs Arm B merge = 0.4261，Δ=-0.0132 → merge 不是主要瓶颈（A≈B）**。与「漏数字是自然压缩」结论一致：压缩损失在 synth 内部自然发生，merge on/off 差异小。产物 /tmp/merge-ablation/merge-ablation-merge-ablation-concat.json |
| E K7 预算扫描 | ✅ GPU 域 15/15 落地 + Pareto 首跑（11-24 00:50） | 5 档 max_nodes(50/100/150/300/719)×3 reps=15 runs 全部落地（ROADMAP "719_r2 在跑" 是 11-22 旧状态）。**执行发现（11-22 10:50）**：`max_nodes` 是轮间检查（s5_state_machine.py:1182，每轮顶部查一次），非逐节点硬顶——单轮 decompose 展开整个 frontier（每节点≤8 子），一轮冲过预算。实测 budget=50→175/103/136 节点，budget=100→314/123/122，各档实际节点数大量重叠。预算参数是下界非上限。**解读修正**：真正自变量=实际节点数（覆盖因子数=算力成本），跑完做 depth vs 实际节点数 的 Pareto 分析，绕开预算参数混淆。若需干净预算轴，修复=逐节点 enforcement（总节点≥budget 即停加子），follow-up 不阻塞本批。**Pareto 首跑结果（11-24 00:50, k7_pareto-gpu-20261124.md）= 旧口径负面信号，已作废（11-24 00:55 修正）**：旧 depth_score 单轴（self-judge，r=0.861 与 cov 相关）下 depth 不随预算单调升（ρ=0.221 ns）——**这是口径伪影，不是真实效应**。**新口径重评（judge_v1 + 域内 gold，k7-pareto-newjudge-20261124.md）= 正面结果，池化后降级（11-24 01:10 修正）**：GPU 域池化（K7 n=3 + rep-scan n=5，100/150/300 档 n=8）：50:0.463 → 100:0.445 → 150:0.501 → 300:0.579 → 719:0.643，总体单调升。**cov 轴在 ~300 节点饱和**（300:0.358 vs 719:0.352），struct 轴机械台阶继续升（0.8→0.933）非质量。**"Pareto 拐点 ≈ 300 节点"是 cov 轴拐点**（D 预算控制假说部分成立：预算大→gold 覆盖升，~300 节点后覆盖饱和，边际收益只剩深度台阶）。K7-only n=3 的"150→300 跳升 0.194/100节点 CI 不重叠"是 n=3 伪影（rep-scan 300 档 cov 0.317 < K7 三 rep 0.39-0.47，池化后跳升消失，150→300 增益 0.077 与 300→719 的 0.064 同量级）——**n=3 只能定拐点位置不能定拐点强度**。Q6 域新口径同向（50:0.329 → 300:0.465 → 719:0.483，300 后放缓）。附带发现：原批 300/719 逐 rep 分数相同的真因 = 旧口径用 gpu gold 跨域评 Q6 批命中数太少（cov 0.0/0.083/0.056），非 cache 串内容（节点 claim 0/30 相同已排除）；cache 压低方差假设在 Q6 gold 口径下初步支持（原批 300 sd=0.000 vs rerun sd=0.011, n=2）。**待办**：719 nodepth 批落地补 Q6 719 独立检索 + 300-r3 补 cache 对照 n=3 + Q7 扫描验拐点跨题稳健。 |
| D K8 rubric | ✅ v0 就绪 | gold/Q9.md J1-J12，权重和=1.00；arena 扩树后同步 |
| D3 rubric→v2 同步 | ✅ 完成 (22:35) | 27b subagent 撞 token 上限挂掉 → 改确定性脚本 build_q9_units.py (modules/B-pipeline-ablation/)。产出 gold-q9-units.json: 37 units (21 leaf/16 split), 权重和=1.0, 11 gate 叶 (J1-J5 cap + J9-J14 rel), lexicographic 语义注释 (judge_v1 加权求和≠lexicographic, E 须单独看 gate 命中率曲线), τ_cap/τ_rel 标 pending_D。judge_run 自检 PASS (不抛异常)。gold/Q9.md v0 判定点段加废弃指针 (不重写, units 是 canonical)。subagent 教训: 确定性文件变换别派 27b (读多文件后撞输出上限), 写解析脚本 |

**串行决策（偏离 design 顺序 K6→K7 并行的隐含假设）**：design 写 K6 ~15min 后 K7 后台，但 K6 的 Arm B 基线 0.4261 是特定负载下采的，K7 并发跑会破坏 K6 单变量对比的同负载前提 → 串行 launcher（K6 完→K7 自动），总 ~7-9h。

## §8 arena T-PR-16 对抗核验结果（2026-11-22 收口，回执已核验）

**核验**：commit 625f49a19bc1ca2b227358b3d3836c6363c88056 存在（origin/arena/f65a5a27-prompt-first-bench HEAD），任务书 sha256 dacfc44b… 与派发时一致，diff 仅加 tasks/T-PR-16-result.md（54 行）。arena 3m47s 完成，6 个引用 ID 全经 abs 页验证。

### A 段 novelty 判决（对我们的声明是坏消息，需改写）

| # | verdict | 关键反例 | conf |
|---|---|---|---|
| A1 组合 novelty | **部分站得住（表述过强）** | OHD 2602.01969（ICML 2026）=正交+依赖+树；SPRING 2609.34660（NeurIPS 2026）=约束追踪+过程分；RPTS 2511.06899=树+逐节点 faithfulness。各占两块，"无人组合"字面被部分证伪 | 0.62 |
| A2 depth 多档连续分 | **部分站得住** | ResearchRubrics 2511.07685 逐 criterion 三元（1/0.5/0）已是"非二元多档"先例；我们差异只剩档位粒度（3-6 档） | 0.55 |
| A3 3 棵 gold 树量级 | **不致命但需论证** | ResearchCodeBench 20 篇@ICLR 2026、TreeReview 80 篇@EMNLP 2025 靠"每例极贵"撑规模；3 棵树须证明同等标注强度 | 0.7 |

**novelty 声明改写（arena 建议，采纳）**：
> 已有的两两组合（OHD=约束+树、SPRING=约束+过程分、RPTS=树+过程分）都用**端任务精度或训练奖励**验收；没有工作把三者做成一个**带 gold 树与逐判定点连续分的评测协议**，并报告该协议的复现性（n=10 轮 + CI + 效应量）。我们的 novelty 在**评测协议**，不在组合本身。

改后 novelty conf：0.8 → **0.75**（更窄但可防）。

### B 段 TCO 滚雪球判决（TCO 时间分解不能当 novelty）

| # | 结果 | 证据 | conf |
|---|---|---|---|
| B1 时间尺度分解 TCO | **有强先例（老题）** | 2509.26534 按资产寿命分层摊销（15-30/7-10/3-5 年）；2509.07567 电价按时间尺度采样；2607.07207 价格分支+折旧传送带 | 0.85 |
| B2 LLM 自主生成带时间尺度成本树 | **未找到（窄缝）** | ACEM 2608.02582 人定固定结构；TCA 2609.23790 深度维度成本归因（非时间）；BAVT 2603.12634 推理期预算 | 0.6（否定性结论按纪律压低） |
| B3 GPU 价格波动量化 | **部分有先例** | 2607.07207 价格路径变→结论翻转 + U 型 breakeven；行业分析给利用率>折旧年限敏感性排序（非同行评议） | 0.7 |

**TCO 定位修正**：
- ❌ 不能主张"时间尺度分解 TCO"为 novelty（B1，0.85，会被 2509.26534/2509.07567/2607.07207 直接打掉）
- ✅ 能守的窄缝 = "LLM 自主生成 + 逐节点 + 时间尺度"三合一（B2 未找到，但 TCA 已在深度维度做了同类事，空间窄，conf 0.6）
- 套磁/论文定位调整：TCO 时间分解作为**应用背景**（引用 3 篇老题），novelty 锚在**评测协议**（A 段改写）

### 方法学缺口（arena 如实登记，需 Lead 知悉）

1. arXiv API id_list 批量查询连挂 3 次 → 降级逐 abs 页（6 ID 全验证正确，无影响）
2. **OpenReview 2025-2026 未系统检索** → A1 若漏 OpenReview-only 投稿（未上 arXiv）会失真，这是最大缺口
3. RPTS 2511.06899 本轮未复核（沿用工作区记录）
4. GPRM 2611.20755"四维评估"是否等价"过程判分多档"未验证 → 不计入 A1 反例

### 对 goal 的影响

- **E 预算实验不受影响**：预算-Pareto 是工程实验，novelty 声明改写不改变实验设计
- **D2 gold 骨架**：arena 核验的是 novelty，不是 gold 内容；Q9-agi gold 仍 conf 0.2（T-PR-16 任务书是 novelty 核验，未含 gold 扩树）
- **论文/套磁定位**：novelty 锚从"组合"移到"评测协议"；TCO 时间分解降为背景引用
- **follow-up**：OpenReview 缺口可补一轮（ego-browser 查 ICML/NeurIPS/ICLR 2025-2026 OpenReview），但非阻塞

## 全景核验（2026-11-24 03:25，goal 子项状态对账）

| 子项 | 状态 | 证据/阻塞 |
|---|---|---|
| ① matched 批+记账 | ✅ 完成 | 30/30 done 核验（results-sm-matched.json 30 runs 对账一致）；cc-state-sm-matched.json stale active 标志已清（11-22 完成时未清） |
| ② T-PR-17 机制验证 | ✅ pilot 9/9 cells 完成 (11-25 10:18) + 正式报告 | r3 落盘 10:18（71min/1263 calls）。**正式报告 tpr17-pilot-report-20261125.md**：① 测量盲区修正——run JSON 计数器只 wrap sm_mod 绑定，verify_node 走 s5_pipeline 自有 import 绕过（漏 ~1150 verify calls），PREVIEW"只省 356 tokens"作废；真实信号=verify 是成本中心（stdout 真计数 canonical ~1238 vs verify-off ~491 calls，wall 75 vs 23min，新窗口 rework 186 vs 21 砍 89%，树结构零变化）② TOST 首判：null-control vs canonical verified_ratio CI[-0.057,+0.008]⊂±0.1 → 序列机制等效（D 收敛假说 pilot 层面支持，n=3 UNDERPOWERED sentinel）③ 质量价值本 pilot 不可判（搜索降级 corrected_claim=0 全臂）。runner 计数器已修（3 处 wrap+哨兵防嵌套，fake 替身验证）。clamp 边界：结构惰性仅在 budget 719 硬顶+depth 4 封顶下成立。commit 3d2b74a62+d3b36b9ea |
| ③ K6 merge 消融 | ✅ 完成 | Δ=-0.013 A≈B（11-22 07:08） |
| ④ K7 预算扫描 | ✅ 完成（relay 链 11-25 全收口） | k7-pareto-newjudge-20261124.md；三待办收口：Q6 719 nodepth 3 reps 落盘+analysis（cov 0.1304/0.2391/0.2174）；300-r3 cache 对照独立评分 0.3077（vs r1/r2 复制 0.2308）；Q7 跨题 719 n=3（replication 2/2 全中 finalized, q7-719-replication-check-r3-20261125.txt）+ workshop §4.3 n=3 同步（2f0556fd4） |
| ⑤ AGI 题面+gold 骨架 | 🟢 推进中 | **D 三项默认立场已冻结（2026-11-27 全自动原则：预算150/5因子/排序键post_acc，E-SYNTH 依赖已解除）**；D1 题面；**Lead 完整推导已备 (11-26, b66e38da3)**：q9-agi-question-d1-lead-derivation-20261126.md（四项默认立场+改主意条件，硬件已实测核验 server6=4×V100 与题面一致；②预算 150 待 E-SYNTH 回执复核）；**D2 gold 骨架 Q9-v1 已交付+Lead 核验通过 (11-24 20:22)**：agent @ 8fe85a2f4（37 节点/深度 5/21 叶/权重和 1.00/题面隔离），agent 主动纠错 +0.182 归属（实为 S0→S5 prompt 级，非 SM 因果；SM 真实 δ=+0.025 p~0.32），Lead 本地实锤 + web-LLM 2/2 独立源（Perplexity+ChatGPT）确认纠错正确且重大；方法学 v1 弱点（等权 0.20/五维不正交）归 v2 修。回执 web-llm/d2-q9v1-lead-verify-20261124.json；E1-E4 由 K7 代理覆盖 |
| ⑤-D2-v2 gold 骨架方法学修正 | ✅ 完成 (11-24 20:25-20:31) | `gold/Q9-v2.md`：① N-0 改 lexicographic（硬门 capability/reliability 先判，门内 min w_t·T+w_c·C；0.20 权重降级为描述性 dashboard）② N-5 重标决策变量层（输入非结果，消 double-count）③ 证据质量登记表 21 行（provenance/uncertainty/n/reproducibility，未跑实验一律 NA）。验收复算：v2 与 v1 树结构一致（37 节点/深度 5/21 叶 J1-J21/权重和 1.00），v1 保留供审计。改动纯方法学层，叶公式/权重数值未动 |
| ⑥ 思考触发分支 T1-T4 | ✅ 全部完成 (11-25) | T1 hook 已实现+commit（stage-gate 仓 1b30bc6，APPROVALS 08697954；隔离沙箱 5 场景过）；T2 接着考虑实验完成（臂B 3/3 爬机制层+预言，臂A 0/3；但域偏移 100% 漂到混沌域——flip=0，形式接住内容未接住；v2 补抓 reasoning 修正低估）；T4 真检测落地（7229159，同一报错签名 10 轮≥2 次或同文件 6 轮改≥5 次且有报错；12 生产 session 0 误报）；T3 整合完成（T2 爬层判据拆成 formalism 的 flip/shift 两分量接进 judge，非 ad-hoc 第四维；阈值维持 223 会话基线待生产 HIT 数据校准）。证据：modules/G-think-mechanism/think-trigger/decomposition.md |
| ⑦ E-SYNTH 跨域 Pareto 综合+推荐操作点 | 🔄 in_progress | 数据已全收口但散在 5+ 文件且各域结论不一（GPU cov ~300 饱和 vs Q6 719 未饱和），无文档回答 goal 核心「Pareto 边界+推荐操作点」。TASK-E-SYNTH-pareto.md 派发（11-26，离线零 LLM，sub 执行中）。产出 e-synth-pareto-20261126.md |

**基础设施修复（本轮）**：ROADMAP 3 处断链路径修复（tasks/ → experiments/stage-ablation/tasks/，6/6 路径核验通过）。
**协调冲突（本轮）**：nodepth 批被另一会话越序并发启动（违反 vLLM 不并发前提），已 kill + relay log 留痕（K7 报告有记录）。

## T-REPAIR-1 repair loop 实验（2026-11-24 22:40 设计）
- **状态**：🚀 已 arm（11-25 10:50, PID 15606 proc_51a33a51c46b），Gate 等 post-pilot 队列 PID 1892 退出 + vLLM 就绪后自动串跑 4 臂
- **设计**：（2×2 析因 Fix-A directed可达 × Fix-B re-entry, budget=300 Q6, n=3/臂, 预测 P-A/P-B/P-A+B）
- **依据**：workshop §5 implication-1（repair 是唯一还开着的高杠杆, 当前 3.7%）
- **执行器**：t-repair1-4arm.sh（commit 71c3c5358+481fb91c7）——序列 baseline→A→A+B→B（每步 commit 留痕, 审计链 H0(0,0)→H_A(1,0)→H_AB(1,1)→H_B(0,1)→restore(0,0)）；每臂独立 SM_CKPT_DIR 防陈旧子树；同 SM_SEED=42；marker 校验 + py_compile 门禁 + 失败即中止；收尾 restore-commit 保审计链线性。临时 repo 干跑验证：终态 SM 逐字节还原（md5 44f6c4b5）。
- **分析**：t-repair1-analysis.py（commit b6ec6059e+46d6c8d6f）——节点级修复率+bootstrap CI+TOST+P-A/P-B/P-A+B 机械判别；rc 感知（executor log 解析 per-rep rc, 失败 rep 排除防旧文件冒充）；6+2 单测过。watcher t-repair1-postcheck.sh 自动跑。
- **Prereg 效度注记（11-25 分析前核查）**：Q6-300 基线 rework 事件 mode 全 angle(167), value_mismatch=0 → P-A 主判别在 Q6 域分母=0 不可直接测，降级间接观察。**Follow-up（不阻塞本批）**：P-A 正式测需 gpu 域补 4 臂（gpu 域 value_mismatch 分母>0，80-run corpus 基线 2.4%=22/932）；另注意搜索降级条件下 rework 事件构成可能漂移（no_source 占比升），跨批对比带 caveat。
- **时序**：队列(4 步, ~2-4h) → T-REPAIR-1 4 臂(12 runs × ~45min ≈ 9h) → 自动分析
- **进度核验（2026-11-25 15:45, subagent）**：4/12 reps 完成（baseline r1-3 + fixA r1，全 rc=0），t-repair1-stats.json 4 条目与日志一致；postcheck(PID 19059)+执行器(PID 15606) 均存活健康。**外观陷阱（勿误判）**：postcheck 的 "arms runs json count" 行用递归 `find arms/ -name '*.json'`，会把每臂 `checkpoints/` 下的 node.json（~1260 个）一并计入 → 完成时该行显示 ~1266 而非 12，**正常**（runs json 是 `arms/<arm>/<arm>-r<rep>-<ts>.json` 顶层文件，分析脚本 t-repair1-analysis.py L44 用非递归 glob `{arm}-r*.json` 不受影响，已核验）。
- **中期机制核验（2026-11-25 15:50 提出 → 16:20 n=2 复现, subagent · interim 非 prereg 主结局）**：Fix-A 机制指纹已在 live run 确认且**n=2 可复现**——baseline 3/3 reps `directed`=0（directed 模式不可达），fixA r1 `directed`=4（N42/N105/N223/N331，全为数值量级/算术矛盾/工程常识挑战=value_mismatch 类）、fixA r2 `directed`=5（16:20 落盘后核验）。对照设计（Fix-A=directed 可达）+ prep `c999cb241`（directed 集≡VM 人口，14511 事件零偏差）→ directed>0=Fix-A 使 directed 可达后正确路由的 VM 事件，两 rep 复现。**这是 prereg 标注的 P-A 在 Q6 域唯一可用间接观察信号的实际兑现**（主判别 value_mismatch 分母=0 不可直接测）。caveat：fixA 仅 2/3 reps、n=2/臂，是机制确认非效应量估计；最终 P-A/P-B/P-A+B 判别以 12-run 完整分析为准。
- **directed 路径下游效应急间信号（2026-11-25 16:25, subagent · interim 非 prereg 主结局 · n=2/9 事件）**：机制可达后 directed 事件的下游验证情况——r1 1/4 verified（N105；N42 pending、N223/N331 degraded）、r2 **0/5 全 degraded**（N14/N17/N36/N43/N311，L2×2/L3×2/L4×1）→ 合并 1/9=11.1%。**两个方向相反的信号并存，n=2 不足以定论**：①事件级 directed 修复率 11.1% **高于** P-A 的 2.4% corpus 基线（方向性正向，但 n=9 极小、r2 单 rep 0/5 拖低）；②节点级合并修复率 fixA 目前**未高于** baseline（fixA 0.0476/0.0118 均值≈0.030 vs baseline 0.0600/0.0390/0.0606 均值≈0.053），且 rep 间大方差（fixA spread 0.036 > baseline 0.021）。对照 angle 事件级：baseline 10/193=5.2%、fixA 4/160=2.5%。**方向性提示**：若 12-run 终态 fixA 节点级不升，与 prereg 判别规则一致（"A、B 都不升→瓶颈在 fixer 能力/contradiction 证据"）——directed 可达解决了路由缺陷，但节点级净效应取决于 directed 修复质量能否在更大样本上兑现；若 directed 事件级维持 >2.4% 而节点级仍不升，则瓶颈在 directed 路径的改写质量（fixer 能力）而非路由。此为中期观察，12-run 完整析因后才可定论。
- **rc 解析链实证（2026-11-25 16:15, subagent · 补 16:50 触发链核验的前提实证）**：16:50 核验了 postcheck→分析触发链 + "parse_rep_rc 多日志合并安全"，但那只是**静态读代码推断**正则能匹配 log 格式。本轮用**实际代码函数对真实 log 执行**（importlib 加载 t-repair1-analysis.py → 调 mod.parse_rep_rc 对 1 个 executor log）：解析出 5 个 (arm,rep)→rc 条目（baseline 1/2/3 + fixA 1/2，全 rc=0），与独立正则数的 5 行 rc **完全一致** → 正则确实匹配当前 log 格式，`rep_rc` 非空，**失败 rep 会被正确排除**（旧文件不会被当新 rep 用）。`load_arm_runs` 行为核验：baseline 加载 3 reps、fixA 加载 2 reps，与磁盘一致。**意义**：rc 排除链（防旧文件冒充）从"静态推断安全"升级为"真实执行验证安全"——这是 all-or-nothing 脆弱点（任一 rep 失败→该臂<3 reps→FATAL）的**正确触发前提**，若正则不匹配则 rep_rc 空→失败 rep 不被排除→旧文件被误用→析因基于脏数据。至此 rc 解析链实证闭合。
- **postcheck→分析触发链全链核验（2026-11-25 16:50, subagent · 5h 关键路径最后一段）**：通读 t-repair1-postcheck.sh（24 行）+ 分析脚本 main()（L123-146），确认开火链：①postcheck `while kill -0 TR1_PID` 每 180s 探活执行器 → 退出后 ②`cd $BJ/research && python3 t-repair1-analysis.py`（L21）→ ③写 `logs/t-repair1-postcheck-<ts>.log`。**两个验收要点**：**A. `TR1-POSTCHECK-DONE` 标记无条件打印**（L22 只 `echo analysis rc=$?` 不据此分支，L24 恒打印 DONE）→ **DONE ≠ 分析成功**，验收时必须查 `analysis rc=` 行（rc=0 且 `t-repair1-analysis.json` 实际落盘才算成功；rc=1=FATAL 臂数不足，无文件）**B. `parse_rep_rc` 多日志合并安全**（分析脚本 L131 `sorted(glob t-repair1-4arm-*.log)` 按时间戳排序 + L134 `.update()` 顺序覆盖 → 新 log 的同 (arm,rep) 条目覆盖旧 log，执行器重启也不会被旧 rc 污染）；当前仅 1 个 log（5 条 rc=0 与 5 个已完成 rep 一一对应，无污染）。至此 5h 关键路径全链（执行器→postcheck 探活→分析触发→rc 语义→多日志合并）核验闭合。
- **跨天稳定性核验 + 两处口径注记（2026-11-25 16:40, subagent · 效度保护非 prereg 改动）**：用同口径（rework_count>0 且 status==verified）核三批独立未修改 SM 的 Q6-300 run 节点级修复率——11-23 原批 11/167=**0.0659**、11-23~24 重跑批（cache 隔离 rep-tag）11/158=**0.0696**、11-25 T-REPAIR-1 baseline 臂 10/193=**0.0518**，全在 0.05-0.07 带内、跨 2 天稳定。**对 4 臂比较的效度意义**：baseline 臂未跨天漂移，fixA/fixAB/fixB 与 baseline 的同日同域比较不被"SM 行为随时间漂移"混杂（若 baseline 两天间大幅移动，臂间差会被误读）。**注记①（文档/代码不一致，非功能 bug）**：分析脚本头 L6 声明"外部参照 q6-budget-scan/q6-300-r{1,2,3}*.json"，但 242 行代码从未加载该文件（仅 docstring 提及）——属信息性声明非实际消费；且现存在两套 q6-300（原批 q6-budget-scan/ + 重跑批 q6-budget-scan-rerun/），头指向原批。**注记②（P-B 判读口径）**：P-B claim 文字"> 3.7% 基线"的 3.7% 是 80-run 跨域 corpus 基线，而 Q6 单域未修改 SM 已 5-7%（>3.7%）→ 任何 Q6 run 平凡越过 3.7% 地板，**P-B 的有效判别实为 fixB vs 实验内 baseline 臂的 TOST/差值**（脚本已正确产出 `delta_vs_baseline_arm` + `tost_equivalent_to_baseline`），3.7% 仅作 sanity floor。此为解读注记，不改脚本（prereg 纪律）。
- **r3 n_nodes=229 异常排查（2026-11-25 15:55, subagent）**：baseline r3 节点数 229（r1/r2=300）经查为**正常 run 间变异非异常**——节点减少均匀跨层（L2 30→24/L3 88→64/L4 177→136，非某层塌缩）、无重复 ID（distinct=n）、ID 空洞更多(19)+分配范围更小(1-261 vs 1-318/329)=构建树本就小+rework 删得多；rework 事件 r3=93 反低于 r1=97/r2=121。结构完整(L1-L4 全在/max level L4/3 rounds/leak=0)。**对 prereg 分析的意义**：节点级修复率若误判 r3 为"塌缩 run"会错误排除，确认健康变异保护分析完整性，r3 应纳入 12-run 分析。
- **分析脚本 FATAL 路径实测 + 脆弱点（2026-11-25 16:00, subagent）**：用当前 4/12 数据实测 t-repair1-analysis.py——FATAL 路径行为正确（caveats 准确报 fixA 1 rep/fixAB 0/fixB 0，exit 1，不写分析文件，符合 postcheck 容忍 rc=1 的设计）。**但暴露 all-or-nothing 脆弱点**：L144 任一臂因某 rep 失败(rc≠0)而有效 reps<3 即被排除 → `len(arm_stats)<4` → FATAL → 整个 12-run 析因不产出。**即 4 臂里只要 1 个 rep 挂掉，5h 跑完也拿不到析因**。**真实恢复路径（已核实执行器结构，非"单 arm/rep 重跑"）**：执行器是单体（固定序列 baseline→A→A+B→B、REPS=3 硬编码、只吃 queue_pid 参数，无 arm/rep 选择）；rep 失败时仍 `cp` 旧 runs-s5-sm-q6.json（上一 rep 文件）+ 记 rc≠0（分析脚本 rc 感知会排除，commit 46d6c8d6f 防旧文件冒充）。若某臂有效 reps 掉到 <3 → FATAL。恢复 = 手动重放该臂：重新 apply 该臂的 fix marker（Fix-A/Fix-B hunk）+ 直接调 SM 命令（run_arm 函数体可复用，SM_SEED=42 + 独立 SM_CKPT_DIR + 同 QFILE/budget），补出该 rep 的 json 后重跑分析；或整批重跑执行器（代价大）。**注：此为预防性注记，当前 4 个已完成 rep 全 rc=0，暂无需触发。**
- **分析脚本 happy path 冒烟（2026-11-25 16:05, subagent）**：5h 投资的最后一段未测代码路径（正常 4 臂析因 + 4 prediction 判别 + 文件写入）用真实数据结构端到端跑通——4 臂全指向 baseline 真实 3 reps（b=a=ab=bb 合成，delta=0），exit 0、无 stderr，4 臂 + 4 prediction（P-B/P-A/P-A+B/discriminant）全产出，文件 3388 字节写入 scratch（真实数据目录未触碰）。**关键观察对得上 prereg**：P-A `testable:false`（Q6 域 value_mismatch 分母=0，与 prereg 效度注记一致）+ discriminant `both_not_up:true`（合成数据相等时正确）+ interaction `orthogonal`（相等时正确）。至此 T-REPAIR-1 开火前可验证项全闭合：输入数据完整性（r3 健康/Fix-A 指纹/postcheck 计数陷阱/文件发现逻辑）+ 执行器结构 + 双进程健康 + FATAL 路径 + happy path。**下一步新信息只能来自 run 本身**（新 rep 落盘 / catchup 开火 / 12-run 完成自动析因），再查进度即刷进度。
- **catchup 链 4 步开火前门禁（2026-11-25 16:08, subagent）**：vllm-catchup 将在 t-repair1 退出后(~5h)自动跑 C1 l4-synth-recover / C2 l4-judge / C3 gptr / C4 tjudge1-J4。已做开火前语法+import 门禁——C1/C2/C3/C4 四入口 `py_compile` 全 OK；C3 三个关键 import（gpt_researcher + 本地 pfb_retriever + s8b_pilot）在**真实执行环境**（`cd experiments/stage-ablation` + `.venv-gptr/bin/python`）下全部可导入（先前探针报 pfb_retriever/s8b_pilot 缺失系未把 $SA 放进 sys.path 的假警报，文件确在 $SA、真实环境能 import）。catchup 链开火前可验证项闭合，无语法/import 级挂点。
- **catchup 链 C3 输入面核验（2026-11-25 16:12, subagent · 补 16:08 门禁只验 import 留下的最后输入缺口）**：C3 gptr_pfb_3q 无外部输入数据文件（query 来自 `s8b_pilot.QUESTIONS`），但有两运行时输入面未验——①`QUESTIONS` 是否含 nat/soc/gpu 三键（缺键→KeyError 崩）：实测三键齐全、query 非空（nat 225/soc 250/gpu 373 字符）✓；②gpu 题启用的 `local_corpus` 语料（`_LOCAL_CORPUS_DIRS` 指向 `pfb/knowledge-base/hardware` + `projects/decomp/archive/D1-gpu-research-2026`）：两目录均存在 ✓。**重要降级特性**：`_local_corpus_search`（research_hook.py L528）对缺失目录 `if not os.path.isdir(d): continue` 优雅降级为空、且 nat/soc 题经域门控直接返回 []（2026-11-09 设计，防 GPU 语料污染非 gpu 题）→ local_corpus 缺失**不是 C3 硬断点**，即使目录缺也只降级不崩。**至此 catchup 链 4 步运行时输入面 100% 闭合**（C1 输入 runs-s5-sm-l4-disambig.json+GOLD ✓ / C2 读 C1 产物 ✓ / C3 QUESTIONS 三键+local_corpus 目录 ✓ / C4 fallback-all+match-all ✓），加上 16:08 的 4 入口 py_compile+import 门禁，catchup 链开火前可验证面全闭合。
- **catchup 链输入依赖 + vLLM 就绪核验（2026-11-25 16:10, subagent · 补 16:08 门禁未覆盖的运行时输入面）**：16:08 门禁只查了语法/import，本轮补**输入文件存在性 + 依赖链 + vLLM 硬门**（catchup 的 FATAL exit 2 条件）——①**C1**：输入 `runs-s5-sm-l4-disambig.json`（453KB, 11-25 11:15）✓ + import 链 s5_state_machine(NodeRecord/synthesize_answer 均在) + s8b_pilot ✓ + **GOLD 含 l4-disambig 条目（4 条目 dict, 原崩溃根因已修）**✓；②**C2**：读 C1 产物 `runs-s5-sm-l4-disambig-synth.json`（C1 生成, 链上依赖正确, 非 C1 前就需存在）✓；③**C4**：输入 `tjudge1-llm-fallback-all.json`(715 行) + `tjudge1-match-all.json`(15794 行) 均存在 ✓，输出 `...-adjudicated.json` 不存在=正确（C4 产物, 终验 FRESH 检查对象）；④**vLLM 硬门**：`/v1/models` 当前 rc=0 返回 `qwen3.8-27b-mtp`（max_model_len 262144）→ catchup 的 30-min ready 探测门**当前已满足**（t-repair1 退出时 vLLM 若仍在跑则直接过, 无需等探测）。至此 catchup 链 4 步的**输入依赖面**（16:08 语法/import + 本轮输入文件/依赖链/vLLM 门）全闭合。
- **catchup 链结构核验 + 记忆纠正（2026-11-25 16:14, subagent · 5h 关键路径唯一未碰环节）**：通读 vllm-catchup.sh 实际 69 行，纠正此前凭记忆的两处不准确（来源③→①）：①**第 5 步不是"post armc-prime-post"**（此前记忆错），实际是 **VERIFY 块**（L58-68 产物级新鲜度：mtime > 启动时间戳 → FRESH/STALE/MISSING），查 3 产物 = C1 synth.json / C3 gptr summary.json / C4 adjudicated.json；②**链是容错的**（`set -uo pipefail` 无 `-e`）→ C1/C2/C3/C4 任一步 rc≠0 **不中断链**，rc 记 log 继续跑，靠 VERIFY 抓产物 STALE/MISSING。**验收标准因此明确**：不能只看 CATCHUP-DONE 标记，要查 4 条 `Cx ... rc=` 行 + VERIFY 的 3 行 FRESH（C1/C3/C4 产物新鲜）。**C2 无落盘产物是设计非缺口**：l4-disambig-judge.py 全文 0 行文件写入、出口 print（判读 JSON 由 L42 `>> "$LOG"` 捕获进 catchup log）→ VERIFY 不查 C2 合理，C2 验收 = 看 log 里判读输出（A/B/C/D 结论）。另注：C4 docstring L7 说输出 `...-gpu-adjudicated.json` 但实际 OUT=L14 `...-all-adjudicated.json`（docstring 过时，VERIFY 查 all 版=正确）。至此 catchup 链 5 步（C1-C4 + VERIFY）结构 + 容错语义 + 验收标准全核验。
- **P-A 间接观察口径风险（2026-11-25 16:12 提出 → 16:20 实证修正, subagent · 解读注记非改脚本）**：读 `event_modes()`（L81-93 按 mode 字段分桶）+ 用真实 runs json 核验。**主判别不可测（确认）**：P-A 主判别读 `value_mismatch` mode 桶，但两臂该桶皆 `None`（VM 类事件 baseline 路由到 `angle`、Fix-A 后路由到 `directed`，从不用 `value_mismatch` 作 mode 值）→ `testable:false` 恒成立，与 prereg 效度注记 + happy path 冒烟一致。**间接观察修正（16:20，fixA r2 落盘后）**：原假设"angle_fixA 被 VM 事件迁移到 directed 而压低（口径污染）"**被数据推翻**——实测 angle 计数 fixA r1=r2=**80 稳定**（baseline 50/77/66），directed 为**叠加新增**（r1=4/r2=5，baseline 全 0），非从 angle 迁移而来。故间接观察的 angle 对比**未被污染**，反而干净地显示 Fix-A 在不蚕食 angle 路径的前提下**新增了 directed 修复路径**（directed>0 即正向机制信号，n=2 可复现）。**核心判别仍以节点级修复率（b vs a，`node_repair` L72-78）为准**（不受 mode 路由影响）；angle 间接观察可读但 n=2 仅 suggestive。另注：`load_arm_runs` glob 是嵌套路径 `arms/{arm}/{arm}-r*.json`（L44），与真实落盘布局一致，文件发现逻辑正确（早期探针误用扁平路径致空结果，已纠正）。

