# Goal: PFB Production Hardening (v2, 2026-11-09)

**状态**: ACTIVE（替代 goal-pfb-full-run.md — 该文档的 S0/A3/A4×500 矩阵已被用户指令取消，数据冻结于 runs-prod/）
**来源**: 成璐 2026-11-09 "看看现在的goal，质检标准，计划，退出条件，如果让你长期自主执行有什么计划吗"

## 北极星（成璐 2026-11-09 指令 · 长期目标）

**深广信息目标函数 S_α = Σ[n·ln(kₙ) + α·kₙ·ln(n)] 是 pfb 的核心研究贡献**：把"答案的深度×广度"从隐式 reward model 变成 prompt 层显式可计算的目标，让模型自主调节分解树形状。近期用 S_α 引导推理（本 goal 的 Phase 1-4），远期目标是训练一个完全自适应的系统——自己构建准确的目标函数、在 Pareto 前沿上自主选择操作点（深度 vs 广度 vs 成本）。远期路线不阻塞近期执行，但所有设计决策（状态机终止条件、预算分配、judge 校准）都要向这个方向对齐。

**机制层延伸（成璐 2026-11-09 追加 · 升级为长期目标组成部分）**：S_α 不只是打分器，更是「no-query recall」的激活机制——LLM 训练时已学会领域知识但不问不想起来，分解树每下探一层就是一次外部化触发，拆到领域最小过程单元（如 prefill → tensor/标量/运算单元/带宽/指令发射）≈ in-context 内完成小白→专家转变。推论：① 状态机的停止判据 = 「节点已到不可再拆的定义级粒度」（自然饱和），与 S_α 边际收敛判据互为印证；② S_α 跨域饱和深度曲线可作「知识完备性地图」，比 cov/depth 更有解释力；③ 终极问题（开放，不承诺解决）：若分解能稳定达到各领域最小过程单元，是否构成 AGI 的必要条件之一（判断：必要非充分，缺跨域迁移/目标自设/持续学习维度）。

**T55 术语核验结果（2026-11-09 落盘 research/no-query-recall-survey.md，90 行 + 346 行搜索日志）**：无 established 单一专名（conf 中）。推荐工作性描述 *cue-/context-dependent access to parametric knowledge*。最接近的可操作概念是 **compositionality gap**（子题都会、组合题失败，Press et al. arXiv:2210.03350）；认知科学类比 cue-dependent forgetting（Tulving & Psotka 1971）；ELK / capability elicitation 是正式相邻方向而非同义词。四层区分（存储→可探测→任务中使用→主动提醒）均不互相保证。「decomposition depth 作为激活强度指标」无人做过经验证的通用测量——**这是 pfb 的差异化空间**。关键近邻：Probing the Knowledge Boundary（arXiv:2602.00959，递归主题树 L5W5 vs L2W2 提取量 6 倍，但深宽叶同时变化非独立因果）、SMoT（arXiv:2312.17445，外部状态机 14%→95%，支持我们状态机路线）。

T53 已完成（2026-11-09 落盘 `research/longterm-vision-survey.md`，402 行）：Q1 gap 确认（无人把树形闭式效用写进 prompt 让模型自调结构，conf 0.75）；Q2 生成时连续深广评分仍是 gap（事后评估侧 STORM/RACE/Beyond Retrieval 已标准化）；Q3 RL reward gap 窄但窗口收窄中（ReasonRAG/TreeRPO/SPA-RL/rubric-RL 正快速逼近，"拿着目标函数去训"应尽快做）；Q4 meta-objective learning 领域真实存在（Eureka/Text2Reward/OptiMUS/OMNI-EPIC 有 task-specific 版本），可跨任务泛化的元目标学习器未见，离完全自适应还差三步（§5.3）；Q6 有可引用定理护栏（PBRS 策略不变性、率失真 D*(R)、树目标 NP-hard）。

**统一框架（成璐 2026-11-09 追问 · 承整理）**：之前说"分解深度是 AGI 必要非充分，缺跨域迁移/目标自设/持续学习"——这三样其实都能收进同一个循环里：① **持续学习** = 对终极目标做分解后，每个未覆盖的缺口就是一次查询，查询结果回写记忆（分解 → 查缺口 → 学 → 更新地图），这就是持续学习的操作化定义，不需要额外机制；② **泛化** = 分解算子本身不含领域内容（懂的直接拆，不懂的查定义再拆），所以它天然跨域——"通用要求"本身就是泛化性的检验方式，不是独立维度。真正的开放项只剩两个：**目标自设**（谁来定"终极目标"是什么——目前是人定的，自动推导目标是 T53 Q4 的 gap）和**权重层固化**（prompt 层的分解激活每次都要重新触发，要变成"不问也想得起来"需要训练把行为写进权重，即 T53 Q3 的 RL 路线）。所以更准确的说法是：分解循环覆盖了 AGI 的"知识获取+组织"半边，剩下的是"目标从哪来"和"怎么不用每次都触发"。

