# PFB 完整探索历史脉络（前 S 版本 + T1-T8 专题）

> origin: ai · 2026-11-26 · D 问「S 已经很后面了，前面十几个版本呢，还有更多的 t1-8 这些呢」
> 定位：`exploration-history.md`（v2，权威编号映射）覆盖 v3-v19 主线叙事；本文件补齐它没展开的三段——
> ① 十月 pre-bench 时代（stage-ablation 之前的整个仓史）② v1-v15 逐版本细节（"前面十几个版本"）③ T1-T8 的多重命名空间（"更多的 t1-8"）。
> 来源标注：①=本轮 git log/文件实读；②=exploration-history.md（11-11，按新鲜度降档）；③=numbering-audit-2026-11-11.md。

## 0. 全仓分期总览（5 个时代）

| 时代 | 时间 | 主角编号 | 一句话 |
|------|------|---------|--------|
| E0 十月 relay+loop 时代 | 10-24~11-02 | r5-r154、E01-E28、T6/T7.1/T8(Oct) | 仓最初是视频 episode relay 仓 + prompt-first 1-loop 实践场（T8=prompt 消融研究 v1-v7 + rubric-v3 迭代） |
| E1 bench 建立+四臂基线 | 11-03~11-07 | T17-T25、S0-S5、T0-T2、runs-r293 | decomp 并入 pfb（T23），5 题 bench + gold + rubric v2/v3，四臂 n=30，S8 质询循环 |
| E2 S5 管线硬化 v3→v15 | 11-08~11-09 | v3-v15（"前面十几个版本"） | 往 prompt 堆规则期：每版本=一次 P1/P4 规则修改+单 rep smoke，判决=容量上限 |
| E3 状态机转向 v16→v17 | 11-09~11-11 | v16.x、v17 | 目标函数驱动转向；v17 层级 INDEX 爆炸（1930 节点）→ Goodhart 诊断 |
| E4 T53/v18 + v19 + 后续 | 11-11~今 | v18(T53)、v19(langgraph)、A0-A13、T1-T8(11月各命名空间) | 目标函数重写状态机；QC 消融矩阵；think-trigger/idea53 等新 goal 的 T 编号复用 |

**主线一句话**（沿用 exploration-history.md）：S5 臂从"往 prompt 里堆规则"（v3-v15，失败）→"目标函数驱动的状态机"（v16→v17→T53/v18），
中间发现 v17 爆炸本质是 Goodhart 刷分（目标函数只奖规模不罚冗余）。

## 1. E0 · 十月 relay + prompt-first loop 时代（10-24~11-02）

stage-ablation 不存在之前，pfb 仓干过两件正交的事（① git log 实读，10-24 起共 ~200 个 commit）：

### 1.1 视频 episode relay 线（10-24~10-26）
- 仓最初承载 d1-video-recreation 的 arena 渲染 relay：batch-8~11（E13-E28 集）、episodes.md、render_E01 布局标准、
  full_v1.3.4 风格锚、Opus 5.5 对标素材（封面+抽帧+contact sheet）、style-analysis.md（19936 字节）。
- 同期 bench r3/r4 校准（n=3 run mean 87.84±3.53 → 独立校准 76.45±7.29，自估偏差 +11.39 实证）——
  这是后来 judge 校准方法论（双判官/盲评/κ 检验）的源头。
- 残留：`outputs/full_v1.3.4.mp4`、`src/*.js` 渲染脚本（numbering-audit 建议迁移项）。

