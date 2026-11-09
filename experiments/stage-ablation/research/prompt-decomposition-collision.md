# T52 · Prompt 层逐层分解 → 推理深度：滚雪球撞车调研

> origin: arena agent (T52) · 2026-11-09 · 任务书：tasks/T52-prompt-decomposition-collision.md（sigma-nlnk-snowball @ 2f3bc174）
> 姊妹任务：T51（S_α 公式先例）→ research/objective-function-priorart/SNOWBALL-T51.md。本报告聚焦**机制层**：
> 「prompt 层逐层/递归分解提升 LLM 推理深度」是否被系统研究过，以及 S5 pipeline 三个创新点 (a)迭代加深 (b)逐节点检索验证 (c)显式目标函数 S_α 各自的先例状况。
> 检索日志（全部查询组+命中+筛选）：research/prompt-decomposition-search-log.json

---

## §0 结论速览（三个核心问题判决句）

**Q1「迭代加深分解」（允许返回上一层重新拆）——判决：有先例，机制级撞车成立，但形态不同（conf 0.85）。**
ADaPT [arXiv:2311.05772] 的"执行失败→递归再分解"、IdealGPT [arXiv:2305.14985] 的"置信不足→触发新一轮子问题分解"、RT-RAG [arXiv:2601.11255] 的"检索失败→重述并重复分解-检索"、RDD [arXiv:2505.02576] 的"递归 split-solve-merge 直到原子可解"均已实现"分解不是一次性的、可回到分解层加深"这一机制；SMoT [arXiv:2312.17445] 与 λ-RLM [arXiv:2603.20105] 进一步把它做成显式状态机/受限运行时。**S5 的差异化空间不在"可返回 P1"本身，而在触发信号（P1.5 gap check + S_α 边际收益判据）与研究型 pipeline（分解→逐节点验证→综合）的组合**——该组合未见先例（conf 0.75）。

**Q2「逐节点独立检索验证」（非整体上下文）——判决：两个子机制各有成熟先例，三合一组合无先例（conf 0.8）。**
按子问题/节点独立检索是 multi-hop QA 标配：Self-Ask [arXiv:2210.03350]、TRQA [DOI:10.1609/aaai.v38i17.29928]、RT-RAG、QD-RAG [arXiv:2507.00355]、Decompositional Graph Retrieval [arXiv:2506.13380]；按 claim/节点独立核验是 FActScore 谱系标配：ClaimDecomp [arXiv:2403.11903]、ClaimVer [DOI:10.18653/v1/2024.findings-emnlp.795]、以及分层验证架构 [arXiv:2609.31937]。**"节点级检索 + 节点级验证 + source tagging(given/knowledge/search) 预算记账"三位一体未见先例**；最近邻 BAR [arXiv:2610.07739] 有预算内 plan-navigate-verify 与 provenance，但挂在 KG 边上且失败触发修订而非降级。

**Q3「显式目标函数驱动分解深度」（告诉模型 S_α 让它自调节）——判决：无完整先例，T51 结论在更宽检索面下仍成立，但出现两个必须引用的近邻（conf 0.7）。**
UtilityMax [arXiv:2603.11583]（2026-03）首次系统论证"把形式化数学效用函数写进 prompt、令 LLM 显式对目标各分量推理"优于自然语言指令——但其效用作用于**任务输出分布**（推荐精度），不作用于分解树结构；TALE [arXiv:2412.18547] 注入的是**标量 token 预算**；λ-RLM 的 (k\*, τ\*, d) 结构参数由**外部 planner** 设定而非模型读公式自调。**「S_α=Σ[n·ln(kₙ)] 全文进 prompt、模型自行权衡树的深/宽/验证投入」未找到任何先例**（与 T51 §4-N2 一致，本任务用不同关键词组复核后维持）。

**总判定：S5 作为整体 pipeline 无撞车（无一篇同时覆盖 迭代加深+逐节点验证+目标函数自调节）；三个组件中 Q1 机制已有强先例、Q2 子机制已有强先例、Q3 无先例。论文叙事必须放弃"首个迭代分解/首个逐节点验证"类声明，把贡献收窄到：(i) S_α 目标函数的 prompt 注入与自调节（Q3，方法贡献）；(ii) 三组件在研究型 pipeline 中的集成与**组件级贡献测量**（呼应支柱 A：depth score v8→v13 0.354→0.487 的纯 prompt 增益 + 分解贡献消融）。**

---

## §1 调研方法、渠道与限制

### 1.1 四象限执行映射（任务书关键词组 → 实际执行）