**优先级裁定（成璐 2026-11-09 指令）**：两个开放项都不急——① 目标自设不急："这个做好了，他会完全分解我的目标"，即先把分解循环做扎实，人定的终极目标能被完整分解就是当前验收标准，自动推导目标留到以后；② 权重层固化不急："如果我能稳定 prompt+管线激活，不需要训练去妨碍 RL 成果"——prompt 层稳定激活是 RL 的前置而非替代，不抢训、不动权重。因此当前全部重心 = **把分解循环做到稳定**（状态机 + S_α 停止判据 + 跨域饱和验证），这也是 v3 plan 分支 B 的定位依据。

## 一句话目标

让 S5（分解→检索→验证→综合管线）**稳定超过 S0（裸 27b）**，在 nat 题上 mean cov ≥ 0.634（S0 当前值），并在 GPU 题上 depth ≥ 0.50；然后产出可发表级别的消融报告。

## 当前真实状态（2026-11-09 核对）

| 项 | 状态 |
|---|---|
| S0/A3/A4 量产 (runs-prod/) | **已冻结**：nat 391+30+30, soc 30+60+60。用户判定"够了"，不再续跑 |
| s5-prod nat | ✅ 100/100 完成。mean cov=0.533 < S0 的 0.634 → **不达标** |
| s5-prod soc | 🔄 10/100 进行中 (PID 57416) |
| v13 × 50 reps (GPU) | 🔄 6/50，r5 截断失败 (max_tokens)，有效 5。~3.5h 剩余 |
| T52 撞车调研 (arena) | ✅ 完成（prompt-decomposition-collision.md +758 行，含 Beyond Retrieval [2512.00986] / Dissecting Agentic RAG [2606.21553] 两个意外发现） |
| T53 长期方向调研 (arena) | ✅ 完成（research/longterm-vision-survey.md 402 行，Q1/Q3 gap 确认 + Q4 六线索 + Q6 定理护栏） |
| T54 推理激活调研 (arena) | ✅ 完成（research/reasoning-activation-survey.md，操作性激活成立 / 神经层未证实；P3 条件证据槽列为待试假说） |
| T55 no-query recall 术语核验 (arena) | ✅ 完成（research/no-query-recall-survey.md，无 established 专名 → 工作性描述 cue-/context-dependent access to parametric knowledge） |
| S0-gpu 基线 | ✅ 完成 n=10 cov=0.167 → GPU 是模型天花板非管线 bug（tasks/s0-gpu-baseline.md） |
| 已知缺陷 | ① P4 综合阶段 hedging（有 verified 数字却输出定性描述）② research_hook snippet 抽取可能为空 ③ P1 输出超 max_tokens 无重试 |

## 分阶段计划（长期自主执行）

### Phase 1: 修管线（本周内，不依赖新数据）
1. **P4 prompt 修复**：加指令"基于已验证事实做最大幅度定量推导，不要因个别缺失数据整体降级为定性描述"。改完用现有 fact table 离线重放 5 个 rep 验证（不调 LLM 全链）。
2. **research_hook snippet 诊断**：检查 .research-cache/ 里 snippet 字段是否为空；若空，定位是哪个通道（DDG lite / webfetch / web-LLM）没抽到正文。
3. **P1 max_tokens 提升 + 截断重试**：v13 r5 事故根因。max_tokens 从当前值提到 8192，parse 失败时自动 retry 一次（temperature 降到 0.3）。
4. **质检门禁 G1**：Phase 1 完成 = 三项修复 commit + 离线重放显示 P4 输出含具体数字的比例从 ~12% 提升到 ≥40%。

### Phase 2: 状态机重构（等 Phase 1 通过）
把线性 P1→P2/P3→P4 改成允许回退的状态机：
- 状态：P1_DECOMPOSE / P2_SEARCH / P3_VERIFY / P4_SYNTHESIZE / P4_EVALUATE
- 回退触发：P4_EVALUATE 发现某 verified 节点的具体数字没进最终答案 → 回 P4 重综合；P2 返回空内容 → 回 P1 换查询词重分解该分支
- 终止：S_α 收敛（Δ<ε）或预算耗尽或 max_iterations
- **前置**：Phase 1 的 snippet 修复必须先过，否则回退拿到还是空壳
- **质检门禁 G2**：GPU 单 rep smoke × 3，depth 均值 ≥ 0.50 且无死循环（单 rep wall < 30min）
- **北极星对齐点**：状态机的终止条件不用固定轮数/固定节点数带，用 S_α 收敛判据（ΔS_α < ε 或边际增益 < 阈值 → 停），预算分配向高不确定性节点倾斜——这是"目标函数驱动停止"的最小落地，也是远期自适应系统的原型

### Phase 3: 补跑对比（状态机版 vs S0）
- S5-v2 (状态机) × nat 100 reps + gpu 50 reps
- 与冻结的 S0-nat (391 reps) 同 judge 对比
- **质检门禁 G3**：S5-v2 nat mean cov ≥ 0.634（追平 S0）且 ≥25% reps 达到 cov≥0.8；gpu depth 均值 ≥ 0.50