### 1.2 prompt-first 1-loop 实践线（10-28~11-02）
loop/prompt-first 六阶段流程的首批完整跑法，任务编号即"十月 T 系"（与十一月 T 系不同命名空间，见 §5）：
- **T6**（10-28~29）：换域效果验证 r1——机械键盘新域 01→04.5 完整 loop，三盲点修订全部生效 verdict pass。
- **T7.1**（10-29~31）：会议室预约系统选型，prompt-first 六阶段全流程首跑 + 交付报告 + 成本模型复跑。
- **T8**（10-29~31，十月命名空间）：**prompt 消融研究**，v1→v7 快速迭代：
  v2 现状盘点+文献调研+结构整改 / v3 可解释性加速消融 / v4 交叉矩阵+arena 内部流程对比 /
  v5 可解释性双实例对照 / v6 三机分工 / v7 vLLM 能力边界实测（ninfer 探针端点）；
  Part A 三卷审计（W1-W6 机械键盘域 / decomp-bench ablation-L1 / T7.1 会议室域，零表演三测）；
  矩阵 r1 立项（T-select×V-full 第三点）；r47/r48 hidden-state 探针（C1 第三条路→C3 top-k 锁定）；
  **C3 v3 方案 + 对抗核验**（r55/r55b/r59：6 质询方向，PASS-with-fixes，R4 全因子 8 组预注册冻结）。
- **rubric-v3 迭代**（r59→r69+，10-31~11-05 跨入 E1）：outcome(O1-O5)+process(P1-P4) 双层分离草案 →
  对抗核验 27 findings（9 blocker）→ O3 权重定稿 w_v=1+min(-log2 p̃, log2(1/ε)) → 权重消融任务书。
  11-05 收口：hetero-judge 验证 κ=+0.31，rubric v3.1 FINAL sign-off。
- **r 编号时代**：r5-r154 是 ralph-loop 主仓全局迭代轮号（每轮一个 commit 前缀 `rNN:`），
  含 market-alpha 双线（r75-r77）、RV3G3cdx/RV3G6 系列（r101-r154，五源盘点/映射表/多域升级）。
  11-06 的 r293 轮次出了 scores-v2（M1 judge 改进+Q4 gold 修正）→ 即 `runs-r293/` 目录来历（②）。

### 1.3 转折：decomp 并入 pfb（11-03）
- **T22/T23**（11-03）：decomp-bench 并入 pfb + 逐阶段子模块消融实验设计（stage-ablation 目录诞生，
  首个 commit `a03aa0694`）；gates.py 回填（8 单测通过）；T22 r2 12/12 补跑定案 S5 闸保留。
- competitor-survey（11-03，成璐指令）：开源 DRA 格局 + GPT Researcher 源码解剖 + 对标三层
  （L1 工程基线/L2 榜单 SOTA/L3 能力空白）。

## 2. E1 · bench 建立 + 四臂基线（11-03~11-07）

### 2.1 基础设施周（11-03~11-05）
- **research_hook 检索基建**：v2.1 ego-browser 联网通道验证（T25）→ v2.2 双策略 arXiv（all:+ti:）精度修复
  （S2-Q1 0.566→0.652，Q2 +0.068，Q3 回退识别）；T24 lit-survey 65 篇回执（H1 修正：非前置条件，跨文档任务稳健杠杆）。
- **judge 体系**：M7 维度设计（建模/矛盾推理）+ 90-run 全量打分 + LLM judge 交叉验证；
  7B 半异族 judge 尝试 FAILED（judge 能力不足）；ScientistTwo（arXiv:2609.19644）对照假设测试。
- **T17**（11-05）：final report（gate-fixed，cross-judge 对比）+ M7 章节 + 事实准确性诊断 + decomp 能力边界；
  T23-v2 hetero-judge 回执（H1 在 Q1 被驳，gate 缺陷暴露，M6 同源误报）。
- **v4 修复**（11-05）：M2/M5 测量偏差（sources-field fallback + 结构检测）。

### 2.2 四臂基线 + S8（11-06~11-07，exploration-history.md Phase 0/1 的展开）
- 5 道事实题（nat/soc/gpu/hw/bio）+ gold 要点表 + judge 口径（rubric v2）。
- **四臂 n=30**：S0=0.5558, S1=0.5746, S5=0.7907（B-face 跨族 judge 验证方向一致）；
  C-face 判官 FAIL；E3 机制=生成时预防。
