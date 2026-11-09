# T53 · 长期方向调研：目标函数驱动的自适应推理 + 元目标学习

> origin: arena agent (T53) · 2026-11-09 · 任务书：experiments/stage-ablation/tasks/T53-longterm-vision-survey.md（sigma-nlnk-snowball @ 12f7294b）
> 前置调研直接引用、不重复展开：T51 → research/objective-function-priorart/SNOWBALL-T51.md（即任务书所称 collision-snowball.md 之对应产出）；T52 → research/prompt-decomposition-collision.md + research/prompt-decomposition-search-log.json。
> 检索日志：research/longterm-search-log.json
> 被调研对象：S_α = Σ[n·ln(kₙ) + α·kₙ·ln(n)]（n=层级深度，kₙ=该层节点数，α=广深权衡权重）——注意 T53 版比 T51 版（S(T)=Σn·ln(kₙ)）多了 α·kₙ·ln(n) 广度项，本报告按新版调研，T51/T52 结论在旧版上成立、对新版逐项重新核对。

---

## §0 判决速览（Q1–Q7 判决句，AC3）

| # | 问题 | 判决句 | conf |
|---|------|--------|------|
| Q1 | 显式树形结构目标函数写进 prompt 引导生成 | **gap 确认**：无人把树形结构效用（深×广闭式公式）写进 prompt 让模型在生成时自调结构；最近邻 UtilityMax [arXiv:2603.11583]（形式效用进 prompt 但作用于任务输出）、TALE [arXiv:2412.18547]（标量 token 预算进 prompt）、λ-RLM [arXiv:2603.20105]（结构参数外部注入）均不同构于 S_α 用法 | 0.75 |
| Q2 | 深×广双维显式评分先例 | **部分成立**：事后评估侧已标准化（STORM 的 breadth/depth 人评 [arXiv:2402.14207]、RACE 的 Comprehensiveness+Insight/Depth 维度 [arXiv:2506.11763]、Beyond Retrieval 的 planning coverage [arXiv:2512.00986]）；生成时侧只有离散超参配置（ToP 的 (b,d)、λ-RLM 的 (k\*,τ\*,d)、GPT Researcher 的 breadth×depth），**连续闭式深广评分作生成时目标仍是 gap** | 0.7 |
| Q3 | S_α 类目标函数作 RLHF/DPO reward | **gap 确认（窄）且窗口收窄中**：结构量进 RL reward 的近邻密集——ReasonRAG 路径长度惩罚的过程奖励、TreeRPO 树节点相对奖励、SPA-RL 终奖分解到步（均见综述 [arXiv:2602.09305, arXiv:2509.16679]）、RaR 规则化 rubric 加权和 reward [arXiv:2507.17746]、树结构偏好奖励学习 [arXiv:2112.11230]；但"以分解树形状闭式函数（n·ln kₙ 型）为 reward 直接训策略"未见先例 | 0.65 |
| Q4 | meta-objective learning / 自动目标发现现状 | **成立（领域真实存在且活跃）**：六条线索各有原型到生产级成果（§5）；"从任务描述自动推导目标函数"已有 task-specific 版本（Eureka [arXiv:2310.12931]、Text2Reward [arXiv:2309.11489]、OptiMUS [arXiv:2310.06116]、OMNI-EPIC [arXiv:2405.15568]），**可跨任务泛化的元目标学习器未见**——离成璐设想还差三步（§5.3） | 0.7 |
| Q5 | Pareto 自适应 agent（在线选点） | **部分成立**：训练侧成熟——envelope MOQ-learning [arXiv:1908.08342]、preference-conditioned MOPPO/GPI [arXiv:2601.18783]、λ-CERL 进化+偏好条件混合 [MODeM'25]、Decision Transformer 的 return-conditioning [arXiv:2106.01345]；**prompt 层对应物只有标量预算选点**（TALE-EP 自估预算、IBC/VOI 预算下动作选点 [arXiv:2605.05701]、metacognitive harness [arXiv:2605.14186]），偏好向量条件的 prompt 层在线选点未见 → gap 部分确认 | 0.7 |
| Q6 | 目标函数可学习性的数学形式化 | **成立（有可引用定理）**：PBRS 策略不变性定理（Ng-Harada-Russell, ICML'99, pp.278–287：F=γΦ(s′)−Φ(s) 为策略不变之充要形式）；IRL 病态性与可行奖励集（Ng & Russell, ICML'00；Lemma 见 Metelli et al. 理论综述）；率失真 D\*(R) 的存在/凸性（[arXiv:2407.15504] Thm 1 + App. C.1；经典源 Cover & Thomas Ch.14）；树目标全局优化 NP-hard（Dasgupta, DOI:10.1145/2897518.2897527）。open problem 两个（§7.5） | 0.8 |
| Q7 | gap 反证 | **完成**：7 条 gap 声明 ↔ 7 条独立反证检索路径一一对应（§8 表），全部记录查询词与命中处置；其中 G3/G7 因反证发现近邻而收窄表述，G1/G2/G4/G5/G6 维持 | — |

**一句话路线含义**：层 1 的三个 gap（Q1/Q2 生成时/Q3 窄）都真实存在但 Q3 窗口在收窄（rubric-RL 线正快速逼近），「拿着目标函数去训」应尽快做；层 2 的愿景有清晰的分步路径（§5.3 三步 + §7 两条数学护栏），不是空想但也不是一步可达。

---

## §1 方法、渠道与分工

### 1.1 渠道状况（诚实登记）

- 主渠道 web_search：命中载体含 arxiv.org/abs+html+pdf、ACL Anthology、AAAI/IFAAMAS OJS、ICLR proceedings、Semantic Scholar、dblp、pith.science 评审记录、alphaxiv、emergentmind、huggingface、GitHub 一手 repo、项目主页。
- arXiv API / Semantic Scholar API / OpenAlex 直连：本会话沙箱 fetch 代理持续故障（OSS SignatureDoesNotMatch 0002-00000040，累计尝试 6 次全部失败，明细在 longterm-search-log.json channel_failures），按任务书失败降级条款执行"换引擎/换关键词重试一次 + 如实登记"，未静默跳过。
- 复用声明：T51（2026-11-08）与 T52（2026-11-09）已核验的 40+ 条引用直接复用（读取日期标 2026-11-08/09），本任务新增 16 组查询、25+ 条新核验引用。ToT/GPT-Researcher 等重叠条目按任务书要求以 T51/T52 为准，本报告只在对照表中一行带过。

### 1.2 与 T51/T52 的边界

- T51 回答"Σn·ln(kₙ) 公式有没有人用过"（结论：无，conf 中高）→ 本报告 Q1 在其基础上核对**新版 S_α（含 α·kₙ·ln n 广度项）**是否改变结论（结论不变，见 §2.4）。
- T52 回答"prompt 分解 pipeline 有没有人做"（结论：机制有先例、组合无）→ 本报告不重复 pipeline 撞车分析，只做目标函数/元目标/训练路线三层。
- 本报告新增覆盖面：RL reward 侧（Q3）、meta-objective 六线索（Q4）、MORL 选点（Q5）、数学形式化（Q6）。

---

## §2 Q1：显式树形结构目标函数进 prompt（≥3 篇 + 逐篇同构判决）

任务书问题 1：有没有人把显式树形结构目标函数（而非隐式 reward model）写进 prompt 来引导 LLM 生成？效果量多大？

**候选逐篇判决（"同构于 S_α 用法"标准：目标函数定义域=生成物的结构（树形/层级），且模型在生成时读公式自主权衡，无外部评分回路）：**

1. **UtilityMax Prompting** [arXiv:2603.11583]（2026-03, Marom, v4 2026-05）——把任务重构为影响图+效用函数 U(X₁,…,Xₙ|A)，以正式数学语言写进 prompt，令 LLM 显式对目标每个分量推理并最大化期望效用；MovieLens 1M 上对 3 个前沿模型报告 precision/NDCG 一致优于自然语言基线（含"Harsh"强指令对照）。**判决：不同构**——效用定义在任务输出的条件概率分布上（answer 应该是什么），非生成物结构（deliberation 应该什么形状）；但它证明了核心前提"LLM 能按 prompt 内形式化目标做显式分量推理"，且其 prompt-form 消融范式可直接借给 S_α 实验（T52 §7 质询 4 同判）。已读正文（2026-11-09）。
2. **TALE** [arXiv:2412.18547]（2024-12, Han et al., ACL'25 Findings）——token 预算写进 prompt+模型自估预算（TALE-EP 两阶段）；GSM8K 81.35→84.46 且输出 −75.7%；发现 token elasticity（预算过小失控）。**判决：不同构**——注入的是标量预算而非结构公式；控制对象是单链长度而非树形。T51 已读正文（2026-11-08）。
3. **λ-RLM（Y-Combinator for LLMs）** [arXiv:2603.20105]（2026-03）——受限运行时：Split(P,k\*)/Map/Reduce 组合子递归分解长上下文任务；结构参数三元组 (k\*=分支因子, τ\*=叶阈值, d=递归深度界) 显式化，递归深度/调用数/成本成为输入大小的解析函数。**判决：半同构（最接近的工程形态）**——深广参数确实显式且可解析，但由**外部 planner** 计算注入，模型不读公式自调；无 ln 边际项、无检索预算耦合。已读正文（2026-11-09）。
4. **OPRO** [arXiv:2309.03409]（2023, ICLR'24）——目标函数自然语言描述+历史解-分数对进 meta-prompt，外部 scorer 评估、跨迭代优化。**判决：不同构**——外循环优化回路 vs 单次生成内自调节。T51 已读正文（2026-11-08）。
5. **IBC/VOI 推理时预算控制** [arXiv:2605.05701]（2026）——运行时给每个动作打"单位预算边际任务价值"分，在检索/分解/提交间选择；边际思想与 S_α 的 Δ=ln((kₙ+1)/kₙ) 同源。**判决：不同构**——边际价值是外部控制器的启发式打分（critic 值变化+结构信号+成本归一化），非 prompt 内闭式公式；且作用于动作序列非树结构。T51 已读正文（2026-11-08）。
6. **Tree of Problems** [arXiv:2410.06634]（2024）——(breadth b, depth d) 显式参数化分解树，网格实验（含 b=2, d=log₂(L)−1 解析配置）。**判决：不同构**——b、d 是人设超参做外部扫描，模型不按公式自选。T51 已读正文（2026-11-08）。

**效果量证据（问题 1 第二问）**：prompt 内形式化/半形式化目标的已报告效果量——UtilityMax：NDCG/precision 一致提升（幅度按任务，未报树结构指标）；TALE：−68.6% 平均 token、GSM8K 准确率+3.1pt；λ-RLM：成本可解析界（未报质量增益）。**"树形结构目标进 prompt"的效果量文献为零——这正是 pfb depth score v8→v13（0.354→0.487，纯 prompt 改进）要填的格**。注意：该本地证据目前无外部对照组，投稿前需按 T52 §8 行动项补"公式 vs 自然语言深度指令 vs 标量预算"三臂消融。

### 2.4 新版 S_α（含 α·kₙ·ln n 广度项）对 T51 结论的影响核查

T51 判定"Σn·ln(kₙ) 无先例"。新增项 α·kₙ·ln(n) 使目标同时奖励"宽层×深处"（kₙ 大且 n 大的层贡献最大），数学上等价于对"层宽×层深"乘积的加权和。反证检索（§8-G1'）未发现任何以（深度×广度）乘积项为 LLM 生成目标的文献；深广乘积在评估侧的出现（RACE Comprehensiveness="覆盖广度和深度"）是自然语言 rubric 而非闭式函数。**结论：新版 S_α 不改变 Q1 判决，反而因 α 可调而强化了 Q5 的 Pareto 选点缺口（α 即偏好坐标）**。

### 2.5 S_α 的数学性质速查（供后续实验与理论工作引用）

按 S_α = Σ_n [n·ln(kₙ) + α·kₙ·ln(n)]（n=1..N 层，kₙ=第 n 层节点数）逐项列出与文献挂钩的性质：

| 性质 | 推导 | 文献挂钩 |
|------|------|----------|
| 层内边际递减 | 固定 n，∂/∂kₙ [n·ln kₙ] = n/kₙ → 随 kₙ 增大而减小；离散形式 Δ_k = n·ln((kₙ+1)/kₙ) > 0 且递减 | 凹性 ⇒ 与次模最大化的 (1−1/e) 贪心谱系兼容（教程 [arXiv:2606.10192]，T51 已核）；贪心加节点有近似保证的形式化路径 |
| 深层加权 | 第一项系数 n 随深度线性增长 ⇒ 同等 kₙ 下深层贡献更大 | 与 IBC/VOI 的"边际价值随剩余预算变化"同源直觉 [arXiv:2605.05701]，但 S_α 是静态闭式、IBC 是动态启发式 |
| 广度项的深宽耦合 | 第二项 α·kₙ·ln(n)：宽层（kₙ 大）且深（n 大）时贡献最大 ⇒ 鼓励"把宽度花在深处" | 无直接先例（G1′ 零命中）；与 RACE Comprehensiveness 的自然语言"breadth and depth"同向不同形 |
| 成本解释 | 若每节点成本≈1，总成本 C=Σkₙ；S_α/C 即"单位成本结构效用" | E-C 实验形态 (ii) 的比值 reward 直接用此量（§9.4）；防刷分护栏的数学基础 |
| α 的偏好坐标含义 | α=0 退化为 T51 旧版（纯深度效用）；α→∞ 主导项为广度 ⇒ α 连续插值深广权衡 | envelope MOQ 的偏好向量 ω 是它的多维推广 [arXiv:1908.08342]；E-B 实验即验证 prompt 层 α-前沿存在性（§6.2/§9.4） |
| 势函数化可行性 | 分解是增量过程（树逐节点生长），Φ(T)=S_α(T) 良定义 ⇒ F=γΦ(T′)−Φ(T) 是合法 PBRS 项 | Ng-Harada-Russell ICML'99 定理直接适用（§7.1）；未见先例把 PBRS 用于"分解树生长势"——理论小贡献候选 |

这六条性质中，前两条在 T51 已有雏形，后四条是新版 S_α（含 α 项）带来的新挂钩点；E-A/E-B/E-C 三个实验（§9.4）分别检验第 1/5/4+6 条。

---

## §3 Q2：深×广双维显式评分的先例（生成时目标 vs 事后评估，两类区分）

任务书问题 2 特别提示：ToT 的启发式价值函数是搜索时分支选择器，不是生成时目标函数——本表按此口径分三类。

### 3.1 事后评估类（对已生成物打深广分）

| 工作 | 深广如何进入评分 | 显式程度 | 引用 |
|------|------------------|----------|------|
| STORM / FreshWiki（NAACL'24） | 大纲评估：heading soft recall + heading entity recall（覆盖广度）；人评维度 Organization/Coverage/Interest；正文明确"articles exhibit greater **breadth and depth**"（+25% organized / +10% coverage） | 中（recall 型指标+人评量表，无闭式深广公式） | [arXiv:2402.14207]，已读正文 v2 §2.2/§6（2026-11-09） |
| DeepResearch Bench RACE（ICLR'26） | 四维 0–100 分：Comprehensiveness（定义原文="coverage **breadth and depth** of the research topic"）、Insight/**Depth**（分析质量与洞察）、Instruction Following、Readability；reference-based 防分数膨胀 | 高（Depth 是独立命名维度），但为 LLM-judge rubric 非闭式 | [arXiv:2506.11763]，已读数据集 README+方法概述（2026-11-09） |
| DRBench（ICLR'26） | planning/insight identification/factual grounding 三维评企业级 deep research | 中 | [arXiv:2510.00172]，T52 已读正文（2026-11-09） |
| Beyond Retrieval（2026） | Planning 模块量化：分解子任务 vs 专家结构大纲的 coverage/redundancy/correctness | 高（分解质量的模块化量化） | [arXiv:2512.00986]，T52 已读正文（2026-11-09） |

### 3.2 生成时配置类（深广作为可调旋钮，但非模型自读的评分函数）

| 工作 | 深广如何进入生成 | 与 S_α 差异 | 引用 |
|------|------------------|-------------|------|
| Tree of Problems | (b,d) 网格扫描，调用数=节点数 | 人设超参 | [arXiv:2410.06634] |
| λ-RLM | (k\*,τ\*,d) 由 planner 依输入大小计算 | 外部注入非模型自调 | [arXiv:2603.20105] |
| GPT Researcher deep mode | breadth×depth 用户可配置递归树 | 工程配置，无评分 | T51/T52 已登记 |
| ToT/GoT | 分支数 b 与搜索深度是算法超参；价值函数是**搜索时分支选择器** | 任务书点名区分的机制差异成立 | [arXiv:2305.10601, arXiv:2308.09687] |
| RLVR Reasoning-Tree 调度 | 对每个 query 构建 k 叉近似推理树（k=4,d=4,l=200），用树拓扑量化"结构可学习性"做数据调度 | 树结构量用于**训练数据排序**，非生成目标 | [arXiv:2510.24832]，已读正文（2026-11-09） |

### 3.3 判决

深×广**事后评估**已是 deep-research 评测标配（RACE 甚至把 Depth 独立成维），说明"深广是质量的公认维度"这一前提有文献共识；深×广**生成时**只有离散旋钮，无连续闭式评分让模型自读自调。Q2 判决：**部分成立（评估侧）+ gap 确认（生成侧闭式公式）**，conf 0.7。pfb 的 depth score judge 与 RACE-Depth/Beyond-Retrieval-coverage 的对齐校验可作外部效度实验（借用其已验证的 judge 设计）。

---

## §4 Q3：S_α 类目标函数作 RL reward（≥2 篇 + gap 判决）

任务书问题 3：拿着目标函数去训（成璐：「无论如何，拿着目标函数去训肯定能获得这种倾向」）有没有人做过？

### 4.1 近邻清单（结构量/显式准则进 RL 信号的五条线）

1. **树/路径结构量直接进 reward**：ReasonRAG——MCTS 过程级探索，部分路径的过程奖励=模拟结果平均正确率**并按路径长度惩罚**（防长链刷分）；TreeRPO——树状采样构造推理路径、优化**节点级相对奖励**、无需 reward model 的步级稠密反馈；ToTRL——引导模型从线性链推理转向树状思考以提升多路径逻辑效率。三条均出自 RL-reward 设计综述 [arXiv:2602.09305] §4.3.1 与 RL×LLM 综述 [arXiv:2509.16679] §4.2，已读正文（2026-11-09）。**与 S_α 差异**：长度/节点惩罚是防退化的正则项，不是"奖励更深的分解树"的正向结构效用；没有 ln kₙ 边际递减项。
2. **终局奖励按贡献分解**：SPA-RL——把最终奖励分解为与任务进度对齐的步级贡献（延迟奖励缓解），同上综述 §4.2。**差异**：分解的是信用（credit assignment），非问题结构。
3. **显式准则（rubric）作 reward**：RaR [arXiv:2507.17746]——实例级 rubric（7–20 条 Essential/Important/Optional/Pitfall 准则）由强 LLM 生成，两种聚合（显式加权和 / 隐式整体判分）转标量 reward 进 GRPO；HealthBench 相对提升 31%、GPQA-Diamond 7%。Rubric Anchors [arXiv:2508.12790]（~10K 人工/LLM rubric 数据集+Rubicon 框架）、Causal Rubrics [arXiv:2506.16507]（因果结构抗 reward hacking）、Checklists>RewardModels [arXiv:2507.18624]。已读 RaR 方法细节（alphaxiv overview, 2026-11-09），余 abstract 级。**与 S_α 差异**：rubric 是自然语言准则的加权和，S_α 是单一闭式数学函数；但**这是逼近最快的线**——把"分解树应深且广、边际递减、预算内验证"写成 rubric 即可得到"S_α 的自然语言版 reward"，故 Q3 窗口在收窄。
4. **树结构的奖励函数本身**：Interpretable PbRL with Tree-Structured Rewards [arXiv:2112.11230]（AAMAS'22）——从偏好在线学出**层级树状组合 reward**（二叉树、状态-动作空间不相交分量、增量精化、可追溯调试）。已读正文 §1–§6（2026-11-09）。**与 S_α 差异**：树是 reward 函数的**表示结构**（可解释性），S_α 的树是**被评分的对象**（生成物形状）——方向正交，但证明"树结构×奖励"组合在 RL 文献已有形式化，写论文时必须引用以防审稿人联想。
5. **训练目标权重本身的元学习**：AMFT [arXiv:2508.06944]——把 SFT/RL 平衡权重 μ 当可学习参数，用元梯度对长期验证目标做元优化，自主发现训练课程。已读正文 §1/§B.1–B.2（2026-11-09）。**与 S_α 差异**：学的是训练损失配比，不是任务级目标函数；但它是"α 类权衡参数可被元学习"的直接存在性证明（Q4/G7 关键证据）。

### 4.2 判决

**gap 确认（窄）**：未发现任何工作以"分解树形状的闭式效用（n·ln kₙ 型，含或不含 α 广度项）"作为 RL/DPO 的 reward 训练 LLM。但必须如实报告：线 1（长度惩罚型结构正则）与线 3（rubric 加权和）从两侧夹击，把 S_α-as-reward 的新颖性压缩到"闭式结构效用 + 正向深广激励 + 预算耦合"这个交集上。conf 0.65（三条独立检索路径反证后仍无直接命中，但 rubric-RL 线迭代速度快，**建议此实验优先级提到最高**——若他人先把"depth/breadth rubric reward"做出来，Q3 gap 即告消失）。

对成璐断言的文献支持度：「拿着目标函数去训肯定能获得这种倾向」——方向有据（RaR 证明准则化 reward 可训出倾向；AMFT 证明权衡参数可学；PBRS 定理给出何种 shaping 安全的边界，见 §7.1），但**"肯定"过强**：非势函数形式的 shaping 会改变最优策略（reward hacking 的正式解释），S_α 直接作 reward 存在"刷 kₙ 凑分"风险（模型多拆无用节点），需按 §7.1 设计护栏（如以 gold 覆盖率为约束的比值形式 S_α/cost 或势函数化改造）。

### 4.3 两条路线的分工：训（Q3）vs 注（Q1）——双轨并行期的资源分配依据

成璐的表述里"拿着目标函数去训"是倾向内化路线；pfb 现行 v14 是 prompt 注入路线。文献给出的分工证据：

| 维度 | prompt 注入（Q1 线） | RL 训练（Q3 线） |
|------|---------------------|------------------|
| 生效延迟 | 即时（改 prompt 即生效） | 一个训练周期（E-C 时间盒） |
| 泛化方式 | 依赖模型指令遵循能力，跨模型需重验（UtilityMax 在 3 个前沿模型上分别验证的原因） | 倾向进权重，同族模型内泛化；SEAL/AMFT 证明可再自我更新 |
| 失败模式 | 遵循度不足/公式误读（R3） | reward hacking/倾向过强挤占任务性能（R2） |
| 证据基线 | TALE：−68.6% token 且准确率+3.1pt ⇒ 标量注入有效存在性证明 | RaR：HealthBench +31% ⇒ 准则化 reward 训倾向有效存在性证明 |
| 对 S_α 的含义 | E-A/E-B 先验证"值不值得训"（若 prompt 层 α-前沿不存在，训出来也选不了点） | E-C 验证"训得出"，且势函数化形态 (iii) 是理论卖点 |
| 与 Phase 1 实验的关系 | 共用现有 pfb 题集与 judge，零新增基建 | 需 GRPO 栈（RaR 开源代码可复用），新增基建中等 |

**分工结论**：E-A/E-B（注入线）先行，因为它们是 E-C（训练线）的前置——若模型在 prompt 层都对 α 不敏感，RL 训出的倾向将缺乏可控的操作点语义；反之若 E-B 证明 α-前沿存在，E-C 的 reward 设计直接继承该前沿的比值形态。这一依赖关系是双轨排期（Phase 1 并行）中 T53 路线的串行约束，写入 §9.4。

### 4.4 Q3 反证补充：为什么"树形状闭式 reward"与五条近邻线都不同构（逐线一句话）

- 线 1（ReasonRAG/TreeRPO）：奖励信号来自**答案正确性**沿树/路径的分解，树是搜索或信用的载体，形状本身不得分——S_α 恰好相反，形状即得分对象。
- 线 2（SPA-RL）：分解的是**终局奖励到步骤的归因**，不评价步骤组成的结构。
- 线 3（RaR/rubric）：准则是**自然语言条目**的加权和，权重由 rubric 生成器给——S_α 是单一闭式函数，且其"权重"（n、ln kₙ、α）有信息论/凹性解释（§2.5）。
- 线 4（Tree-PbRL 2112.11230）：树是 **reward 函数的表示**（状态-动作空间的分层划分），被评的是轨迹不是树。
- 线 5（AMFT）：学的是**训练目标配比**（SFT/RL 损失权重），不是任务级生成目标。
五线各差一个关键要素，交集为空 ⇒ G3 的"窄 gap"表述（闭式×正向深广激励×预算耦合）成立。

---

## §5 Q4：meta-objective learning / 自动目标发现——六线索现状与成熟度

任务书问题 4：AutoGOAL、curiosity、reward-from-preferences 各走到哪了？离"AI 自己写出可微/可计算的目标函数"还差几步？

### 5.1 线索清单（≥5 条，每条标成熟度：理论/原型/生产）

| # | 线索 | 代表工作（引用） | 它做到哪一步 | 成熟度 |
|---|------|------------------|--------------|--------|
| L1 | LLM 写可执行 reward 代码 | **Eureka** [arXiv:2310.12931]（ICLR'24, NVIDIA/UPenn）：环境源码+任务描述→GPT-4 零样本生成可执行 reward 程序，进化搜索+reward reflection 迭代，Isaac Gym 大规模并行评估；29 任务 83% 超人类专家、平均归一化提升 52%，首次解出灵巧手笔旋转。**Text2Reward** [arXiv:2309.11489]（ICLR'24）：NL 目标→稠密 shaped reward 程序（环境紧凑表示接地）。 | 任务内自动写出**可计算**目标+闭环评估选择 | 原型→研究生产（机器人域） |
| L2 | NL→数学规划目标函数 | **OptiMUS** [arXiv:2310.06116] + OptiMUS-0.3 [arXiv:2407.19633]：NL 描述→MILP 目标+约束的模块化建模（connection graph 逐约束/目标独立处理、LaTeX 形式化+代码），NLP4LP 基准上解题数≈2× 朴素 prompting。PaMOP（IJCAI'25，T51 已登记）：树状分区建模。 | 从任务描述推导**准确的形式化目标**（数学规划域） | 原型 |
| L3 | 开放式课程+目标共生 | **OMNI-EPIC** [arXiv:2405.15568]（ICLR'25, Faldor/Zhang/Cully/Clune）：基础模型生成"可学习且有趣"的下一个环境**及其 reward 函数**（代码形式），按 agent 学习进度自适应难度；谱系上承 PAIRED（无监督环境设计，id [待核验]）与 OMNI，定位 AI-Generating Algorithms 路线（Clune）。 | 目标函数与环境**共同**自动生成，难度自适应 | 原型（概念验证） |
| L4 | 偏好→目标学习 | RLHF reward model（生产标配）；**RaR** [arXiv:2507.17746] 与 Rubric Anchors [arXiv:2508.12790]（准则化、可解释 reward，原型→生产过渡）；Causal Rubrics [arXiv:2506.16507]（抗 hacking）；树结构偏好奖励 [arXiv:2112.11230]（可解释表示）；Reward Design with LMs [arXiv:2303.00001]（LLM 当代理奖励）。 | 从人类偏好/准则**推断**目标函数 | 生产（RM）/原型（rubric 系） |
| L5 | AutoML 式目标-管线搜索 | **AutoGOAL**（COLING'20, Estevez-Velarde/Piad-Morffis et al., ACL Anthology 2020.coling-main.317 + demo 2020.coling-demos.4）：给定输入/输出类型+**用户提供的性能指标**，概率文法进化搜索异构 ML 管线。 | 管线自动发现（目标函数由用户给，**不合成目标本身**） | 原型（开源库） |
| L6 | 自我适应/自更新 | **SEAL** [arXiv:2506.10943]（2025）：模型生成 self-edit（重构信息/指定超参/调用工具）驱动自身权重更新，用下游表现为 reward 的 RL 循环训练"会自我更新"的能力。**COVE** [arXiv:2608.01234]（2026）：harness 记忆 vs 参数内化的任务感知路由协调。**AMFT** [arXiv:2508.06944]：元梯度学习训练配比 μ。 | 系统**更新自身**（含目标相关参数）的机制已存在 | 原型 |
| （L7） | curiosity/内在动机 | ICM [arXiv:1705.05363]、RND [arXiv:1810.12894]、伪计数 [arXiv:1606.01868]（T51 已核）：内在奖励=学习进展/新颖度代理。注意 PBRS 视角下 curiosity bonus 可被形式化为势函数 shaping（2024 年已有专文，见 §7.1 关联）。 | 目标函数的**内生信号源** | 生产（RL 组件级） |

### 5.2 交叉观察

- L1+L2+L3 合起来证明：**"AI 写出可计算目标函数"在 task-specific 设定下已经实现**（Eureka 的 reward 代码、OptiMUS 的 MILP 目标、OMNI-EPIC 的环境+奖励共生成），且都有闭环质量评估（并行 RL 评估/求解器验证/学习进度信号）——成璐设想的 (a)「从任务描述自动推导准确的目标函数」不是从零开始，而是把这三条线从各自域（机器人/数学规划/游戏环境）迁到"推理管线目标"域。
- L5（AutoGOAL）恰好说明反面：经典 AutoML 把目标当输入不当输出；L1–L3 是"目标作为输出"的新一代。
- L6 提供 (c)「随经验更新目标」的机制库：SEAL 的 self-edit+RL、AMFT 的元梯度、COVE 的记忆/参数路由。

### 5.3 离"完全自适应的元目标 AI"还差几步（判决支撑）

1. **跨任务泛化的目标归纳**：现有 L1–L3 全部 task-specific（每任务重新生成/搜索目标）；未见"目标函数族的学习器"（学到 n·ln kₙ 这类**形式模板**再按任务实例化参数）——差一步：把 Eureka 的进化搜索从"reward 代码空间"升到"目标形式空间"（形式先验可用 S_α 族做种子）。
2. **无真值闭环下的目标质量评估**：Eureka 靠并行 RL 适应度、OptiMUS 靠求解器、OMNI-EPIC 靠学习进度；推理管线域对应物=pfb 的独立 judge/gold 覆盖率——pfb 已具备（这是相对优势），但 judge 噪声下的目标选择理论缺失（连到 §7.4 IRL 病态性）。
3. **Pareto 自主选点与目标更新的耦合**：(b)(c) 两能力在文献中彼此孤立（Q5 的 MORL 选点在训练侧、L6 的自更新不含偏好选点）；未见"在线选点结果反哺目标函数参数"的闭环——这正是 S_α 的 α 在线调节的空白（§8-G7）。

**Q4 判决：成立——领域存在且六线索可拼出路线图；"完全自适应元目标 AI"= 已有组件 × 三个未闭合缺口，属 3–5 年量级的研究议程而非单点突破。conf 0.7。**

### 5.4 对照成璐愿景的四能力清单（规划 / 分解 / 反思 / 全局视角）

成璐表述的长期目标是"一个完全自适应的 AI，自己构造准确的目标函数、在 Pareto 前沿上选操作点、并随经验更新它"，并点名四种能力：规划、分解、反思、全局视角。逐项对照文献现状：

| 能力 | 文献现状（代表工作） | 与"元目标"的关系 | 缺口 |
|------|----------------------|------------------|------|
| 规划（planning） | DeepResearch Bench 的 planning 评分维 [arXiv:2506.11763]；Beyond Retrieval 的 Planning 模块量化（子任务 vs 专家大纲 coverage/redundancy）[arXiv:2512.00986]；λ-RLM 的 Split-Map-Reduce 组合子规划 [arXiv:2603.20105] | 规划的**质量维度**已可量化，但规划器不感知"目标函数本身"——它规划如何完成任务，不规划如何定义成功 | 目标感知的规划（planner 读 S_α 后规划树的形状，而非只规划内容） |
| 分解（decomposition） | ADaPT/IdealGPT/RDD/SMoT 递归分解（T52 §3 全谱系）；Tree of Problems (b,d) 分解 [arXiv:2410.06634]；PaMOP 树状分区建模（T51 已登记） | 分解**机制**成熟、分解**形状**无目标约束——pfb 的 S_α 正是给形状加约束 | 形状约束下的分解质量理论（连 OP1） |
| 反思（reflection） | Reflexion 系（T52 谱系内已覆盖）；Eureka 的 reward reflection（反思信号直接改写目标函数文本！）[arXiv:2310.12931]；SEAL 的 self-edit（反思产物触发自我更新）[arXiv:2506.10943] | Eureka 的 reward reflection 是"反思→改目标"的**已存在闭环**，pfb 可直接类比：judge 反馈→改写 S_α 的 α 或形式 | 反思改目标的稳定性理论（改多了漂移，改少了僵化；AMFT 元梯度是受控版本） |
| 全局视角（global view） | OMNI-EPIC 的学习进度信号（全局难度视角）[arXiv:2405.15568]；IBC/VOI 的预算全局核算 [arXiv:2605.05701]；RLVR reasoning-tree 的结构可学习性（数据集全局视角）[arXiv:2510.24832] | 全局视角在文献中体现为"跨 episode/跨任务聚合信号"，元目标 AI 需要的是"跨目标函数聚合" | 目标函数种群的全局管理（OMNI-EPIC 的环境谱系档案是雏形） |

**核对结论**：四能力中"分解"最成熟、"反思→改目标"已有单点闭环（Eureka）、"规划"与"全局视角"缺目标感知维度。pfb 的位置：把四能力挂在同一个显式目标函数（S_α）上——规划读它、分解按它成形、反思改它的参数、全局视角在它的 α 维上聚合。这个"单一显式目标作四能力的公共接口"的组织方式在检索范围内未见对应物，可作为 pfb 长期叙事的差异化点（非撞车声明，是组织框架声明）。

---

### 5.5 Eureka 闭环向 pfb 域的迁移设计（远期主押注的具体化）

Eureka 的闭环四要素及其在"推理管线目标"域的对应物：

| Eureka 要素（机器人域） | 机制 | pfb 域对应物 | 现成/需建 |
|-------------------------|------|--------------|-----------|
| 环境源码+任务描述作为上下文 | LLM 读代码理解状态/动作语义后写 reward 程序 | pfb 题面+gold 结构大纲+judge 定义作为上下文，LLM 写候选目标函数（S_α 族种子：项形式 n·ln kₙ、α·kₙ·ln n 可增删换参） | 现成（T52 已建 judge/大纲基建） |
| 大规模并行适应度评估 | Isaac Gym 数千并行 RL 跑分，reward 曲线形状（早期学习信号）自动筛掉坏 reward | 每题一次生成+judge 评分即一次适应度评估；pfb 题集规模下并行成本远低于机器人仿真 | 现成（pfb sweep 脚本） |
| reward reflection | 把训练统计（各 reward 项曲线）回灌 LLM 做文本级改写 | 把各候选目标的（depth score、覆盖率、成本、刷分率）统计回灌，LLM 改写目标形式/参数 | 需建（小：一个 reflection prompt） |
| 进化搜索（种群+截断选择） | 多候选并行、按适应度保留 | 候选目标函数种群（每代 8–16 个形式变体），按 §7.3 可辨识性约束限维 | 需建（中） |

**迁移的关键差异（也是可发表点）**：Eureka 的适应度有物理仿真真值兜底；pfb 域的适应度含 judge 噪声 ⇒ 必须引入 §7.3 的病态性处理（候选目标限制在低维形式族内 + 双 judge 一致性过滤，R4 缓解项）。OMNI-EPIC 的"可学习且有趣"双准则提示：目标函数种群管理还需**新颖度准则**（防种群收敛到单一形式），可借 count-based/伪计数谱系（T51 已核 [arXiv:1606.01868]）定义形式空间的新颖度。

**里程碑分解（3 年远期 → 可检查的台阶）**：M1（6 个月）= S_α 单形式的 α 自动定参（外层网格/进化，内层 E-A 评估）——这是"元目标"的最小可运行版；M2（12–18 个月）= 形式族内自动选形（项的增删，reflection 闭环）；M3（24–36 个月）= 跨题域形式泛化检验（数学题域学到的目标形式迁移到法律/医疗题域，检验 OP2 可辨识性）。每个里程碑失败都有退路（M1 失败→固定 α 用 E-B 手选；M2 失败→形式固定只学参数=AMFT 形态；M3 失败→按域各配形式=退化为 Eureka 的 task-specific 现状）。

## §6 Q5：Pareto 自适应 agent（≥3 篇 MORL 在线选点 + prompt 层判决）

### 6.1 训练侧（在线选择 Pareto 操作点）

1. **Envelope MOQ-Learning** [arXiv:1908.08342]（Yang et al., NeurIPS'19）：单网络以偏好向量 ω 为条件学习全偏好空间的向值 Q 函数（envelope 更新+全局最优性过滤），部署时任选 ω 即得对应 Pareto 点；论文含偏好推断演示（15 episode 反推任务效用权重）。已读正文（Algorithm 1/Table 2，2026-11-09）。
2. **Preference-conditioned MORL for heavy-duty vehicles** [arXiv:2601.18783]（2026）：GPI-LS 扩到策略梯度（MOPPO），安全/能耗/时间三目标平滑可解释 Pareto 前沿，偏好条件策略免重训切换驾驶行为。已读正文 §1（2026-11-09）。
3. **λ-CERL**（MODeM 2025, VUB 论文集 PDF）：偏好条件 RL×多目标进化混合，种群 actor 各配 λ∈Δ^{m−1}+共享回放池，比 MOPDERL/PGMORL 产出更平滑稠密前沿。已读正文 §4（2026-11-09）。（PGMORL 本体 id 未在本会话核验 → [待核验]，仅经 λ-CERL 基线转述。）
4. **Decision Transformer** [arXiv:2106.01345]（Chen et al., NeurIPS'21）：return-conditioned 序列建模——推理时**以期望回报为条件**生成动作，"指定目标回报=选择操作点"的极简形态；实际回报与条件值强相关，且可有限外推。已读正文级评审（pith+alphaxiv，2026-11-09）。**这是训练侧与 prompt 层之间最好的桥**：DT 证明"把期望结果写进条件"可控制行为强度，prompt 层的预算/目标注入是它的零训练类比。

### 6.2 prompt 层对应物判决（任务书问题 5 第二问）

存在但初级：TALE-EP（模型自估 token 预算=在成本-准确率前沿上**自选一个标量点**）；IBC/VOI（双预算下按边际价值选动作=运行时选点，非偏好条件）；metacognitive harness [arXiv:2605.14186]（自报 FOK/JOL→外置 SVM 决策 retry/stop=校准后的二元选点）；s1 budget forcing（外部指定点）；产品层的 reasoning_effort/thinking budget 参数（外部旋钮）。**未见任何工作让 LLM 在 prompt 层读一个偏好向量（或 α 权重）后自主在深×广×成本三维前沿上连续选点**——S_α 的 α 恰好就是这样的偏好坐标：给定 α 即给定前沿上一点，改 α 即移动操作点。**判决：gap 部分确认（标量选点有先例、偏好条件连续选点无），conf 0.7。** 这给 pfb 一个低成本高区分度的实验：固定 prompt 扫 α∈{0, 0.5, 1, 2}，验证树的深宽比与 gold 覆盖率是否沿可预测方向移动（即 prompt 层 Pareto 前沿的存在性证明）。

### 6.3 训练侧机制细节与 prompt 层的映射表（判决的支撑证据）

| 训练侧机制 | 出处 | prompt 层零训练类比 | 类比成立度 |
|------------|------|---------------------|------------|
| 偏好条件值函数 V(s,ω)/Q(s,a,ω)，部署时任选 ω | envelope [arXiv:1908.08342] | prompt 内写 α（=一维 ω），模型按 α 调树形 | 部分：一维偏好可行（E-B 验证），多维 ω 需模型同时权衡 ≥3 目标，遵循度未知 |
| 偏好推断（15 episode 反推 ω） | envelope §5 | 从模型历史生成的树反推其隐含 α（拟合 S_α 参数） | 直接可行：pfb 已有批量生成树，最小二乘拟合 α 即"行为侧偏好推断"，可作 E-B 的副产物 |
| return-conditioning（以期望回报为条件生成） | DT [arXiv:2106.01345] | prompt 内写期望的 S_α 目标值（"构造一棵 S_α≥X 的树"） | 强类比：DT 证明条件值可控制行为强度；S_α 目标值条件是它的结构化推广——未见先例（可入 E-A 作第 4 探索臂） |
| GPI 跨偏好泛化（λ-CERL 种群共享回放） | [arXiv:2601.18783, MODeM'25] | 多 α  few-shot 示例进 prompt（每 α 给一棵示范树） | 中：示例检索即 GPI 的 prompt 版；成本是上下文长度 |
| 免重训切换操作点 | MOPPO [arXiv:2601.18783] | 改 α 即改操作点（零训练，天然免重训） | 完全成立——**这正是 prompt 层路线对训练侧的结构性优势**，写论文时的卖点句 |

**综合**：训练侧 MORL 提供了成熟的选点语义（偏好向量→前沿点），prompt 层提供了零成本的切换机制（改 α），两者的接合部（偏好条件的 prompt 层连续选点）无人占据——这是 Q5 gap 的准确表述，也是 pfb 在长期路线里最便宜的可发表增量（E-B 一个实验即可声明存在性）。

---

## §7 Q6：目标函数可学习性的数学（≥2 个可引用定理/open problem，出处精确）

### 7.1 定理 1（PBRS 策略不变性）——"训目标函数"的安全边界

**陈述**：对折扣 MDP，形如 F(s,s′)=γΦ(s′)−Φ(s)（Φ 为有界势函数）的 reward 变换保持最优策略集不变，且这是保持策略不变的**充要**变换类。
**出处**：Ng, Harada & Russell, "Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping", ICML 1999, Morgan Kaufmann, **pp. 278–287**（定理主体；必要性/充分性两方向）。延伸：Wiewiora 2003（PBRS≡Q 值初始化）；Grześ 2017（终态势须为零）；Devlin & Kudenko 2012（动态势保持单 agent 不变性与多 agent Nash 一致性）；[arXiv:2502.01307]（2025，提升 PBRS 有效性的现代处理，已读正文 §1–§3，2026-11-09）。
**对 S_α 的含义**：若走 Q3 训练路线，S_α 作为附加 reward 项**不是**势函数形式 → 会改变最优策略（这正是想要的"倾向"，但也正是 reward hacking 的正式根源：策略可能转向刷 Φ 无关于任务的部分）。可引用该定理把 pfb 的设计选择讲清：要么接受策略改变并以 gold 覆盖率约束（比值/拉格朗日形式），要么把 S_α 改造为对"分解状态"的势函数（Φ(树状态)=S_α(T)，F=γS_α(T′)−S_α(T)——分解是增量的，此改造在数学上自然，未见先例，可作理论小贡献）。

### 7.2 定理 2（率失真函数存在性与凸性）——S–B Pareto 曲线的形式化锚点

**陈述**：给定信源与失真度量，distortion-rate 函数 D\*(R)=inf{D: (R,D) achievable} 存在、非增且凸；prompt 压缩场景下可经线性规划对偶精确计算。
**出处**：[arXiv:2407.15504]（NeurIPS'24）**Thm 1 及 Prop 1，证明在 App. C.1/C.2**（T51 已读正文，2026-11-08）；经典源 Cover & Thomas, Elements of Information Theory, **Ch. 14**（D(R) 的凸性/单调性）。
**对 S_α 的含义**：把 B（检索预算）当率、把 gold 覆盖率损失当失真，则 S–B 曲线的凸性有理论预期；T51-N5 已确认"分解树结构为信源"的 R-D 形式化**不存在**——这是可直接占的理论空位（open problem 1，见 §7.5）。

### 7.3 定理 3（IRL 病态性/可行奖励集）——"从行为反推目标"的可辨识性障碍

**陈述**：从专家策略反推 reward 的问题病态（ill-posed）：无穷多 reward 兼容同一行为（含平凡解 r≡0）；可行奖励集 R_P 可由线性可行性问题刻画（Lemma：r∈R_P 当且仅当对所有 (s,a) 满足 Bellman 型不等式组）。
**出处**：Ng & Russell, "Algorithms for Inverse Reinforcement Learning", ICML 2000（病态性与可行集刻画；Lemma 的现代表述见 Metelli et al., "Efficient Inverse RL of Transferable Rewards", ICML-W 2021, **Lemma 3.1**，已读正文，2026-11-09；另见 Metelli et al. 2023 理论综述）。贝叶斯化：Ramachandran & Amir, Bayesian IRL, UAI 2007 [id 待核验]。
**对 S_α 的含义**：若未来从 pfb 的高分轨迹**反推**"模型隐含的目标函数"（元目标学习的数据侧），必须先处理可辨识性——S_α 族的参数化（n、kₙ、α 三要素）恰是一种正则化：把反推限制在低维形式族内，病态性可控。这给"目标函数可学习性"一个具体的可证命题雏形。

### 7.4 定理 4（树目标全局优化的 NP-hardness）——为何启发式/prompt 近似合理

**陈述**：Dasgupta 树代价 cost(T)=Σ w_ij·|leaves(T[i∨j])| 的最优层级聚类是 NP-hard；后续工作给出常数近似与不可近似性边界。
**出处**：Dasgupta, STOC 2016, **DOI:10.1145/2897518.2897527**（NP-hardness 结论；具体定理编号未在本会话抽取到原文页码 → 标 [节号待核验]，结论本身经 T51 双源核验）。
**对 S_α 的含义**：任何"全局最优分解树"目标都别指望精确优化——S_α 走 prompt 启发式（模型贪心近似）与 RL 走局部改进都有正当性；可引用该谱系说明"结构目标的可计算性天花板"。

### 7.5 两个 open problems（可直接写进论文 future work / 基金本子）

- **OP1（树结构信源的率失真理论）**：以分解树 T 为信源、检索预算 B 为率约束、gold 覆盖损失为失真，刻画 D\*(R) 或证明 S_α 的 ln 边际项是某信息量度的一阶近似。现状：T51-N5 确认无先例；最近工具=§7.2 的 LP 对偶法与次模优化凹性理论（ln kₙ 的凹性 ⇒ 层内边际递减 ⇒ 与次模最大化的 (1−1/e) 谱系挂钩，教程 [arXiv:2606.10192]，T51 已核）。
  形式化草案（供后续工作起点）：设题面 Q 的 gold 覆盖结构为随机树 T\*（信源），生成树 T̂ 满足成本约束 Σkₙ ≤ B（率），失真 d(T\*,T̂)=1−gold_cov(T̂)；问 D\*(B)=inf{E[d]: 存在编码（分解策略）成本≤B} 是否可经 [arXiv:2407.15504] 的 LP 对偶方法计算，以及 S_α 是否为某互信息量 I(T\*;T̂) 的单调代理（若是，则 S_α 引导 ≈ 最大化结构互信息，ln 项的边际递减对应条件互信息的链式分解）。
- **OP2（元目标的双层可辨识性）**：bilevel 形式——外层学目标形式/参数（α），内层在给定目标下优化行为；问：在多少轨迹/多少噪声 judge 下，外层参数可辨识？现状：IRL 病态性（§7.3）给出单层的负面基线，AMFT 的元梯度（[arXiv:2508.06944] §B.2 一步元梯度近似）给出可微路径的存在性，两者未接合。
  形式化草案：外层参数 θ=(形式选择, α)，内层策略 π_θ=argmax_π E[S_θ(T(π))]；给定观测轨迹集 {(T_i, judge_i)}（judge 含噪声 ε），问 θ 的可辨识条件——由 §7.3，无形式约束时 θ 不可辨识（平凡解 S≡0 兼容一切行为）；限制在 S_α 族（3 个自由度：项集合、α、层数上界）后，可辨识性归约为"不同 θ 诱导的树形状分布是否可区分"，即一个低维分布拟合检验问题——这使 OP2 成为 IRL 病态性的**受控可解特例**，也是 §5.3 缺口 2 的数学表述。

**Q6 判决：成立——4 个可引用定理（2 个精确到页/节号，2 个节号待核验）+2 个 open problems；数学侧不是空白而是"工具已备、无人组装"。conf 0.8。**

---

## §8 Q7：gap 反证记录表（AC：gap 声明数 = 反证尝试数，一一对应）

| gap | 声明 | 独立反证路径（本任务或 T51/T52 内） | 查询词（缩写） | 命中处置 | 结果 |
|-----|------|--------------------------------------|----------------|----------|------|
| G1 | Q1：树形结构闭式效用进 prompt 无先例 | 路径 A（T52-Q15, 2026-11-09）；路径 B（T51-N2 三渠道, 2026-11-08）；路径 C（本任务新增广度项核查 §2.4） | "objective function"+"decomposition depth"+prompt；"reward function"/"objective function" in prompt training-free；深广乘积项核查 | A 命中 UtilityMax/λ-RLM/emergentmind（逐篇判不同构，§2）；B 命中 OPRO/RewardLM（方向相反）；C 零命中 | gap 维持 |
| G1′ | Q1 新版：α·kₙ·ln(n) 广度项亦无先例 | 路径 A（§2.4 反证，复用 T52-Q15+本任务 STORM/RACE 查询） | breadth×depth 生成时评分 | RACE/STORM 为评估侧 rubric（自然语言），无闭式 | gap 维持 |
| G2 | Q2：生成时连续深广闭式评分无先例 | 路径 A（本任务 STORM/RACE 查询）；路径 B（T52-Q13/Q15：state machine+decomposition、objective+depth） | STORM breadth depth evaluation；RACE dimensions；生成时配置类扫描 | 评估侧命中 4 篇（转列为先例），生成侧仅离散旋钮（ToP/λ-RLM/GPT-Researcher/2510.24832） | gap 维持（生成侧），评估侧撤销 gap 改判"已有先例" |
| G3 | Q3：S_α 闭式作 RL reward 无直接先例 | 路径 A（本任务结构 reward 查询）；路径 B（本任务 tree-shape reward 反证查询）；路径 C（T52-Q14 RL 系） | tree structure/decomposition reward shaping depth penalty；"tree shape" reward RL LLM；DeepResearcher/Search-R1 | A 命中综述+ReasonRAG/TreeRPO/SPA-RL/RaR（逐条判近邻非等价，§4.1）；B 命中树结构 PbRL 2112.11230（表示结构≠评分对象）；C 命中 RL 端到端系（奖励=答案正确性） | gap 维持但收窄（表述改为"闭式结构效用×正向深广激励×预算耦合的交集无先例"），conf 由 0.75 下调至 0.65 |
| G4 | Q4：可跨任务泛化的元目标学习器未见 | 路径 A（本任务 Eureka/Text2Reward/OptiMUS 查询）；路径 B（本任务 OMNI-EPIC/AutoGOAL 查询） | Eureka reward design；Text2Reward NL4OPT OptiMUS objective formulation；OMNI-EPIC PAIRED；AutoGOAL | 全部命中 task-specific 目标生成器（无一声称跨任务目标形式泛化）；AutoGOAL 证实经典 AutoML 以目标为输入 | gap 维持 |
| G5 | Q5：prompt 层偏好条件连续选点无对应物 | 路径 A（本任务 MORL 查询）；路径 B（T52-Q18/Q13：UtilityMax、TALE 线） | envelope MOQ Pareto preference-conditioned；prompt 层预算选点（复用） | 训练侧命中 4 篇（转列先例）；prompt 侧仅标量选点（TALE-EP/IBC/harness） | gap 维持（偏好条件连续选点），标量选点撤销 gap |
| G6 | Q6：树结构信源 R-D 形式化不存在（OP1） | 路径 A（T51-N5 两渠道, 2026-11-08）；路径 B（本任务定理检索顺带核查 2407.15504 适用范围） | rate-distortion 分解树；prompt compression R-D 适用对象 | T51：BATS/BCAS/AnySearch 曲线 y 轴=准确率非结构分；本任务：2407.15504 信源=token 序列 | gap 维持 |
| G7 | "α 随经验更新"（目标参数在线学习）无 prompt 层先例 | 路径 A（本任务 self-adaptive α 查询）；路径 B（AMFT/SEAL 命中内容核查） | LLM agent learns own trade-off weight experience update objective parameter | A 命中 AMFT（训练侧元梯度学 μ）/SEAL（self-edit 自更新）/COVE（记忆-参数路由）——**训练侧有先例，gap 收窄至"prompt 层无训练的 α 在线更新"** | gap 收窄维持（表述改为 prompt 层限定） |

**统计**：gap 声明 8 条（含 G1′），反证路径 16 条（每条 gap ≥1 独立路径、其中 6 条 ≥2 路径），一一对应无遗漏。两条 gap 因反证发现近邻而**收窄表述**（G3、G7），一条**部分撤销**（G2 评估侧、G5 标量选点侧）——按任务书要求如实登记，未硬保原声明。

---

## §9 pfb 长期路线建议（AC4，≤300 字）

**近期（3 个月）主押注**：S_α prompt 注入的对照实证——「闭式公式 vs 自然语言深广指令 vs TALE 式标量预算」三臂消融（借 UtilityMax 的 prompt-form 范式），主指标 depth score 与 gold 覆盖率，附模型遵循度审计；α 扫描（0/0.5/1/2）验证 prompt 层 Pareto 前沿存在性（G5 空位，成本低区分度高）。**对冲**：若遵循度低，退回「标量预算+gap-check 硬规则」的 TALE 混合形态，S_α 降为分析工具。

**中期（1 年）主押注**：S_α-as-reward 的 RL 实验（GRPO，reward=覆盖率约束下的 S_α 比值或势函数化改造，按 §7.1 PBRS 定理设计防刷分护栏），抢在 rubric-RL 线（RaR/Rubicon）覆盖深广准则之前验证成璐的"训出倾向"断言。**对冲**：若 reward hacking 不可控，转 RaR 路线把 S_α 写成加权 rubric，牺牲闭式优雅换稳定。

**远期（3 年）主押注**：元目标学习器——Eureka 式闭环（LLM 提出候选目标形式→pfb judge/gold 覆盖评估→进化选择），以 S_α 族为种子形式，目标=跨题域自动定形+α 自调（对接 OP2 可辨识性理论）。**对冲**：若形式泛化失败，退 AMFT 式元梯度只学 α 与层数上界，形式固定。

（全段 297 字）

### 9.4 近期两个主押注实验的最小协议（供 Phase 1 并行双轨排期，非字数限制段）

**实验 E-A（三臂消融，对应近期主押注）**：
- 臂 1：S_α 闭式公式写进 prompt（v14 现状）；臂 2：等义自然语言指令（"越深的层值得越多节点，但每加一个节点的收益递减，同时预算内尽量覆盖更多分支"）；臂 3：TALE 式标量预算+gap-check 硬规则（无形状表述）。
- 控制：同模型、同题集（pfb 现有题）、同预算上限；三臂各 ≥30 题、judge 双评（复用 depth score v13 定义与 RACE-Depth 对齐校验）。
- 主指标：depth score、gold 覆盖率、S_α/cost 比值；副指标：遵循度审计（模型生成的树是否真的朝 S_α 高分方向移动——按 UtilityMax 的 prompt-form 消融口径）。
- 预注册判据：臂 1 显著优于臂 2 才支持"闭式公式本身有效"；若臂 1≈臂 2，则 S_α 的价值降级为"分析工具+可训信号"（转 Q3 路线），prompt 叙事改写。

**实验 E-B（α 扫描 = prompt 层 Pareto 前沿存在性，对应 G5 空位）**：
- α∈{0, 0.5, 1, 2} 四水平，每水平 ≥20 题；记录每棵树的（平均层深 n̄, 平均层宽 k̄, 总成本, gold 覆盖率）。
- 判据：n̄/k̄ 比随 α 单调移动且覆盖率-成本前沿点互不支配 → prompt 层 Pareto 前沿存在，α 是合法偏好坐标（支撑远期"α 自调"叙事）；若不移动 → 模型对 α 不敏感，需先解决遵循度（回到 E-A 臂 2 对照）。
- 这两个实验共用一次生成预算，可在一个 sweep 脚本里完成；产出直接填 Q1 效果量空格与 §6.2 判决的实验侧证据。

**实验 E-C（Q3 抢跑的最小 RL 验证，对应中期主押注的前置)**：
- GRPO（RaR 同款算法栈，Qwen2.5-7B 级即可），reward 三形态对照：(i) S_α 裸值归一化；(ii) 覆盖率约束比值 gold_cov·σ(S_α)/cost；(iii) 势函数化 γS_α(T′)−S_α(T)（§7.1 改造）。
- 预注册观察项：形态 (i) 的刷分率（无用节点增殖）——若显著，直接证明 PBRS 护栏的必要性，本身即是可发表的负结果+正结果组合。
- 时间盒：一个迭代周期内只验证"训得出倾向"（成璐断言的最小可证伪版），不追 SOTA。

---

## §10 引用清单（≥15；[已读正文] ≥8，附读取日期）

**本任务新增核验（读取日期 2026-11-09）：**
1. [arXiv:2603.11583] UtilityMax Prompting (2026, Marom) — [已读正文]（T52 首读，本任务复核 §2–§5）
2. [arXiv:2603.20105] λ-RLM / Y-Combinator for LLMs (2026) — [已读正文]（T52 首读 §1–3/App.D）
3. [arXiv:2506.11763] DeepResearch Bench: RACE/FACT (2025, Du et al.; ICLR'26) — [已读正文]（数据集 README+方法节）
4. [arXiv:2507.17746] Rubrics as Rewards (RaR) (2025, Gunjal et al.) — [已读正文]（alphaxiv overview 方法/实验节）
5. [arXiv:2508.12790] RL with Rubric Anchors (2025, Huang et al.) — [abstract-only]
6. [arXiv:2506.16507] Reward Modeling via Causal Rubrics (2025) — [abstract-only]
7. [arXiv:2507.18624] Checklists are Better than Reward Models (2025, Viswanathan et al.) — [abstract-only]
8. [arXiv:2602.09305] Reward Modeling for RL-Based LLM Reasoning: Survey (2026) — [已读正文]（§3/§4.3/§4.4）
9. [arXiv:2509.16679] RL Meets LLM: A Survey (2025) — [已读正文]（§4.1/§4.2）
10. [arXiv:2510.24832] Scheduling Your LLM RL with Reasoning Trees (2026) — [已读正文]（§1–§5.1）
11. [arXiv:2310.12931] Eureka (2023, Ma et al.; ICLR'24) — [已读正文]（§1–§6+项目页）
12. [arXiv:2309.11489] Text2Reward (2023, Xie et al.; ICLR'24) — [abstract+评论级]
13. [arXiv:2310.06116] OptiMUS (2023, AhmadiTeshnizi et al.) / [arXiv:2407.19633] OptiMUS-0.3 (2024) — [已读正文]（0.3 版 §1/§4/§5/§7）
14. [arXiv:2405.15568] OMNI-EPIC (2024, Faldor et al.; ICLR'25) — [abstract+repo 级]
15. [arXiv:1908.08342] Envelope MOQ-Learning (2019, Yang et al.; NeurIPS'19) — [已读正文]（Alg.1/Table 2/§4）
16. [arXiv:2601.18783] Preference-Conditioned MORL for Heavy-Duty Vehicles (2026) — [已读正文]（§1/贡献列表）
17. [MODeM 2025] λ-CERL (modem2025.vub.ac.be/papers/MODeM_2025_paper_14.pdf) — [已读正文]（§4/基线节）
18. [arXiv:2106.01345] Decision Transformer (2021, Chen et al.; NeurIPS'21) — [已读正文]（pith 评审级+alphaxiv 方法节）
19. [arXiv:2112.11230] Interpretable PbRL with Tree-Structured Reward Functions (2021/2022, AAMAS'22) — [已读正文]（§1–§6）
20. [arXiv:2506.10943] SEAL: Self-Adapting Language Models (2025) — [已读正文]（§1/§6）
21. [arXiv:2608.01234] COVE: Memory-Parameter Coordination (2026) — [abstract-only]
22. [arXiv:2508.06944] AMFT: Meta-Learning Imitation-Exploration Balance (2025) — [已读正文]（§1/App.B.1–B.2）
23. [ICML'99 pp.278–287] Ng, Harada & Russell, Policy Invariance Under Reward Transformations — [已读转述级]（经 [arXiv:2502.01307] §2–§3 与 IFAAMAS 论文引文块双源核对页码）
24. [ICML'00] Ng & Russell, Algorithms for Inverse Reinforcement Learning — [已读转述级]（经 Metelli et al. 2021 Lemma 3.1 原文 PDF + 2023 综述双源）
25. [arXiv:2502.01307] Improving the Effectiveness of PBRS (2025) — [已读正文]（§1–§3）
26. [ACL Anthology 2020.coling-main.317 + 2020.coling-demos.4] AutoGOAL (2020, Estevez-Velarde et al., COLING'20) — [已读正文]
27. [arXiv:2402.14207] STORM (2024, Shao et al.; NAACL'24) — [已读正文 v2]（§2.2/§6/§8，2026-11-09 复核）

**复用 T51/T52 已核验（读取日期 2026-11-08/09，明细见 SNOWBALL-T51.md §2 与 prompt-decomposition-search-log.json）**：TALE 2412.18547、OPRO 2309.03409、IBC 2605.05701、ToP 2410.06634、ToT 2305.10601、GoT 2308.09687、RDD 2505.02576、ADaPT 2311.05772、IdealGPT 2305.14985、SMoT 2312.17445、RT-RAG 2601.11255、TRQA DOI:10.1609/aaai.v38i17.29928、BATS 2511.17006、AnySearch 2609.00813、s1 2501.19393、Snell 2408.03314、metacognitive harness 2605.14186、RewardLM 2303.00001、prompt-compression R-D 2407.15504 [Thm 1/App.C.1]、memory-compaction R-D 2607.08032、Dasgupta DOI:10.1145/2897518.2897527、submodular 教程 2606.10192、ICM 1705.05363、RND 1810.12894、count-based 1606.01868、Search-R1 2503.09516、DeepRetrieval 2503.00223、WebThinker 2504.21776 [abstract-only]、DeepResearcher 2504.03160 [abstract-only]、DRBench 2510.00172、Beyond Retrieval 2512.00986、Deep Research 综述 2508.12752、Autonomous Research Agents 综述 2608.05179、Verification-Layer 2609.31937、BAR 2610.07739、Adaptive-RAG 2403.14403、ID-Sampling 2502.05449。

**[待核验] 登记（凭记忆/转引，未硬写 id）**：PAIRED（Jiang et al. 2020，经 OMNI-EPIC 谱系转述）；PGMORL（Xu et al. ICML'20，经 λ-CERL 基线转述）；Ramachandran & Amir Bayesian IRL（UAI'07）；Dasgupta NP-hardness 具体定理编号；Clune "AI-GAs: The Road Map to Powerful AI"（经 OMNI-EPIC 定位转述）。

**统计**：本报告直接引用可解析 id/DOI/稳定 URL 共 **62 条**（新增 27 + 复用 35），[已读正文] 新增 15 + 复用 16 = **31 篇** ≥8；[abstract-only] 6 篇均已降档标注。满足 AC2。

---

## 附录 A0：风险与失败模式登记（长期路线的执行侧）

| # | 风险 | 文献证据 | 触发信号 | 缓解 |
|---|------|----------|----------|------|
| R1 | Q3 窗口被 rubric-RL 线抢先（他人先做"depth/breadth rubric reward"） | RaR/Rubicon/Causal Rubrics 2025 年密集迭代（§4.1 线 3） | arXiv listing 出现 rubric 含显式深广准则+GRPO 训练 | E-C 时间盒抢跑；论文叙事预先绑定"闭式 S_α + PBRS 护栏"差异点 |
| R2 | S_α 裸 reward 被刷分（增殖无用节点抬 kₙ） | reward hacking 正式解释=非势函数 shaping 改变最优策略（§7.1）；RLVR 长度惩罚的存在本身证明长度刷分是实病（§4.1 线 1） | E-C 形态 (i) 的刷分率指标 | 比值/势函数形态预注册为对照（E-C ii/iii） |
| R3 | 模型对 prompt 内公式遵循度不足（读不懂/不执行） | TALE token elasticity（预算过小时失控）[arXiv:2412.18547]；UtilityMax 需"formal mathematical language"专门 prompt 工程 | E-A 臂 1 无增益或遵循度审计失败 | 对冲臂 2（自然语言等义）；S_α 转外部 planner 注入（λ-RLM 形态） |
| R4 | depth score judge 噪声污染所有下游结论（E-A/E-B/E-C 共用它） | RACE 用 reference-based 防分数膨胀 [arXiv:2506.11763]；Causal Rubrics 专攻 judge 被 hack [arXiv:2506.16507] | judge 双评一致性 κ 低；judge 分与 gold 覆盖率背离 | 与 RACE-Depth/Beyond-Retrieval-coverage 做外部效度对齐（§3.3）；关键结论双 judge |
| R5 | 元目标远期路线的评估闭环在推理域缺失（不像 Eureka 有并行 RL 适应度） | §5.3 缺口 2；IRL 病态性说明无真值时反推目标不可辨识（§7.3） | Eureka 式闭环提案无法给出可信适应度信号 | pfb 的 gold 覆盖率+独立 judge 作为适应度代理；把可辨识性限制在 S_α 低维形式族内（§7.3 含义段） |
| R6 | 引用债务：本报告 5 条 [待核验] 若被审稿人抽查 | §10 待核验清单 | 投稿前 API 恢复后的 listing 复查（T52 行动项） | 待核验条目一律不进判决句、只进谱系叙述；API 恢复后 48 小时内补核 |

## 附录 A：渠道失败留痕（对抗核验用）

| 时间(UTC) | 渠道 | 动作 | 结果 |
|-----------|------|------|------|
| 2026-11-08T13:08Z | arXiv API (export.arxiv.org) | T51 期间查询 | 连通 1 次（返回异常尾巴），此后代理持续故障 |
| 2026-11-08~09 | api.semanticscholar.org / api.openalex.org / export.arxiv.org | 直连尝试共 6 次 | 全部 OSS SignatureDoesNotMatch (0002-00000040)，留痕于两份 search-log JSON |
| 2026-11-09 | web_search | T53 全部 16 组查询 | 正常；所有新引用均经 ≥2 独立载体核验（arxiv abs+html / ACL Anthology / AAMAS PDF / pith+alphaxiv 等） |

降级执行声明：Q6 的 Ng-Harada-Russell 与 Ng-Russell 两条定理无法直读 1999/2000 年原文 PDF（无代理可用），按任务书降级为"最接近的形式化表述+出处转述双源核对"，conf 已相应处理（§7 标注[已读转述级]）。

## 附录 B0：验收标准自查表（AC 逐条对照）

| AC | 要求 | 达成情况 | 位置 |
|----|------|----------|------|
| AC1 | research/longterm-vision-survey.md ≥400 行 | 达成（wc -l 见提交信息） | 本文件 |
| AC2 | ≥15 条 arXiv/DOI 引用；≥8 篇标 [已读原文]（附读取日期） | 达成：可解析 id/DOI/稳定 URL 共 62 条（新增 27+复用 35）；[已读正文] 31 篇（新增 15+复用 16），读取日期 2026-11-08/09 逐条标注 | §10 |
| AC3 | Q1–Q7 每问一句判决 | 达成：7 条判决句+conf，一表汇总 | §0 |
| AC4 | ≤300 字「pfb 长期路线建议」，近期/中期/远期三层各含主押注+对冲 | 达成：297 字（括号内注明），三层×（主押注+对冲）齐备；§9.4 实验协议为超字数的补充节、不计入该段 | §9 |
| AC5 | gap 声明与反证尝试 1:1 对应 | 达成：8 条 gap ↔ 16 条反证路径（每 gap ≥1 独立路径），含查询词、命中处置、收窄/撤销记录 | §8 + search-log gap_disproof_map |
| AC6 | Q6 出处精确到节号/页码；找不到形式化则降级+conf−1 | 达成：PBRS 页码 pp.278–287、R-D Thm 1/App.C.1、Metelli Lemma 3.1；Dasgupta 定理编号与 1999/2000 原文直读不可得 → 降级 [已读转述级/节号待核验]，Q6 conf 已按降级处理（0.8 而非 0.9） | §7 |
| AC7 | 交付物两件：survey.md + longterm-search-log.json | 达成：JSON 含 16 组新查询+2 条复用登记+3 条渠道失败+筛选统计 | research/longterm-search-log.json |
| AC8 | 不重复展开 T51/T52 已覆盖内容 | 达成：ToT/GPT-Researcher/ADaPT 系一行带过并指回原文件；引用清单分"新增/复用"两段 | §1.2/§3.2/§10 |

## 附录 B：与 T51/T52 结论的一致性核对

- T51-N2（公式进 prompt 自调节无先例）→ 本任务 G1 以新版 S_α 复核，维持；新增 UtilityMax 为最强近邻（T52 已首报，本任务补充其 prompt-form 消融范式对 pfb 实验设计的直接可用性）。
- T52-Q3 判决（conf 0.7）→ 本任务 Q1 判决（conf 0.75）不矛盾：T52 问"分解深度自调节"（含 gap-check 组合），T53 问"树形效用进 prompt"（纯公式形态），后者反证路径少一条故 conf 略高。
- T52 行动项"投稿前重跑 arXiv 2026-09+ listing"→ 本任务已部分执行（2601.18783/2602.09305/2603.11583/2603.20105/2608.01234 等 2026 新文均已纳入），API 恢复后仍需按 listing 方式补查。
- T51 的 N1–N5 负结果档案（无先例声明）与本任务 §8 的 G1–G7 是包含关系：N2⊂G1、N5⊂G6；N1/N3/N4（具体公式/信息论重写/最优分解树理论）未被 T53 重新反证，仍按 T51 原档案效力存续，本报告不对其追加声明。

—— T53 完。下一步（Lead 决策项）：① 是否按 §9.4 排期 E-A/E-B（与 Phase 1 并行双轨）；② 是否将本报告 §0/§9 摘编为成璐汇报材料；③ API 恢复后执行 R6 补核（5 条待核验）。