### Phase 4: 论文与发布
- 跨臂消融报告（S0/A3/A4/S5-v1/S5-v2 × nat/soc/gpu）
- underdetermined 题的条件指标（verified 节点 gold 覆盖 + [待核验] 计数）
- 数据推 prompt-first-bench.git；T51/T52 撞车结论写入 related work
- **退出条件 E1**：报告含全部矩阵 + 统计显著性检验（bootstrap CI 不重叠或 p<0.05）

## 退出条件（何时停）

| 条件 | 动作 |
|---|---|
| G3 达成（S5-v2 ≥ S0） | 停止迭代管线，进 Phase 4 收尾 |
| G3 连续 2 轮未达成且改动已穷尽（P4/检索/状态机都试过） | 停下汇报：给出差距归因分析，等用户定方向（换题/换模型/接受负结果写成 analysis paper） |
| 8787 不可用 > 4h | 暂停所有 run，保留断点，恢复后自动续 |
| v13 50-rep 显示 depth 方差过大（std > 0.15） | 先查方差来源（哪类 rep 崩），不盲目加 rep |

## 自主执行规则（无人值守期间）

1. **每 2h 自检一次**：进程还活着？新 JSON 在产出？error 率 < 5%？任一异常 → 修 or 跳过坏 rep 继续。
2. **断点恢复**：失败的 rep 删文件重跑；同一 rep 连挂 2 次 → 标记 skip 并记录原因，不卡死整批。
3. **不擅自扩大范围**：不加新臂、不改题面、不动 S0 冻结数据。这些需要用户点头。
4. **对外动作一律不做**：邮件、Zenodo/arXiv 上传、公开 repo push 之外的任何外发 → 只留草稿和清单。
5. **决策日志**：每个非平凡决定（skip 哪个 rep、改哪个参数）写进本文件的 Decision Log 节。

## Decision Log
- 2026-11-09: **北极星写入**（用户指令"这是你的长期目标：规划、分解、反思，全局视角"）：S_α 深广信息目标函数 = pfb 核心研究贡献；远期愿景 = 自适应构建目标函数 + Pareto 边界选择的 AI。T53 调研已派发 arena（session 分支 arena/375c1f00），产出 research/longterm-vision-survey.md
- 2026-11-09: **北极星机制层延伸**（用户："这个可以让你作为目前长期目标吗"）：no-query recall 激活机制 + 定义级粒度停止判据 + S_α 跨域知识完备性地图，写入北极星节。T55 术语核验已派发 arena
- 2026-11-09: S0/A3/A4 冻结不续跑（用户指令 "s0怎么还在，关了吧"）
- 2026-11-09: RT-RAG 判定不适合对标，改为以 S0 为 baseline（详见 chat 记录）
- 2026-11-09: Phase 顺序定为 修管线→状态机→补跑→论文；snippet 修复是状态机的硬前置
- 2026-11-09: **修正两个错误诊断**（文件证据推翻了之前基于 raw[:3000] 截断存储的误判）：
  - (a) v13 r5 不是 max_tokens 截断——usage out=2128 < 8000，是模型 ~2100 token 处主动停笔。修复 = _extract_json 截断兜底 + retry 降温度（commit 5a3b6c17），对 r5 raw 实测可恢复 10/11 节点
  - (b) research_hook snippet 不是空的——全量审计 609 sources 全部有内容（arxiv 中位 500ch, ddg 222ch, web_llm 101ch）。真正的问题是 **local_corpus 通道污染**：_LOCAL_CORPUS_DIRS 只含 D1-gpu-research 语料，对 nat 题（CDN/Pareto/LRU）grep 出的"命中"全是 GPU 硬件文档。nat 100 reps 共 1506 个节点，evidence 里大量出现"参考来源[1]为GPU硬件规格...与该节点无关"——P3 在拿不相关的本地文档做核验，把本该 verified 的节点打成 degraded。已修（commit 39aa9536）：非 gpu 题禁用该通道
  - (c) **v13 早期信号偏负**：6 个有效 rep（r5 失败，r8 在跑）depth_score mean=0.389 std=0.061（r1 峰值 0.487，其余 0.316-0.430），cov mean=0.111。few-shot 纯结构示例可能没带来稳定增益，方差大。等 50-rep 完整数据再下结论；若 mean < 0.45，回退到 v8 配置对比
  - (d) **P4 口径分离根因定位 + 修复**（commit 2db5f907）：逐点归因发现 S5 vs S0 差距集中在 point 4（字节 vs 请求命中率口径分离，S5 58% vs S0 71%）。40 个 miss rep 里 39 个 fact table 有对应节点（37 verified）——不是 P1 分解缺失，是 P4 综合时把两种口径合并成一个值。新增 rule 6「口径分离原则」强制逐口径分别报告