- **runs-r293**：11-06 r293 轮次打分快照（scores-v2：M1 judge 改进+Q4 gold 修正），不是 run 配置（②）。
- **S8 质询循环**（11-07）：S8=S5+矛盾质询 loop，O6 均值 0.876；self-judge 系统性偏高 ~0.14（S8 0.783→0.642 B-face）；
  S8L（长 prompt 发散前段）/S8C（约束化模板）→ #24 任务类型路由修正为"结构效应待确认"；
  S8M（初筛式+质询深挖，11-08 凌晨）：Q1=0.900≈基线，Q5 judge 失效，#29 两预测成立→按题型分流路由。
- **S8B**（11-08 凌晨）：masked-condition-rebuild vs persona interrogation（T-PR-13 Q3a）：
  persona ~null（与 2311.10054 一致），mask-rebuild 双域阴性；attention-budget displacement 机制；
  历史 cache 审计（S0/S1/S2 n 虚高 ~1/3——8787 proxy 缓存相同 prompt，anti-cache jitter 进 call_llm）。
- **gap-to-gold 诊断**（11-08 凌晨）：nat 44% vs soc 95%；三个洞全是单位/维度错误（pt5 9/9 同向错）；
  A3 臂（dimension-discipline 一行）0.444→0.611 修 pt4 不修 pt5；A4 few-shot 臂 pt4 修好 pt5 仍漏
  （公式抽出来了但参数估计链独立）→ **expression-layer vs reasoning-layer gap 区分**（关键概念）。
- **G1-G5 报告**（11-08 凌晨）：S0 baseline 段（nat 0.600±0.205, soc 0.957±0.075）+ A3 双域阴性 +
  A4 弱阳性（0.622 vs 0.600, p=1.0 ns）+ production-final-report（论文定位）。
- **judge v2 连续分**（11-08 上午，v1/v2 时代的收尾动作）：coarse tree index + targeted deep-check 抽象
  → 深度梯度 rubric（nat 6pts×3-4 级）→ k·ln(k+1) 加权 → [0,1] 连续分（替代 0/1 级列表）→ 四臂全 strict 复分。
  注意：judge_v2_depth 上线本身被 exploration-history.md 记在 11-08 下午"v3 前后基础设施日"——
  即 v1-v2 没有独立的 runs 目录，是 judge 口径迭代期，v3 才是第一个有 runs 目录的版本。
- **n-expansion**（11-08 13:13）：temp=0.7+top_p=0.95 真采样（此前 temp=0 退化）；r51-101 归档 runs-prod-temp0。

## 3. E2 · v1-v15 逐版本细节（"前面十几个版本"，11-08~11-09）

exploration-history.md Phase 2 给了叙事，这里补 git log 逐版本锚点（① 实读 s5_pipeline.py 提交史 + runs 目录实测）：

### 3.1 v1-v2：无独立 runs 目录（11-08 午前及以前）
- v1/v2 是 s5_pipeline.py 的初版四阶段管线（P1 分解→P2 搜索→P3 核验→P4 综合）+ binary coverage 打分，
  数据混在 runs-s5-smoke / runs-s5-prod / runs-baseline 里，没有 runs-s5-gpu-v1/v2 目录（实测不存在）。
- 版本号锚点：v3 起才有 `runs-s5-gpu-v{N}` 单 rep smoke 目录（v3-v12 各目录恰好 1 个 rep 文件，实测）。
- 版本线官方口径（exploration-history.md §5，11-19 修订）：**v1-v15 = s5_pipeline.py 早期**
  （P1 分解 + P2 搜索 + P3 核验 + P4 综合），v16 起分叉。

### 3.2 v3-v9：基础设施日 + 规则堆叠期（11-08 下午~晚）
一天十几个 commit 把管线从"能跑"推到"能量化"（① s5_pipeline.py 提交时间线）：
- **v3 前后（14:46~15:48）**：judge_v2_depth 深度连续分上线（binary 之外加 k·ln(k+1) 加权）；
  内外校验链闭合；来源标签（given/knowledge/search）强制进正文（≥3 inline）+ 可测量标签统计；
  P4-only rerun 支持（_fact_table_override）。