| 象限 | 任务书关键词组 | 执行情况 | 主要收获 |
|------|----------------|----------|----------|
| 权威 | hierarchical decomposition + LLM reasoning | ✅ 2 组查询 | RDoLT(JAIR/arXiv:2501.02026)、HyperTree Planning(arXiv:2505.02322)、SHIELD(仅二次引用→降级) |
| 权威 | question decomposition + multi-hop | ✅（复用 T51 + 本任务 1 组） | TRQA、RT-RAG、QD-RAG、Self-Ask、IRCoT |
| 权威 | tree of thoughts | ✅（T51 已核验 2305.10601） | ToT/GoT 谱系 |
| 权威 | recursive problem solving + LM | ✅ 1 组 | RDD(2505.02576)、RLM(工程 repo)、递归分解综述(emergentmind, 二次) |
| 权威 | iterative refinement + reasoning depth | ✅ 2 组 | Self-Refine(2303.17651)、Reflexion(2303.11366)、ID-Sampling(2502.05449) |
| 小众 | decomposition-guided retrieval | ✅ 1 组精确短语 | QD-RAG(2507.00355)、Decomp-GraphRetrieval(2506.13380) |
| 小众 | node-level verification + LLM | ✅ 1 组 | M-ER(2610.39667, KBQA 节点打分)、2609.31937、ClaimVer 线 |
| 小众 | progressive deepening + prompt | ✅ 1 组（并入 iterative deepening） | ID-Sampling（术语撞名，判定无关但必须区分） |
| 小众 | iterative decomposition + state machine + LLM | ✅ 1 组 | SMoT(2312.17445)、Scheduler-Theoretic 综述(2604.11378)、SHIELDA(2508.07935) |
| 最近轨迹 | deep research agent + decomposition (2026-06~11) | ✅ 2 组 | Autonomous Research Agents 综述(2608.05179)、Beyond Retrieval(2512.00986)、DRBench(2510.00172)、Step-DeepResearch(2512.20491) |
| 最近轨迹 | research pipeline + ablation + stage | ✅ 1 组 | DeepResearch Bench(ICLR'26, RACE/FACT)、Beyond Retrieval（planning 模块量化：coverage/redundancy/correctness vs 专家计划） |
| 过去轨迹 | Self-Refine / Reflexion / L2M / ToT / GoT / plan-and-solve | ✅ 全部核验 | 见 §5 总表（2023–2024 谱系完整覆盖） |

### 1.2 低垂果实精确短语检查（任务书表格逐项回答）

| 短语 | 命中结果 | 判定 |
|------|---------|------|
| "iterative deepening" AND "LLM" AND "decomposition" | ID-Sampling [arXiv:2502.05449]（iterative deepening **采样预算**+自反思触发，非分解树）；IdealGPT（iteratively decomposes，未用该术语） | 术语被采样调度占用；分解语义的迭代加深以 ADaPT/IdealGPT/RT-RAG 为代表，不用这个词 |
| "per-node" AND "retrieval" AND "verification" AND "LLM" | M-ER [arXiv:2610.39667]（KBQA 子图节点级 MCTS 打分）；无"每节点独立检索+独立验证"的完整命中 | 子机制各自存在（§0-Q2），组合短语零直接命中 |
| "objective function" AND "decomposition depth" AND "prompt" | UtilityMax [arXiv:2603.11583]（形式效用进 prompt，不涉分解深度）；λ-RLM [arXiv:2603.20105]（深度界 d 为外部结构参数）；emergentmind TODO 分解主题页（含 E₀≤b^D·ε_D 深度-分支-误差关系式，二次来源） | **无"S_α 类公式驱动模型自调分解深度"命中** |
| "state machine" AND "decomposition" AND "language model" AND "reasoning" | SMoT [arXiv:2312.17445]（状态=子问题、转移=依赖，双 agent PlAgt/ActAgt）；Scheduler-Theoretic [arXiv:2604.11378]（FSM/图执行分类学）；SHIELDA [arXiv:2508.07935]（36 类异常分类+升级控制器） | 状态机×分解架构已有先例，但均无检索预算与目标函数 |
| "source tagging" AND "knowledge" AND "search" AND "LLM pipeline" | 仅工程实践（Databricks/Neo4j provenance tagging、grasp.study 四标签 [int]/[url]/[data]/[assumption]+载重假设占比门槛）；学术侧最近邻为 Adaptive-RAG（问题级三路由）与 BAR（KG 边级 provenance） | **学术文献无 given/knowledge/search 节点级三源 tagging 先例**（与 T51 §4-N4 一致） |

### 1.3 渠道与"读原文"口径（失败降级声明）

- 主渠道：web_search（索引覆盖 arxiv.org/html 全文页、arxiv.org/abs、AAAI OJS、ACL Anthology、ICLR proceedings、Semantic Scholar、dblp、pith.science 评审记录、GitHub 一手 repo）。
- **arXiv API / Semantic Scholar API / OpenAlex 直连在本会话全部被沙箱 fetch 代理拦截（OSS SignatureDoesNotMatch，错误码 0002-00000040，共尝试 5 次，全部留痕于 search-log.json 的 channel_failures 字段）**。任务书降级路径"ego-browser 访问 arxiv.org"不可用（无浏览器工具），故按"换同义词再试一轮 + 多查询式交叉"补偿：同一论文均用 ≥2 个独立查询式/独立载体核验 id。
- 「读了原文」口径：凡检索抽取覆盖到论文**正文方法/实验/消融章节**（非仅 abstract）者标记 [已读正文]；仅 abstract/摘要级信息者标记 [abstract-only] 并按任务书降一档 conf。本调研 [已读正文] 共 **21 篇**（清单见 §9），远超 ≥8 底线。
- 关键词零结果时的同义词替换已执行："hierarchical"→"recursive/layered/multi-level"（§1.1 权威象限第 4 组）；"progressive deepening"→"iterative deepening"（§1.2 第 3 行）；"source tagging"→"provenance tagging"（§1.2 第 5 行）。

---

## §2 机制问题 1：这种 pipeline 被系统研究过吗？效果量与生效条件

**判决：是，已被系统研究（2022 起谱系完整，2025–2026 出现模块化定量评测），但"分解本身贡献多少分"的消融仍是稀缺品——这正是 pfb 支柱 A 的空位。**

### 2.1 效果量汇总表（只收可归因到"分解/迭代"机制的数字）

| 工作 | 任务域 | 效果量（对照） | 分解贡献是否被单独量化 | 来源 |
|------|--------|----------------|------------------------|------|
| Least-to-Most [arXiv:2205.10625] | SCAN/算术/GSM8K | SCAN 组合泛化 16%→**99.7%**；GSM8K 随步数增加超越 CoT | 否（端到端） | [已读正文] |
| ToT [arXiv:2305.10601] | Game of 24 | CoT 4%→**74%** | 否（搜索整体） | [已读正文] |
| GoT [arXiv:2308.09687] | 排序/集合运算 | 排序质量比 ToT **+62%**、成本 **−31%** | 否 | [已读正文] |
| Plan-and-Solve [arXiv:2305.04091] | 10 个数学/常识/符号数据集 | 零样本超 Zero-shot-CoT，可比 8-shot CoT | 否（PS vs PS+ 消融触及变量抽取） | [已读正文] |
| Self-Refine [arXiv:2303.17651] | 7 任务 | 平均 **~20% 绝对提升**；**数学推理无外部信号时增益≈0**（94% 案例自评"没问题"） | 部分（按任务分解增益） | [已读正文] |
| Reflexion [arXiv:2303.11366] | HumanEval/ALFWorld | pass@1 80%→**91%** | 否（反思循环整体） | [已读正文] |
| ADaPT [arXiv:2311.05772] | ALFWorld/WebShop/TextCraft | 成功率 **+28.3 / +27 / +33 pt**；消融证明多级分解必要、随执行器能力自适应 | **部分（多级 vs 单级分解消融）** | [已读正文] |
| IdealGPT [arXiv:2305.14985] | VL 推理 | 迭代分解 vs 单轮分解消融（Table 3）：迭代至置信显著更优 | **是（迭代次数消融）** | [已读正文] |
| RDD [arXiv:2505.02576] | 数学/符号/常识 | 给出**转变点定理**：仅当子问题单元准确率高于根问题时分解才有效；token 更少、更快 | **是（理论+难度分箱）** | [已读正文(评审级)] |
| STORM [arXiv:2402.14207] | 长文写作 | 组织性 **+25%**、覆盖广度 **+10%**（vs outline-driven RAG 基线） | 部分（question-asking 机制消融） | [已读正文] |
| RT-RAG [arXiv:2601.11255] | multi-hop QA | 树深 2→3：MuSiQue F1 **+1.9**；深 4 饱和 | **是（树深消融）** | [已读正文] |
| Dissecting Agentic RAG [arXiv:2606.21553] | HotpotQA(本地 Qwen2.5-7B) | 去掉 query decomposition：**−1.4 EM**；2 轮检索捕获 5 轮 **95%** 增益 | **是（组件消融，最接近 pfb 支柱 A 方法）** | [已读正文] |
| BATS [arXiv:2511.17006] | 开放域搜索 agent | 准确率 +12.8% 同时 search 调用 **−40.4%**、总成本 −31.3% | 部分（Budget Tracker/规划/验证模块消融） | [已读正文] |
| Tree of Problems [arXiv:2410.06634] | 列表排序等 | (b,d) 参数化树 vs L2M/CoT-SC 全面胜出；调用数=节点数 | 部分（b×d 网格） | [已读正文] |
| λ-RLM [arXiv:2603.20105] | 长上下文任务 | 递归深度/调用数/成本成为输入大小的**显式函数**（可分析运行时） | 是（成本模型） | [已读正文] |
| UtilityMax [arXiv:2603.11583] | MovieLens 多目标推荐 | 形式效用 prompt vs 自然语言 prompt：precision/NDCG 一致提升（3 个前沿模型） | 是（prompt 形式消融） | [已读正文] |
| SHIELD（仅二次引用） | StrategyQA | 77.8% vs CoT 69.1%（+8.7pt） | 不详 | [abstract-only，经 BJMS 综述转引；**conf 降档，未计入判定依据**] |

### 2.2 生效/失效条件（跨工作归纳，论文讨论节可直接引用）

1. **难度阈值/转变点**：RDD 证明分解只在"子问题准确率 > 根问题准确率"区间有效——太简单白付分解成本，太难子问题同样失败。
2. **无外部信号时自我迭代失效**：Self-Refine 在数学推理上增益≈0（模型找不到自己的推理错误）；ID-Sampling 同样发现"模型能自纠但不能自判何时纠"。→ **S5 的 P1.5 gap check 与 S_α 正是外部化的"何时再拆"信号，此文献线是它的动机证据。**
3. **深度饱和**：RT-RAG depth 4 无增益；Dissecting 2 轮≈5 轮 95%；s1 budget forcing 6 次后压平。→ 支持 S_α 的 ln 边际递减设计（横向铺量有饱和点）是有文献共鸣的。
4. **分解会碎片化预算并传播首错**：Verification-Layer [arXiv:2609.31937] 实测"加入 planning 在已有 verification 时反而降分"；BJMS 综述引 SHIELD 的层间一致性纠错。→ S5 逐节点验证需报告错误传播分析。
5. **执行器能力耦合**：ADaPT 的分解深度随执行 LLM 能力自适应——prompt 层分解的收益是模型能力的函数（pfb 用 qwen 本地模型的实测应放在这个坐标系里报告）。

### 2.3 S5 相位 × 文献坐标系（一图定位）

| S5 相位 | 功能 | 文献中最接近的机制族 | 文献中最接近的量化证据 | S5 独占点 |
|---------|------|----------------------|------------------------|-----------|
| P1 | 逐层分解（L1 正交因子 → L2 定义展开 → L3 可计算项）+ source tagging | 递归分解族（L2M/DecomP/RDD/ToP/λ-RLM）；研究树族（RT-RAG/TRQA/GPT Researcher） | L2M SCAN 99.7%；ToP b×d 网格；λ-RLM 成本解析式 | 三源节点标注（given/knowledge/search）+ knowledge 节点断言纪律（须含数值/公式） |
| P1.5 | gap check → 决定是否返回 P1 加深 | as-needed 再分解族（ADaPT/IdealGPT）；迭代 refinement 族（Self-Refine/RT-RAG 环路） | ADaPT +28.3/+27/+33pt；IdealGPT 迭代消融；RDD 转变点定理 | 触发信号=结构化信息缺口核查+Δ=ln((kₙ+1)/kₙ) 边际判据（非失败/置信/满意度） |
| P2/P3 | 逐节点检索 + 逐节点验证（预算 B 记账） | 子问题检索族（Self-Ask/IRCoT/QD-RAG/RT-RAG）；claim 核验族（FActScore/ClaimVer）；预算验证族（BATS/IBC/BAR/2609.31937） | BATS −40.4% 调用；Dissecting 去分解 −1.4 EM；2609.31937 gate/judge 成本分离 | 检索与验证对齐在同一棵分解树节点上 + 预算耗尽节点级 [待核验] 降级 |
| P4 | 综合成文 | 报告生成族（STORM/WebThinker/Step-DeepResearch/DeepResearch Bench 评测线） | STORM +25%/+10%；DRBench 三维评分 | 无独占点（不主张贡献） |
| 贯穿 | S_α 目标函数进 prompt 自调节 | 形式目标进 prompt（UtilityMax）；标量预算进 prompt（TALE）；外循环目标（OPRO） | UtilityMax NDCG 提升；TALE −75.7% token 且 GSM8K +3.1pt | S_α 定义域=分解树结构×检索预算；S–B Pareto 可解释曲线；单次生成内自算边际权衡 |

**术语谱系备注（防审稿人混淆）**：「iterative deepening」一词在文献中有三条独立谱系——(i) 经典搜索：Korf 1985 IDA* 系（深度界限递增的 DFS）；(ii) LLM 采样调度：ID-Sampling [arXiv:2502.05449]（token 预算几何递增+反思触发）；(iii) S5 语义：分解树层级按需加深（最近邻术语实为 recursive/as-needed re-decomposition，ADaPT/RDD 系）。论文措辞建议用 "gap-check-driven recursive re-decomposition"，避免直接占用 "iterative deepening"，除非显式注明沿用 (i) 的类比并引用 (ii) 作区分。

---

## §3 S5 三差异点逐条判定（对应 Q1/Q2/Q3 的论证细节）

### 3.1 差异点 (a)：迭代加深（状态机架构，允许返回 P1）

**先例簇（按机制强度排序）：**
- **ADaPT** [arXiv:2311.05772]（2023-11，AI2/UNC）：executor 失败 → planner 再分解 → 递归调用自身。与 S5"gap check 不过 → 回 P1 加深"**控制流同构**；差异：触发信号是执行失败（agent 任务）而非信息缺口核查（研究任务）；无检索预算；无目标函数；分解深度由能力自适应而非显式公式。
- **IdealGPT** [arXiv:2305.14985]（2023-05）：Reasoner 不置信 → 触发新一轮 sub-question 分解，直到置信或达迭代上限；有迭代分解消融。差异：置信度信号（模型自报）vs gap check（结构化核查）+ S_α（解析式）。
- **RT-RAG** [arXiv:2601.11255]（2026-01）：初次检索不满意 → 重述问题 → **重复分解与检索步骤**（iterative refinement 环路），另有最大深度硬超参。差异：环路触发是答案满意度，非层级缺口；无 source tagging。
- **RDD** [arXiv:2505.02576]（2025-05）：递归 split→solve-or-split→merge，带依赖占位符 {P-1} 形成 DAG，含 merge 时错误恢复。差异：通用分治推理，无检索/验证阶段。
- **SMoT** [arXiv:2312.17445]（2023-12）：显式状态机——状态=分解后子问题、转移=子问题依赖；PlAgt/ActAgt 分工；跨轨迹经验复用。差异：状态机用于推理轨迹组织与经验记忆，非研究 pipeline 的 P1→P1.5→P2/P3→P4 相位控制。
- **λ-RLM** [arXiv:2603.20105]（2026-03）：把递归分解做成受限运行时：Split(P,k\*)/Map/Reduce 组合子，(k\*, τ\*, d) 显式结构参数，成本可解析。差异：结构参数由 planner 决定，模型不自调；面向长上下文腐化而非推理深度。
- 工程侧：**RLM**（Mathews-Tom/rlm，EXECUTE-vs-RECURSE 决策节点+深度/步数限制）、**GPT Researcher deep mode**（breadth×depth 可配置递归树，见 §4）。

**判定：机制级撞车（Q1 有先例）。** 但所有先例的"何时加深"信号 ∈ {执行失败, 自报置信, 答案满意度, 外部 planner}，**没有一个用"信息缺口核查(P1.5) + 显式结构目标函数(S_α)"作为加深判据**；也没有一个把迭代加深放进"分解→逐节点验证→综合"的研究 pipeline 状态机。差异化叙事成立，conf 0.75。

### 3.2 差异点 (b)：逐节点独立检索验证（非整体上下文）

**先例簇：**
- 检索侧（每子问题独立检索，成熟到成为标配）：Self-Ask [arXiv:2210.03350]、IRCoT [arXiv:2212.10509]（交替式）、TRQA（RAIL 模块按叶子检索）、RT-RAG（每节点一次检索）、QD-RAG [arXiv:2507.00355]（分解→逐子问题检索→合并重排，无训练）、Decompositional Graph Retrieval [arXiv:2506.13380]（逐子问题迭代检索子图再合并）。
- 验证侧（每 claim 独立核验）：FActScore 谱系——ClaimDecomp 质量研究 [arXiv:2403.11903]、ClaimVer [DOI:10.18653/v1/2024.findings-emnlp.795]（claim 级 Attributable/Extrapolatory/Contradictory + 归因分）、decompose-then-verify 流水线综述（OpenReview wT6R0z9kbx）；架构化验证 [arXiv:2609.31937]（每规范层配验证器、确定性 gate 先于 LLM judge、拒绝预算耗尽→abstention）。
- 何时值得检索/验证（节点级路由的最近邻）：Adaptive-RAG [arXiv:2403.14403]（问题级三路由）、Self-RAG [arXiv:2310.11511]（token 级反射）、FLARE [arXiv:2305.06983]（置信阈值触发）、BAR [arXiv:2610.07739]（预算内逐步骤核验+provenance）。

**判定：部分重叠（related work），无整体撞车。** "逐节点检索"与"逐 claim 验证"各自都是成熟先例（因此**不能**声明首创），但：(i) 验证与检索在**同一棵分解树的节点上对齐**（每个 P1 节点携带自己的证据与核验状态）未见先例——FActScore 线验证的是**已生成文本**的 claim，S5 验证的是**解题前的知识需求节点**；(ii) source tagging 决定"该节点要不要花预算验证"（given/knowledge 免检、search 才检）无学术先例（§1.2 第 5 行；T51 §4-N4 同判）。差异化叙事成立，conf 0.75。

### 3.3 差异点 (c)：显式目标函数 S_α 驱动分解深度

**先例簇：**
- **UtilityMax** [arXiv:2603.11583]（2026-03，v4 2026-05）：**最强学术近邻**。核心主张与 S5(c) 同思想——"自然语言指令在多目标下含糊，应把任务重构为形式化优化目标（影响图+效用函数）写进 prompt，令 LLM 显式对目标每个分量推理"；零样本、三前沿模型验证。**差异**：效用定义在任务输出的条件概率分布上（推荐排序质量），是"答案应该是什么"的目标；S_α 定义在**分解树结构**上（Σn·ln(kₙ)+边际增量 Δ=ln((kₙ+1)/kₙ)+预算 B），是"努力应该花在哪、拆多深"的元目标。前者优化 answer，后者优化 deliberation 结构。
- **TALE** [arXiv:2412.18547]：标量 token 预算进 prompt + 模型自估预算（TALE-EP），GSM8K 准确率 81.35→84.46 且输出 −75.7%。差异：标量 vs 结构公式；token 长度 vs 树深宽。
- **OPRO** [arXiv:2309.03409]：目标函数描述进 meta-prompt，但由外部 scorer 打分、跨迭代优化。差异：外循环 vs 单次生成内自调节。
- **λ-RLM** [arXiv:2603.20105]：(k\*, τ\*, d) 显式控制分解形状，但由 planner 计算注入，模型不自调。
- **IBC/VOI** [arXiv:2605.05701]：运行时"单位预算边际任务价值"打分选择 检索/分解/提交——**边际收益思想同源**，但是外部控制器的启发式分，非 prompt 内公式。
- 反向对照：Reward Design with LMs [arXiv:2303.00001]（LLM 给别人当奖励函数）、rubric-as-reward 线（评审/RL 侧）。

**判定：无撞车（Q3 无完整先例），但 UtilityMax 必须作为"形式化目标进 prompt"的开创性引用正面处理。** S5 的独占点是"结构效用 × 检索预算 × 分解树"的定义域组合。conf 0.7（受限于 API 渠道不可用；两轮独立关键词组 + T51 三渠道尝试均未命中）。

---

## §4 最近邻系统专节（任务书点名的四个 + deep research 系）

| 系统 | 它怎么做 | 有没有量化"分解本身贡献了多少分" | 与 S5 的关键区别 | 判定 |
|------|----------|----------------------------------|------------------|------|
| **GPT Researcher deep mode**（assafelovic/gpt-researcher，一手 repo 文档） | planner 生成研究问题 → 并行 crawler 逐问题采集 → 摘要+来源追踪 → 聚合报告；deep research = **可配置 breadth×depth 的递归树探索**，跨分支上下文管理，~5min/$0.4 每次 | **否**——只有成本/时长数字，无任何消融或质量对照实验 | 工程系统无 peer review；分解形状是配置超参而非模型自调；验证=来源追踪而非逐节点核验；无目标函数 | 部分重叠（工程先例，学术未量化）——**撞车风险被低估项**，见 §7 质询 3 |
| **STORM** [arXiv:2402.14207]（NAACL'24） | 多视角发现 → persona 对话式提问（接地于检索）→ 信息策展 → 大纲 → 成文；假设"深入提问需要迭代研究" | **部分**——question-asking 机制消融 + 人评（组织性 +25%、广度 +10%）；但未单独剥离"分解/提问结构"贡献 | 分解发生在**写作前研究阶段**且由多 persona 驱动（横向多样性），S5 是单模型逐层纵向加深；无预算记账；无逐节点验证（引用接地在成文层） | 部分重叠 |
| **Self-Refine** [arXiv:2303.17651]（NeurIPS'23） | 同一冻结 LLM：生成→自我反馈→修订，循环；无训练 | **部分**——7 任务逐一报告（平均 ~20%），数学≈0 的失效边界诚实披露 | 迭代对象是**同一份输出**（refine），不是**问题结构**（decompose）；无检索、无树 | 部分重叠（低） |
| **Reflexion** [arXiv:2303.11366]（NeurIPS'23） | 试错→语言化反思→情景记忆→下次尝试条件化 | 否（91% vs 80% 端到端） | 跨 trial 学习 vs 单题内分解；无分解树 | 无关～部分重叠（低） |
| **ToT** [arXiv:2305.10601] / **GoT** [arXiv:2308.09687] | 解空间搜索树/图：thought 生成+自评+BFS/DFS（ToT）、聚合/精炼/反馈环（GoT） | 否（端到端任务成功率） | 树是**候选解空间**，S5 的树是**问题结构分解**（正交因子/定义展开/可计算项）；搜索由外部算法驱动 | 部分重叠（低）——必须引用以区分两种"树" |
| **WebThinker** [arXiv:2504.21776] | LRM 在推理轨迹中自主穿插 搜索/导航/起草；section-aware 分解连接规划与生成 | [abstract-only] 未见分解贡献消融 | RL/交错式单轨迹 vs 显式相位状态机；无节点级验证协议 | 部分重叠 [abstract-only，conf 降档] |
| **DeepResearcher** [arXiv:2504.03160] | 端到端 RL（GRPO）在真实 web 训练；涌现规划/交叉验证/自我反思/诚实性 | 否（RL 端到端） | 训练内化 vs prompt 注入——**功能等价性威胁**，见 §7 质询 1 | 部分重叠（对照组） |
| **Step-DeepResearch** [arXiv:2512.20491] | 意图分析→分步计划→围绕子问题组织工具调用→多源过滤/对比/交叉验证→成稿；SFT+RL 三阶段 | 否（技术报告级） | 同上（训练路线）；阶段划分与 S5 P1–P4 神似但由训练固化 | 部分重叠 |
| **DeepResearch Bench**（ICLR'26, Du et al.） | 100 个博士级任务×22 领域；RACE（报告质量）+FACT（检索/引用能力）自动评测 | 评测框架本身不测分解贡献，但 FACT 提供引用可靠性维度 | 是 pfb 可借用的外部效度工具 | 无关（基础设施，建议引用） |
| **DRBench** [arXiv:2510.00172]（ICLR'26） | 企业级 deep research 基准；基线 agent 多阶段架构 Stage1=分解研究问题为结构化子任务 | 部分（planning/insight/grounding 三维评分；发现 agent 常漏高价值洞察、引用无关证据） | 评测向；证实"分解质量≠检索质量"需要分开测——支撑支柱 A | 部分重叠（评测近邻） |
| **Beyond Retrieval** [arXiv:2512.00986] | 把 DR 工作流模块化：Planning/Retrieval/Reasoning 分开评测；planning 用专家结构化大纲做 ground truth，量化子任务 **coverage/redundancy/correctness** | **是——目前最接近"分解本身贡献多少"的模块化量化** | 评的是分解产物质量而非分解对最终答案的因果贡献（无干预式消融）；无逐节点验证/目标函数维度 | 部分重叠（高）——支柱 A 的直接方法论对话对象 |

---

## §5 候选评分总表

评分维度与权重（任务书）：机制重叠 30% · 量化程度 25% · 任务类型 20% · 时间 15% · 可复现性 10%。各维 0–5 分；加权总分 ≥3.5 → **撞车风险（须正面差异化）**；2.0–3.49 → **部分重叠（related work）**；<2.0 → **无关（留档）**。任务类型分：open-ended/research=5，multi-hop QA=4，agent 任务=3，数学/符号=2，其他=1。时间分：2026=5，2025=4，2024=3，2023=2，≤2022=1。

| # | 候选（引用） | 机制 | 量化 | 任务 | 时间 | 复现 | 加权 | 判定 |
|---|--------------|------|------|------|------|------|------|------|
| 1 | ADaPT [arXiv:2311.05772] (2023, Prasad et al.) | 5 | 4 | 3 | 2 | 5 | **3.80** | 撞车风险(Q1) |
| 2 | RT-RAG [arXiv:2601.11255] (2026) | 5 | 4 | 4 | 5 | 2 | **4.25** | 撞车风险(Q1+Q2) |
| 3 | IdealGPT [arXiv:2305.14985] (2023) | 4 | 4 | 4 | 2 | 3 | **3.55** | 撞车风险(Q1) |
| 4 | RDD [arXiv:2505.02576] (2025) | 4 | 5 | 2 | 4 | 3 | **3.65** | 撞车风险(Q1 理论) |
| 5 | UtilityMax [arXiv:2603.11583] (2026) | 3 | 4 | 1 | 5 | 3 | **3.10** | 部分重叠(Q3 最强近邻) |
| 6 | λ-RLM [arXiv:2603.20105] (2026) | 4 | 3 | 1 | 5 | 3 | **3.25** | 部分重叠(Q1/结构参数) |
| 7 | SMoT [arXiv:2312.17445] (2023) | 4 | 2 | 2 | 2 | 3 | **2.85** | 部分重叠(状态机×分解) |
| 8 | GPT Researcher deep mode（repo 文档, 2024–2026 持续迭代） | 5 | 0 | 5 | 4 | 5 | **3.75** | 撞车风险(工程先例) |
| 9 | STORM [arXiv:2402.14207] (2024, NAACL) | 3 | 4 | 5 | 3 | 5 | **3.75** | 撞车风险(研究 pipeline 近邻) |
| 10 | Beyond Retrieval [arXiv:2512.00986] (2026) | 3 | 5 | 5 | 5 | 3 | **4.05** | 撞车风险(量化方法近邻) |
| 11 | Tree of Problems [arXiv:2410.06634] (2024) | 4 | 3 | 2 | 3 | 4 | **3.25** | 部分重叠 |
| 12 | TRQA [DOI:10.1609/aaai.v38i17.29928] (2024) | 4 | 2 | 4 | 3 | 3 | **3.25** | 部分重叠 |
| 13 | Dissecting Agentic RAG [arXiv:2606.21553] (2026) | 3 | 5 | 4 | 5 | 4 | **4.05** | 撞车风险(消融方法近邻) |
| 14 | BATS [arXiv:2511.17006] (2025) | 3 | 4 | 4 | 4 | 4 | **3.70** | 撞车风险(预算×计划树) |
| 15 | IBC/VOI [arXiv:2605.05701] (2026) | 3 | 3 | 4 | 5 | 2 | **3.35** | 部分重叠 |
| 16 | TALE [arXiv:2412.18547] (2024, ACL'25 Findings) | 2 | 4 | 2 | 3 | 4 | **2.85** | 部分重叠(Q3 标量版) |
| 17 | Verification-Layer [arXiv:2609.31937] (2026) | 3 | 3 | 3 | 5 | 2 | **3.15** | 部分重叠(Q2 验证架构) |
| 18 | BAR [arXiv:2610.07739] (2026) | 3 | 2 | 5 | 5 | 2 | **3.20** | 部分重叠(Q2 预算×provenance) |
| 19 | Adaptive-RAG [arXiv:2403.14403] (2024, NAACL) | 3 | 3 | 4 | 3 | 5 | **3.40** | 部分重叠(Q2 路由) |
| 20 | Self-RAG [arXiv:2310.11511] (2023, ICLR'24) | 2 | 3 | 4 | 2 | 5 | **2.95** | 部分重叠 |
| 21 | FLARE [arXiv:2305.06983] (2023, EMNLP) | 2 | 2 | 4 | 2 | 5 | **2.70** | 部分重叠 |
| 22 | ClaimVer [DOI:10.18653/v1/2024.findings-emnlp.795] (2024) | 2 | 3 | 3 | 3 | 3 | **2.70** | 部分重叠(Q2 claim 验证) |
| 23 | ClaimDecomp [arXiv:2403.11903] (2024) | 2 | 4 | 3 | 3 | 4 | **3.05** | 部分重叠(Q2) |
| 24 | QD-RAG [arXiv:2507.00355] (2025, ACL SRW) | 3 | 2 | 4 | 4 | 3 | **3.10** | 部分重叠 |
| 25 | Decomp-GraphRetrieval [arXiv:2506.13380] (2025) | 3 | 2 | 4 | 4 | 3 | **3.10** | 部分重叠 |
| 26 | Self-Ask [arXiv:2210.03350] (2022, EMNLP'23) | 3 | 2 | 4 | 1 | 5 | **2.80** | 部分重叠(谱系起点) |
| 27 | IRCoT [arXiv:2212.10509] (2022, ACL'23) | 3 | 2 | 4 | 1 | 5 | **2.80** | 部分重叠 |
| 28 | DecomP [arXiv:2210.02406] (2022, ICLR'23) | 3 | 1 | 3 | 1 | 4 | **2.35** | 部分重叠(低) |
| 29 | Least-to-Most [arXiv:2205.10625] (2022, ICLR'23) | 3 | 2 | 2 | 1 | 4 | **2.40** | 部分重叠(低) |
| 30 | ToT [arXiv:2305.10601] (2023, NeurIPS) | 2 | 2 | 2 | 2 | 5 | **2.35** | 部分重叠(低，两种树必须区分) |
| 31 | GoT [arXiv:2308.09687] (2023, AAAI'24) | 1 | 3 | 2 | 2 | 5 | **2.25** | 部分重叠(低) |
| 32 | Plan-and-Solve [arXiv:2305.04091] (2023, ACL) | 2 | 2 | 2 | 2 | 5 | **2.45** | 部分重叠(低) |
| 33 | Self-Refine [arXiv:2303.17651] (2023, NeurIPS) | 2 | 4 | 3 | 2 | 5 | **3.05** | 部分重叠(迭代≠分解) |
| 34 | Reflexion [arXiv:2303.11366] (2023, NeurIPS) | 1 | 2 | 3 | 2 | 5 | **2.20** | 部分重叠(低) |
| 35 | HyperTree Planning [arXiv:2505.02322] (2025) | 3 | 2 | 3 | 4 | 2 | **2.90** | 部分重叠 |
| 36 | RDoLT [arXiv:2501.02026 + JAIR] (2025) | 3 | 3 | 2 | 4 | 2 | **2.90** | 部分重叠 |
| 37 | WebThinker [arXiv:2504.21776] (2025) [abstract-only] | 3 | 1 | 5 | 4 | 3 | **3.00** | 部分重叠(conf 降档) |
| 38 | DeepResearcher [arXiv:2504.03160] (2025) [abstract-only] | 2 | 1 | 5 | 4 | 5 | **2.90** | 部分重叠(RL 对照) |
| 39 | Step-DeepResearch [arXiv:2512.20491] (2025) [abstract-only] | 3 | 1 | 5 | 4 | 2 | **3.00** | 部分重叠(conf 降档) |
| 40 | DRBench [arXiv:2510.00172] (2025, ICLR'26) | 2 | 4 | 5 | 4 | 3 | **3.35** | 部分重叠(评测近邻) |
| 41 | DeepResearch Bench (ICLR'26, Du et al.) | 1 | 3 | 5 | 5 | 4 | **3.30** | 部分重叠(评测基础设施) |
| 42 | Deep Research 综述 [arXiv:2508.12752] (2025) | 1 | 2 | 5 | 4 | 5 | **3.05** | 部分重叠(综述定位用) |
| 43 | Autonomous Research Agents 综述 [arXiv:2608.05179] (2026) | 1 | 2 | 5 | 5 | 3 | **2.95** | 部分重叠(综述定位用) |
| 44 | ID-Sampling [arXiv:2502.05449] (2025) | 1 | 4 | 2 | 4 | 3 | **2.55** | 无关(术语撞名，须区分) |
| 45 | Scheduler-Theoretic [arXiv:2604.11378] (2026) | 2 | 1 | 3 | 5 | 2 | **2.40** | 无关(架构谱系背景) |
| 46 | SHIELDA [arXiv:2508.07935] (2025) | 2 | 2 | 3 | 4 | 2 | **2.55** | 无关(异常处理工程) |
| 47 | M-ER [arXiv:2610.39667] (2026) | 1 | 2 | 4 | 5 | 2 | **2.45** | 无关(KBQA 子图检索) |
| 48 | OPRO [arXiv:2309.03409] (2023, ICLR'24) | 2 | 3 | 2 | 2 | 4 | **2.45** | 部分重叠(低，Q3 对照) |
| 49 | s1 [arXiv:2501.19393] (2025) | 1 | 4 | 2 | 4 | 5 | **2.85** | 无关(解码干预对照) |
| 50 | Snell compute-optimal [arXiv:2408.03314] (2024, ICLR'25 oral) | 1 | 4 | 2 | 3 | 4 | **2.55** | 无关(算力分配对照) |
| 51 | SHIELD（Chen et al., 转引自 BJMS 综述）[abstract-only, id 待核验] | 3 | 2 | 4 | 2 | 1 | 2.60 | 部分重叠(**二次引用，不入判定依据**) |

注：加权=0.30×机制+0.25×量化+0.20×任务+0.15×时间+0.10×复现。判定阈值见本节开头。撞车风险 8 项、部分重叠 33 项、无关 9 项、二次引用降档 1 项。

---

## §6 撞车风险矩阵（S5 组件 × 文献）

| S5 组件 | 最强先例 | 重叠面 | 文献未覆盖面（pfb 增量） | 量化缺口（文献没测的） | 撞车风险 | 建议叙事 |
|---------|----------|--------|--------------------------|------------------------|----------|----------|
| P1 逐层分解+source tagging | RT-RAG(2601.11255)、QD-RAG(2507.00355)、GPT Researcher(工程) | 递归分解树、逐节点检索、报告聚合 | given/knowledge/search 节点级三源标注；knowledge 节点"必须含数值/公式"的断言纪律 | 三源标注对幻觉率/预算效率的因果贡献 | **中** | "分解树+来源纪律"而非"分解树"本身 |
| P1.5 gap check + 迭代加深(返回 P1) | ADaPT(2311.05772)、IdealGPT(2305.14985)、RT-RAG 迭代环 | 失败/不置信触发再分解的控制流 | gap check 作为结构化信息缺口核查（vs 执行失败/自报置信）；加深判据挂接 S_α 边际收益 | 迭代加深轮数×深度得分的剂量-反应曲线（pfb 已有 v8→v13 证据） | **高** | 不声明首创迭代分解；声明"缺口核查+效用判据驱动的加深"并引用 ADaPT 对照 |
| P2/P3 逐节点检索验证 | ClaimVer/FActScore 线、2609.31937、BAR(2610.07739) | claim 级独立核验、预算有界验证、provenance | 验证对象=解题前知识需求节点（非生成后文本）；验证与检索共用同一棵树；预算耗尽→节点级 [待核验] 降级 | 节点级验证对 gold 覆盖率的组件贡献（支柱 A 的 search×verify 不可加性） | **中** | "分解树上的对齐验证"而非"逐 claim 验证" |
| S_α=Σ[n·ln(kₙ)] 目标函数进 prompt | UtilityMax(2603.11583)、TALE(2412.18547)、λ-RLM(2603.20105) | 形式化目标/预算写进 prompt、结构参数显式化 | 效用定义域=分解树结构×检索预算；模型单次生成内自算 Δ=ln((kₙ+1)/kₙ) 权衡深宽；S–B Pareto 可解释曲线 | prompt 遵循度（模型是否真的按公式调节）、S 值与独立 judge 深度分的共向性（pfb 已有 8.15/7.19/5.49↔0.26/0.289/0.159 证据） | **低** | 核心方法贡献；引 UtilityMax 作"形式化目标进 prompt"先声，引 TALE 作标量预算对照 |
| P4 综合（报告生成） | STORM、WebThinker、Step-DeepResearch | 分解产物→大纲→成文 | （无独占点） | — | 低（不构成贡献声明） | 作为 pipeline 完整性引用 STORM 系即可 |

矩阵读法：**唯一"高"风险格是 P1.5 迭代加深**——论文任何"首个迭代/递归分解"措辞都会被 ADaPT/IdealGPT/RDD 直接反驳；"低"风险格是 S_α——两轮独立调研（T51 三渠道 + T52 四象限）均未命中。

---

## §7 反方复核（对抗性质询 ≥3，逐条回应）

**质询 1：「你的关键词全在 prompting/RAG 圈打转，可能漏掉 RL 训练出的分解策略——DeepResearcher/Search-R1/AnySearch 把'分解+预算+验证'内化进权重，功能上与你的 prompt 注入等价，凭什么说组合无先例？」**
回应：承认功能等价性威胁，已把 RL 系（#38 DeepResearcher、Search-R1 [arXiv:2503.09516]、AnySearch [arXiv:2609.00813]、Step-DeepResearch #39）全部列入总表与 §4。差异化不在"能否做到"而在三点可辩护属性：(i) training-free 可迁移到任意基座（pfb 实测 qwen 本地模型）；(ii) 准则显式可读→行为可审计（S 值可复算、judge 共向可验证）；(iii) RL 系的分解行为涌现且不可解释（DeepResearcher 自己报告"涌现规划/交叉验证"但无法指定形状）。论文措辞必须限定"**在 prompt 层/无训练设定下**首个…"，否则该质询成立。残余风险：中。

**质询 2：「你把 ID-Sampling(#44) 判无关，但它名字就叫 iterative deepening、机制也是'预算不够→注入触发语→继续加深'，和你的 P1→P1.5→返回 P1 控制流同构，判无关是否草率？」**
回应：维持无关判定但升级为"必须主动区分"项：ID-Sampling 加深的是**单条生成的 token 预算**（几何级数扩采样窗口+反思触发语），作用对象是解码过程；S5 加深的是**问题结构树的层级**，作用对象是分解产物。两者共享"iterative deepening"术语（源自经典 IDS 搜索）恰好说明该术语有独立的谱系（Korf 1985 的 IDS → ID-Sampling → S5），related work 应把这条术语谱系讲清以防审稿人混淆。另注意其结论"模型能自纠但不能自判何时触发"反而是 S_α/P1.5 外部化判据的动机证据。残余风险：低。

**质询 3：「GPT Researcher deep mode 是 breadth×depth 递归研究树+逐问题采集+聚合报告，形态上就是 S5 去掉目标函数；你给它量化维度打 0 分把它压到部分重叠，但它 60k+ star 的工程存在意味着'撞车'在实践层面已经发生，学术评分掩盖了叙事风险。」**
回应：接受该质询的核心——已在 §6 矩阵把 P1 行风险标"中"并把它列入撞车风险格（#8, 3.75 分实际过 3.5 阈值，判定已是"撞车风险(工程先例)"）。补充防御：(i) GPT Researcher 无任何消融/对照数据（一手 repo 文档核实），因此 pfb 的**组件贡献测量**（支柱 A）对它构成严格增量；(ii) 其 depth/breadth 是用户配置超参，树形状不由模型按准则自调——S_α 恰好回答"depth/breadth 应该设多少"这个 GPT Researcher 留给用户的问题。论文应显式引用它并说"工程系统已验证递归研究树可用性，但未回答分解形状如何决定、各组件贡献几何"。残余风险：中（审稿人若来自工程背景会追问）。

**质询 4：「UtilityMax 你说'效用作用域不同'就排除撞车，但它的核心 claim——形式化数学目标写进 prompt 约束 LLM 显式推理——与你的 (c) 是同一个 idea 的两次实例化；按专利审查的'等同替换'标准，把推荐效用换成树效用算显而易见的变体，Q3 的'无先例'是否过强？」**
回应：部分接受，已把 Q3 conf 从 T51 的 0.75 下调至 **0.7** 并把 UtilityMax 升级为"Q3 最强学术近邻、必须正面引用"。辩护点：(i) 时间线——UtilityMax v1 (2026-03) 晚于 pfb 本地实验记录，不构成优先权威胁，但构成**同期工作**（concurrent work），论文应如实标注；(ii) 非显而易见性论证素材：S_α 的定义域（树结构×外部预算）带来 UtilityMax 影响图框架不直接覆盖的要素——预算约束下的边际收益递减与诚实降级协议，这两者在 UtilityMax 中无对应物；(iii) 实证义务：论文应补一个"自然语言深度指令 vs S_α 公式"的 prompt-form 消融（UtilityMax 的 Harsh/自然语言基线范式可直接借用），若 S_α 不赢，Q3 贡献声明需再收窄。残余风险：中高——这是三个判决句中 conf 最低的一条。

**质询 5（自加）：「四象限里'最近轨迹 2026-06~11'你只有 4 条命中（2608.05179/2609.31937/2610.07739/2610.39667+2512.x 系列属 12 月），会不会漏了 2026 年 9–11 月刚挂出的同题预印本？」**
回应：承认覆盖窗口风险。已用 deep research agent/ablation/planning 三组 2026 向查询（§1.1 最近轨迹行）扫过 arXiv html 新文（2604.11378、2606.21553、2608.05179、2609.31937、2610.07739、2610.39667、2512.00986、2512.20491 均在列），未发现 S_α 类构造；但 arXiv API 的 submittedDate 过滤通道在本会话不可用（§1.3），**发表前（尤其投稿前一周）必须重跑一次 2026-09 之后的 arXiv listing 检查**，此为程序性遗留风险，已写入 §8 行动项。

---

## §8 related work 定位建议（含行动项）

**建议段落草稿（英文，可直接改写进论文）：**

> Hierarchical decomposition of complex problems for LLMs has been studied extensively: least-to-most and decomposed prompting establish the subproblem paradigm [arXiv:2205.10625, arXiv:2210.02406]; recursive, as-needed re-decomposition on failure or low confidence appears in ADaPT [arXiv:2311.05772], IdealGPT [arXiv:2305.14985], and RDD, which additionally proves decomposition helps only past a difficulty transition point [arXiv:2505.02576]; retrieval-augmented variants organize sub-questions into trees with per-node retrieval and depth limits [DOI:10.1609/aaai.v38i17.29928, arXiv:2601.11255, arXiv:2507.00355], and production deep-research systems explore breadth×depth trees without training or ablation (GPT Researcher; STORM [arXiv:2402.14207]). Claim-level verification decomposes outputs into subclaims checked independently against evidence [arXiv:2403.11903, DOI:10.18653/v1/2024.findings-emnlp.795], and budget-bounded verification with honest abstention on exhaustion has been proposed at the answer level [arXiv:2609.31937]. Most recently, formal mathematical objectives have been injected into prompts to constrain LLM reasoning about task-level utility [arXiv:2603.11583], and scalar token budgets have been shown to steer reasoning effort without training [arXiv:2412.18547].
>
> Our S5 pipeline differs from this body of work in the *object* of optimization and the *locus* of control: the injected objective S_α=Σₙ n·ln(kₙ) is defined over the shape of the decomposition tree itself — its within-layer marginal returns Δ=ln((kₙ+1)/kₙ) and its retrieval-budget coupling — so a single training-free prompt lets the model jointly decide how deep to decompose, how wide to go per layer, and which nodes warrant spending verification budget, with exhausted budget degrading honestly to per-node [unverified] tags rather than answer-level abstention. Crucially, whereas prior systems report end-to-end gains, we measure the causal contribution of each pipeline stage (decomposition, gap-check-driven deepening, per-node verification) to reasoning depth, and find no unified search×verify contribution function — complementing modular evaluations of deep-research planning quality [arXiv:2512.00986, arXiv:2510.00172].

**措辞红线（由 §6/§7 导出）：**
1. 禁用："first to iteratively decompose / recursive decomposition / per-claim verification / budget-aware agent"——分别被 ADaPT·IdealGPT·RDD / FActScore 线 / BATS·AnySearch 占据。
2. 可用："first **training-free, objective-function-driven** regulation of decomposition-tree shape **under an explicit retrieval budget**"；"first to report **stage-level causal contributions** in a decompose→verify→synthesize research pipeline"。
3. UtilityMax 按 concurrent work 处理（v1 2026-03），引用时注明效用定义域差异。
4. 行动项：投稿前重跑 arXiv 2026-09+ listing 检查（质询 5）；补"自然语言深度指令 vs S_α"prompt-form 消融（质询 4）。

---

## §9 来源清单与阅读深度（≥15 来源，≥8 已读正文）

**[已读正文]（21 篇，正文抽取覆盖方法/实验/消融章节）：**
1. [arXiv:2311.05772] ADaPT (2023, Prasad) — §1/§3 正文
2. [arXiv:2305.14985] IdealGPT (2023) — 摘要+§4.4 消融
3. [arXiv:2505.02576] RDD (2025, Hernández-Gutiérrez) — pith 评审级全文抽取（核心定理+referee）
4. [arXiv:2402.14207] STORM (2024, Shao) — §1/§3/§8 正文
5. [arXiv:2601.11255] RT-RAG (2026) — §1/§3/§4.7 正文（T51 抽取复用）
6. [arXiv:2501.02026] RDoLT (2025) — §1/§3/附录 + JAIR 版
7. [arXiv:2312.17445] SMoT (2023) — §1/§3/§6 正文
8. [arXiv:2603.20105] λ-RLM Y-Combinator (2026) — §1–3/附录 D
9. [arXiv:2603.11583] UtilityMax (2026, Marom) — abstract+§2–5 PDF 正文
10. [arXiv:2303.17651] Self-Refine (2023, Madaan) — 全文级细节（含数学失效 caveat）
11. [arXiv:2303.11366] Reflexion (2023, Shinn) — pith 评审级抽取
12. [arXiv:2308.09687] GoT (2023, Besta) — AAAI OJS 正文（Table 2、实验）
13. [arXiv:2305.04091] Plan-and-Solve (2023, Wang) — 官方 repo+结果细节
14. [arXiv:2205.10625] Least-to-Most (2022, Zhou) — arxiv html 正文
15. [arXiv:2502.05449] ID-Sampling (2025, Chen) — §1/§6/§7 正文+pith 评审
16. [arXiv:2507.00355] QD-RAG (2025, ACL SRW) — Algorithm 1+§1/§3 正文
17. [arXiv:2506.13380] Decompositional Graph Retrieval (2025) — §1/§2/§6 正文
18. [arXiv:2508.12752] Deep Research Survey (2025) — §1/§2.3/§3.2/§5/§6 正文
19. [arXiv:2608.05179] Autonomous Research Agents Survey (2026) — §6 正文
20. [arXiv:2512.00986] Beyond Retrieval (2026) — §1/§2 正文
21. [arXiv:2510.00172] DRBench (2025, ICLR'26) — §4 Stage1/Table 5 正文
（另：T51 已读正文并本报告复用：BATS、TALE、IBC/VOI、Dissecting Agentic RAG、Verification-Layer 2609.31937、BAR、Tree of Problems、OPRO、Adaptive-RAG、Self-RAG、s1、ToT、Self-Ask、IRCoT、DecomP、2403.11903——合计正文级阅读 37 篇。）

**[abstract-only]（conf 降档，共 4 篇）：** WebThinker [arXiv:2504.21776]、DeepResearcher [arXiv:2504.03160]、Step-DeepResearch [arXiv:2512.20491]（有 §2/§4 片段，接近正文级但消融未见）、SHIELD（二次引用，id 待核验，不入判定依据）。

**[工程一手来源]：** GPT Researcher README/docs（github.com/assafelovic/gpt-researcher）、RLM repo（github.com/Mathews-Tom/rlm）、Adaptive-RAG 官方 repo citation 块。

**[评测基础设施]：** DeepResearch Bench（ICLR'26 proceedings PDF）、DeepResearchGym（经 2508.12752 转引）。

---

## 附录：与 T51 的交叉引用及新增核验记录

- T51 已核验并在本报告直接复用的 id：2210.03350 / 2212.10509 / 2210.02406 / 2205.10625 / 2305.10601 / 2310.11511 / 2305.06983 / 2403.14403 / 2412.18547 / 2501.19393 / 2309.03409 / 2511.17006 / 2605.05701 / 2609.00813 / 2603.08877 / 2503.09516 / 2410.06634 / 2606.21553 / 2609.31937 / 2610.07739 / 2403.11903 / 2407.15504。
- 本报告新增并核验的 id：2311.05772（arxiv abs+html 双载体）、2305.14985（arxiv html）、2505.02576（pith+emergentmind 综述双源）、2501.02026（arxiv html+JAIR）、2312.17445（arxiv html v1/v2）、2603.20105（arxiv html）、2603.11583（arxiv abs v4+PDF）、2502.05449（arxiv html+pith）、2305.04091（GitHub citation 块+arxiv）、2308.09687（arxiv abs+AAAI OJS DOI:10.1609/aaai.v38i16.29720）、2507.00355（ACL Anthology PDF+arxiv html）、2506.13380（arxiv html）、2508.12752 / 2608.05179 / 2512.00986 / 2510.00172 / 2512.20491（arxiv html/pdf）、2504.21776（arxiv abs）、2504.03160（官方 repo citation 块）、2505.02322（arxiv pdf）、2604.11378（arxiv html）、2508.07935（arxiv pdf）、2610.39667（arxiv abs+html）、ClaimVer DOI:10.18653/v1/2024.findings-emnlp.795（ACL Anthology PDF）。
- 未采信/排除：SHIELD 主文献（仅 BJMS 综述转引，一次定向检索未命中一手 arXiv id → 标 [待核验] 且不作判定依据）；emergentmind「LLM-Based Hierarchical TODO Decomposition」主题页（聚合页非一手文献，其 E₀≤b^D·ε_D 关系式仅作数学近邻线索记录）；grasp.study/Databricks/Neo4j 的 provenance tagging（工程教程，仅作 source-tagging 负结果佐证）。
- 渠道故障：fetch 代理（arXiv API/Semantic Scholar API/OpenAlex 直连）5 次尝试全部 SignatureDoesNotMatch，明细在 search-log.json channel_failures；未发生任何"编造命中"——所有零结果短语均如实登记（§1.2）。