- **v4（runs-s5-gpu-v4 实测：depth 0.228, cov 0.200, 23 nodes）**：基础设施日后首个 gpu 单 rep。
- **v5-v6（17:08~17:28）**：--workers 并发 rep 执行 + goal-pfb-full-run；n_verified KeyError 修复；
  **P1 迭代分解（3 层树，8→25 节点）**+ JSON retry。
- **v7-v9（19:10~19:42，runs-s5-gpu-v7 实测：depth 0.167, cov 0.267, 17 nodes）**：
  P1.5 两遍 gap check（A=独立维度/B=补洞）+ prompt 完全通用化（无领域示例）；
  P1 rule 6（复合词展开）+ P3 放宽核验；P1 rule 7（定义节点必须展开到可计算项）。
- **关键转折（11-08 晚）**：引入分解目标函数——先 Σn·ln(kₙ)，后对称化 S_α = Σ[n·ln kₙ + α·kₙ·ln n]（α=0.5），
  边际增益精确化 Δ=ln((k_n+1)/k_n)，替代固定节点数 band 做停止判据；
  GPU 题 rubric 重建（31 节点 gold-tree 1:1 对齐）；**D 指令：撤掉检索预算上限（21:58）**。

### 3.3 v10-v12：诊断 + 稳定性期（11-08 晚~11-09 凌晨）
- **v10（runs-s5-gpu-v10 实测：depth 0.249, cov 0.200, 37 nodes）**：exclusion 修复——
  排除性结果不该终止树（exclusion ≠ dead branch）。
- **v11-v12（runs-s5-gpu-v12 实测：depth 0.377, cov 0.267, 40 nodes）**：规则堆叠后期；
  P4 rule 6 口径分离（byte vs request hit rate 分开报）；P1 rule 8 子问题覆盖；
  P1 rule 9 定量承诺（每节点必须带数字/公式）；P4 rule 5 反 hedging
  （69% 的 p4-miss rep 明明有 verified 公式节点却说"无法给出定量"）。
- **v13 稳定性 runner 上线**：50-rep 首跑 r5 截断失败→根因是 early-stop 不是 max_tokens。
- **归因审计结论：P1 > P4 > retrieval**（丢分大头在分解层不在检索层）——这条决定了后面所有版本的火力方向。

### 3.4 v13 判决 + v14 量产 + v15 转向（11-09）
- **v13（runs-s5-gpu-v13 实测：34 个 rep 文件，depth_score mean 0.384）**：round-3 判决 **gpu FAIL（0.389 < 0.50）**。
- **v14（runs-s5-nat-v14 / runs-s5-soc-v14 实测：nat 101 reps，mean cov 0.573）**：
  早期 0.605（+0.070），量产仍低于 S0 的 0.637；
  rule 9b 两次变形：硬件 spec-table+TCO 公式强制（领域规则）→验证失败→换通用参数敏感性分析；
  soc rule 7 同构失败（point-0 命中率 54%→17%）。
- **v15**：阶段分离原则落地——P1 删敏感性规则（纯分解），P4 新增分析层
  （对 verified fact table 做敏感性/条件推断/分布估计）；smoke 6/6：mean cov 0.361，方差极大（0.0~0.667）。
- **判决（v15 + soc rule 7 两个独立证据）**：prompt 层行为塑造有容量上限，继续加 rule 稀释基础覆盖，负收益。
  → goal v3 分解落盘（decomposition-goal-v3.md）：杠杆换方向——① 结构（状态机）② 激活（推理倾向）。
- 同期 **S0-gpu baseline 收口（n=10 cov=0.167）**：gpu 题难是模型天花板，不是管线丢失。
- **T0/T1/T2 措辞梯度臂**（11-07 17:12 立项，11-09 数据落盘，runs/ 下 T0/T1/T2-Q1/Q2-r1-r5 实测存在）：
  机器指标 T2 gap/kTok 2.12 > T0 1.42 > T1 0.66，T1 最省 token；
  T2 短 prompt 在 GPU 域试跑（T53 前身记录：M1+0.329 但 M6=-1/M5-0.287，cascade L1 档需结构约束）；
  T2+research_hook 重跑（T53b：total 与 S5 持平 p≈0.32，M1+0.226，速度减半）。
  注：这是 runs/ 内唯一存在的 T 前缀臂（T3-T8 无 phrasing 臂数据，见 §5）。

## 4. E3-E4 · v16→v19 主线（11-09~11-19，与 exploration-history.md 对齐）

此处不重复叙事（Phase 3-5 见 exploration-history.md），只补版本线锚点（① 实读）：
- **v16-v16.3**（11-09）：P1e 状态机臂（多轮回退分解 + confirmed-fact 注入 + S_α 边际停止，R1-R4 规则演化）。
- **v17**（11-09 14:41 立项，11-11 爆炸数据浮出）：层级 INDEX 分解，1930 节点/10 轮/有效维度仅 6-8，r10 HTTP 502 崩。
- **v18 = T53 状态机**（s5_state_machine.py，① 首个 commit ae26341e8 11-11 20:26）：
  {IDLE, DECOMPOSE, VERIFY, REWORK, STOP} + J_necessary/J_verify/J_stop 机器裁决；
  工程迭代 r1-r6（sm-modification-log.md）；smoke v5=75 nodes/2 rounds/0 leaks，r7=133 nodes/2 rounds/0 leaks。
- **v19 = langgraph 控制流**（langgraph-pfb-full.py，① 首个 commit b0fb66a29 11-19 00:05）：
  修 recursion limit（nat N254 超限）；同期 A0-A13 QC 消融矩阵立项（4 因子 D1-D5，14 臂×3 题×3 rep=126 runs，
  11-18 补 A10-A13 二阶交互角点；no_challenge 臂假阴性修复 P3_VERIFY_NC）。
- **版本纪律**（11-19 修订，exploration-history.md §5）：版本线连续 v1→v19 不断档；
  S5 线代码大改继续 vN 不跳 T 编号；轮次放子文件夹；基座 prompt（formula/text/minimal/method/method_challenge）作子标签。

## 5. "T1-T8" 的多重命名空间（D 问的"更多的 t1-8"）

**结论先行：pfb 仓里 T 编号至少 4 套命名空间并存**，"t1-8" 在不同语境指完全不同的东西。
（① 本轮 git log 全史实读 + ② numbering-audit-2026-11-11.md 任务 ID 双轨制记录）

| 命名空间 | T1-T8 指什么 | 时间 | 证据 |
|----------|-------------|------|------|
| **NS1 十月 prompt-first 任务系** | T6=换域效果验证（机械键盘域 loop 首测）；T7.1=会议室预约系统选型全流程首跑；T8=prompt 消融研究 v1-v7+C3 v3+rubric-v3 迭代 | 10-28~11-05 | git log `T6 任务书`/`T7.1 任务书`/`T8 v2..v7`/`T8 Part A 分卷 B/C` |
| **NS2 stage-ablation runs/ 臂系** | T0/T1/T2=措辞梯度臂（phrasing-gradient，Q1/Q2 n=5）；**T3-T8 无此命名空间的臂数据**（runs/ 实测只有 T0/T1/T2 + D1/D1deep） | 11-07~11-09 | commit 2a4c16b6c（11-07 17:12）+ runs/T0-Q1-r1.json 等实测 |
| **NS3 十一月 goal 任务系（think-trigger）** | T1=思考触发 hook 实现；T2="接着考虑"实验；T3=落点整合；T4=修脚本卡住→general 思考升级触发；T5=流程索引层（咒语=调度器 ROUTING.md）；T6=SOP 检查点效果验证；T7=always 层加牙（自评式→可执行式）；T8=pfb 六阶段 vs 直接求解 GPU 题（T8b smoke/T8c token-matched 对照） | 11-24~11-26 | tasks/think-trigger/decomposition.md 任务表（全 ✅/进行中） |
| **NS4 cc/夜间任务书系** | T1 核验/T2 套磁/T3 related work/T4 臂标注/T5 sweep（消融矩阵+前人标记）；另一份夜间任务书 T1-T5=langgraph gpu 题+汇总+commit，T6=A0-A13 sweep | 11-18 | experiments/stage-ablation/cc-tasks/ablation-prior-marking.md + ralph-loop-night.md |

**易混点澄清**：
- NS3 的 T8（think-trigger，11-25）与 NS1 的 T8（十月 prompt 消融）同名不同物；
  NS3 的 T8c smoke 即当前在跑的 t-repair1 fixB arm 所属实验线（PID 28232 时代，11-26 已确认结束）。
- NS2 的 T0-T2 是**臂编号**（与 S0-S8 同级，出现在 runs/ 数据文件名里），不是任务 ID。
- numbering-audit（②）记录的"任务 ID 双轨制"：主 tasks/ 到 T53C，stage-ablation/tasks/ 到 T54，
  另有 R*/G*/B*/C* 单字母前缀 + T7.1/R5.1 小数点——本表 NS1/NS3/NS4 就是双轨制的活样本。
- **编号纪律现状**：11-19 修订只管住了 v 线（v1-v19 连续）和 S 线（S9 起递增）；T 线仍是多命名空间，
  新 goal 复用 T1-T8 是常态（每个 goal 的 decomposition.md 内部自编号），跨 goal 引用必须带 goal 前缀。

## 6. 编号体系速查（五套，合并 exploration-history.md §0 + numbering-audit）

| 前缀 | 含义 | 备注 |
|------|------|------|
| S | 实验臂（S0-S8M，S9 起递增） | S5=decompose→search→verify→synthesize 四阶段 |
| v | S5 线 prompt/代码版本（v1-v19 连续） | v16 状态机分支/v17 层级 INDEX/v18=T53/v19=langgraph |
| T | 任务 ID（多命名空间，见 §5） | 跨 goal 引用必须带 goal 前缀 |
| r | ① run 内 rep/round（scorer 硬编码格式）② 工程迭代轮（sm-modification-log）③ 历史遗留：r293=主仓全局轮号 | 三个命名空间，易混 |
| A | QC 消融矩阵臂（A0-A13，4 因子） | 11-18 补 A10-A13 交互角点 |
| E | 十月视频 episode（E01-E28+，relay 时代） | 与实验无关的历史残留 |

## 7. 来源与置信度
- ① 本轮 git log 全史（1944 commits）+ 文件实测（runs 目录 rep 计数/s5_pipeline.py 提交史/INDEX.md）：可直接复现。
- ② exploration-history.md（11-11 v2，11-19 修订 §5）：v3-v15 叙事与 runs 映射的权威源，按新鲜度降档（其 v16.3/v17 数据为 11-09~11 实测回填）。
  ⚠️ 双副本漂移（① 实测 diff）：`knowledgebase/pfb-research/exploration-history.md` 是 11-19 修订**前**的旧快照——
  其 §5 编号纪律写"S5 线代码大改跟任务 ID 走（T53、T54…），不再发明 vN"，与 pfb 正本 11-19 修订
  （"继续 vN 编号 v18/v19，不跳 T 编号"+版本线 v1-v19 确认+基座 prompt 子标签）**直接矛盾**。
  以 pfb 正本为准；knowledgebase 副本是向量库镜像（INDEX.json src 指向 pfb 正本），同步滞后，引用时注意。
- ③ numbering-audit-2026-11-11.md：5 套编号体系盘点（归档于 archive/legacy-docs/）。
- 不确定项：v1/v2 的精确边界（无独立 runs 目录，只能从 s5_pipeline.py 提交史+judge 口径迭代推断，conf 0.7）；
  NS4 两份 cc 任务书的 T1-T5/T6 与 NS3 的 T1-T8 是否存在派发时序关联（未深查，conf 0.5，不影响主线叙事）。
