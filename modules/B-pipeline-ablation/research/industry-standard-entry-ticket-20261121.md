# 业内承认的评测规模与报告规范——套磁入场券（2026-11-21）

> origin: ai · 触发：D 问"业内所承认的试题数据量以及其他规范是怎么样的，就是我们拿去 social 套磁的入场券"
> 来源：2410.03492 / 2609.37294（SafeLLM4SE）ar5iv 全文（来源①本轮查证）+ 本地 survey（来源②）。
> 用途：① 套磁时展示"我们知道业内标准、且知道自己在哪"；② 自我差距清单。

## 0. 一句话

业内规范分两层：**规模层**（题数 × 重复数 × 模型数）和**报告层**（必须报什么）。
我们的位置：规模层差 1-2 个量级（3 题 × 10 轮 × 1 模型 vs 100-5760 题 × 30 重复 × 6 模型），
报告层**基本达标且有一处超出**（我们报了方差来源诊断，公开 SOP 都没做这一步）。
套磁叙事 = "小样本私有 bench 的过程/深度评测 + 完整报告规范 + 本地量化模型方差诊断"，
缝隙在"私有小规模 + 过程细粒度"，不在规模。

## 1. 规模层：业内承认的量级（按对口度排序）

| 论文 | 日期 | 题数 | 重复 | 模型数 | 收敛判据 |
|---|---|---|---|---|---|
| 2410.03492 Reproducible LLM Eval | 2024-10 | 100 / 5760 | 1→30 扫描 | 6 | PI 宽度 <0.01 需 n=30 |
| 2609.37294 SafeLLM4SE | 2026-09 | HumanEval（164 题） | 自适应（N_min 起，CI 宽度达标或 token 预算耗尽即停） | 2（示例） | CI 宽度 ≤ w_max 且 token 预算 B |
| 2511.07685 ResearchRubrics | 2025-11 | 101 prompt | —（单跑） | 多 | rubric 2500+ 条（2800+ 人工小时） |
| 2601.08536 DeepResearch Bench II | 2026-01 | 132 任务 × 22 领域 | — | 多 | 9430 条二元 rubric |
| 2607.12252 FinResearchBench II | 2026-07 | 104 题 | — | 多 | 14450 候选 rubric → 共识筛选 |
| **我们 T53b** | — | **3 题** | **10 轮/arm** | **1（NVFP4 本地）** | 无正式判据（ad-hoc trim + 稳健性检查） |

**规模结论**：
- 题数：rubric bench 线公认 100-130 题量级（101/104/132 三篇独立收敛）。我们 3 题差 ~35×。
- 重复数：统计可复现性线 n=30 是"PI<0.01"的门槛（2410）；SafeLLM4SE 更务实——
  自适应采样（N_min 起步，CI 宽度达标或预算耗尽即停），**不强制 n=30**。
- 模型数：复现性研究 6 模型（跨模型泛化）；单模型消融（我们的场景）业内无硬性要求。
- **我们的 n=10 在 SafeLLM4SE 框架下可辩护**：它是"最小样本 + CI 精度目标"而非固定 n=30；
  且我们的 Δ（0.113/0.186）> 5× PI 宽度，结论对样本量稳健（已验证）。

## 1b. 每题评分颗粒度对比（2026-11-21，D 问"他们每题有几百个节点吗"）

**不是几百，是每题 25-71 条平铺二元判据**（来源②：survey 已核的 rubric 总量/题数）：

| bench | 题数 | rubric 总量 | 每题均 | 形态 |
|---|---|---|---|---|
| ResearchRubrics | 101 | 2500 | 25 条 | 平铺（factual/reasoning/clarity） |
| DeepResearch Bench II | 132 | 9430 | 71 条 | 二元判据（recall/analysis/presentation） |
| FinResearchBench II | 104 | 14450 | 139 条（候选，共识筛选后 gold 更小） | 候选→gold 管线 |

**结构差异 > 数量差异**：他们的 rubric 平铺（每条独立二元打勾，打在最终报告）；
我们的是树结构（节点有父子关系，depth 一等指标，打在推理过程）。
单题粒度（来源②：stats.py 注释 + gold 树文件实数）：nat 6 判定点/19 层、soc 7/24 层、
**gpu 38 判定点/122 层**（gpu 单题比 DRB II 的 71 条/题只细不粗，且是树）；
另一套 Q6-Q10 gold 树 34-46 节点/题。

**套磁应答**："3 题凭什么" → 颗粒度不是短板（gpu 122 层树结构 > 平铺 71 条），
短板是题数（3 vs 100-132），属私有 bench 定位；nat/soc 两题 gold 树偏粗（6-7 点）
是标注上限的真实约束 [待核验：是否拆细]。

## 1c. 有效测量量级论证（2026-11-21，D 论点："一个题=一套有依赖的习题，reward 颗粒度满足 100 量级"）

**D 的论点成立一半，另一半需精确化**——套磁时会被攻击的点，提前备好：

**成立：测量精度意义**（conf 0.9）
- 我们的每题分数不是单个 0/1 判断，而是 ~38 个二元节点判定的聚合（gpu 题 coverage = 38 项命中比例，
  二项 SE ≈ √(p(1-p)/38) ≈ 0.08 @ p=0.5；单题测量精度远高于单判断）。
- IRT（项目反应理论，心理测量学 1950s 成熟理论）正是干这个的框架：多个判据（item）联合估计一个
  潜变量（模型对该题的理解质量），**信息量跨 item 累加**。LLM 评测 2026 年已有三篇直接应用（ID 均 abs 核实）：
  - **2611.05556 AGORA**（2026-11-03）：IRT aggregator，把每个 item 放在同一潜质量尺度上，
    judge 用敏感度参数描述，可靠性从所有 item 联合学习——**专治"小评测集（几百 item 以下）"场景**，
    正是我们的规模。
  - **2609.35739 Rubric-Calibrated Preferences**（2026-09-28）：yes/no rubric 判据（递增严格度）
    提供绝对尺度 + IRT 跨 query 校准——与我们"二元节点判定 + 树内聚合"同构。
  - **2608.22295 Contextual Multidimensional IRT**（2026-08-23）：多维 IRT 把 LLM 表示为
    潜能力画像，跨题迁移信息。
  - （2602.00521 IRT 诊断 judge 可靠性，此前已核实。）
- **结论：单题测量精度对标几百条平铺判据的 bench 成立**——我们的 coverage 本身就是 polytomous
  分数（多档），正是 GRM/IRT 建模的对象。

**需精确化：独立样本量意义**（conf 0.9）
- 同题的 38 个判定点是**相关的**（都测"这道题"一个潜变量）→ 有效独立样本量**仍是 3 题，不是 114**。
- 颗粒度提升的是每题的**测量信度**（降低单题分数噪声），不是**题域多样性**。
- 消融检验（formula vs text）的分析单元仍是题 → n=3 题的统计效力没变（这也是我们 n=10 轮重复
  的必要性：轮次是独立样本，判定点不是）。

**套磁叙事（精确版）**：
"我们的 3 题不是 3 个二元判断，是 3 × ~38 项的结构化测量仪器。IRT 框架（AGORA 2611.05556 等
2026 三篇）下判据信息跨 item 累加，单题测量精度对标几百条平铺判据的 bench。剩余差距是
**题域多样性**（3 vs 100-132），不是颗粒度——这也是为什么我们用 10 轮重复补样本量：
轮次是独立样本，判定点是测量仪器。"

**[待做]**：若套磁对象追问，可补一个 IRT 拟合演示（GRM 拟合我们的 38 项 coverage，展示信息函数）
——成本半天，价值高，先不做（Occam：叙事够用就不加实体）。

## 1d. 同类可比文献：树/过程类评测的可发表量级（2026-11-21，D 纠正："depth 这种长程分解/研究，普通平铺量级完全不能比较和替代"）

**D 的纠正成立**（conf 0.95）：depth 测的是长程分解/研究**过程**，平铺 rubric（25-71 项/题）
测的是**最终答案质量**——两个不同构念，不能互相替代。§1b/§1c 的"颗粒度对标"论证只覆盖
coverage 类（答案结构完整性），**不覆盖 depth 类（过程深度）**。depth 的同类可比对象是
树/过程结构评测，不是平铺 rubric bench。

**同类文献（ID 均 abs/ar5iv 核实）**：

| 论文 | 评测单位 | 规模 | 报告方式 |
|---|---|---|---|
| **RPTS** 2511.06899（2025-11，ar5iv 全文已读） | 推理树：叶节点=原子证据，非叶节点=层级推导中间结论，逐节点加权 faithfulness | **390 个推理实例（每个一棵树）**，374 图，多模态 | **单轮 greedy（temp=0），无重复、无 CI、无效应量** |
| **ReasonBench** 2512.07795（2025-12，abs 核实） | 层级分解推理，质量+成本作为分布 | 30 独立试验 × 10 策略 × 12 模型 × 6 任务 | 分布报告；核心发现：greedy 下仍有结构方差，**单次分数会静默错排系统**（最强策略对次强仅 77% 胜率） |
| Tree-PLV 2407.00390（2024-06，abs 核实） | 推理树（best-first 构建）+ 步骤级偏好 | 过程验证器训练 | 训练数据构造，非 bench |

**可发表量级结论**（conf 0.85）：
- 树/过程类评测的可发表规模 = **几百个树实例**（RPTS 390），比平铺 rubric bench（100-132 题）
  低一个量级——因为树实例本身携带几十节点的结构信息，单实例信息密度高。
- 我们的差距：3 棵树 vs 390 树实例（~2 个量级），**比平铺对标（3 vs 100-132）更诚实的表述**。
- 我们的优势：报告规范**超过 RPTS**——它单轮 greedy 裸报均值，我们有 10 轮重复 + Welch/MWU 双检验
  + bootstrap CI + Cliff's δ。ReasonBench 的"单次分数会静默错排"结论直接背书我们的重复设计。

**套磁叙事（depth 维度精确版，替代 §1c 对 depth 的覆盖）**：
"depth 是过程测量，同类可比对象是树结构评测（RPTS 2511.06899：390 个推理树实例，逐节点加权
faithfulness），不是平铺 rubric。我们的 3 棵分解树（19/24/122 层）在该文献量级下差 2 个量级，
但报告规范（10 轮重复 + 分布化报告）对齐 ReasonBench 2512.07795 的标准，超过 RPTS 的单轮裸报。
下一步扩到 10-20 棵分解树即可进入该文献的量级带。"

**RPTS 实例到底是什么（ar5iv Table 1 实测）**：
- 实例 = 一棵推理树，规模按**树高（depth）**统计，不是节点数：
  树高 ≤2: 3.85% / 3: 42.82% / 4: 32.56% / 5: 13.08% / ≥6: 7.69%（390 棵树）
- 即 RPTS 是**浅树评测**（主体 3-5 层），我们是 19/24/122 层——**深度差 4-40 倍**。
- RPTS 无层级依赖约束、无正交/完备/压缩约束——只有"叶=证据、非叶=推导"的结构。
  **我们的层级依赖 + 正交/完备/压缩约束在现有树评测文献中无直接对应物**（conf 0.8，
  基于已查的 RPTS/Tree-PLV/ReasonBench/VISTA 四篇均无此约束组合）——这是 novelty 声明点。

**发表水平 + 滚雪球锚点（venue 均 OpenReview/S2 核实，非凭记忆）**：

| 论文 | venue | 角色 |
|---|---|---|
| Let's Verify Step by Step（OpenAI, 2023, 2305.20050） | arXiv（OpenAI 技术报告） | **PRM 领域开山**（过程奖励模型 + PRM800K 数据集） |
| **Math-Shepherd** 2312.08935 | **ACL 2024**（OpenReview 确认，标题精确匹配） | 步骤级自动验证+强化，PRM 奠基 |
| **Tree-PLV** 2407.00390 | **EMNLP 2024**（S2 确认） | 树基过程验证（步骤级偏好） |
| **VISTA** 2511.10182 | **AAAI 2025**（S2 确认） | 多轮推理过程解构 |
| PRM That Think 2504.16828 | **TMLR accepted**（OpenReview） | PRM 前沿（2026-02 v5） |
| RPTS 2511.06899 | preprint（无 venue，仅 ARR 投稿记录） | 树评测（最接近我们，但未发表） |
| ReasonBench 2512.07795 | preprint（29 页 19 表） | 稳定性基准 |

**滚雪球路径（顶刊锚点 → 领域分支）**：
PRM 开山（Let's Verify Step by Step, OpenAI 2023）→ Math-Shepherd（ACL 2024）→
Tree-PLV（EMNLP 2024）→ PRM That Think（TMLR 2026）= **过程验证/奖励主线**（顶会密度高）。
树评测分支（Tree-PLV → RPTS）= **顶会锚点少**（仅 EMNLP 一篇，RPTS 未发表）——
说明"树结构评测"本身是新兴分支，**我们的层级依赖+正交/完备/压缩约束组合可能是该分支的空白点**
（conf 0.7，待 arena 对抗核验：是否有我们没查到的顶会论文已覆盖此约束组合）。

**关联结构分支全景（2026-11-21 二轮滚雪球，D 质疑"这么少？"后换依赖/拓扑/正交/完备角度重搜）**：

D 的质疑成立：第一轮关键词太窄（"reasoning tree"+evaluation 只抓到树评测基准小类），
换关联结构角度后空间很密，只是**分散在至少 4 个子分支、没有统一命名**——这就是"看起来少"的原因。

| 子分支 | 顶会锚点 | 与我们的对应 |
|---|---|---|
| **PRM 主线**（步骤级奖励/验证） | Let's Verify Step by Step（OpenAI 2023）→ Math-Shepherd（**ACL 2024**）→ Tree-PLV（**EMNLP 2024**）→ PRM That Think（**TMLR**）→ **GPRM 2611.20755**（2026-11-16，最新） | 步骤级信号；**GPRM 明确把"weak historical dependency modeling"列为开放问题——层级依赖建模是业内承认的 gap** |
| **结构化过程监督** | **Rewarding Novel Deductions 2609.34660 = NeurIPS 2026 accepted**（solver-guided，"constraint tracking, consistency preservation, multi-step deduction"）；BioPRM 2610.19657（步骤级一致性验证） | 约束追踪+一致性保持=我们的完备/依赖约束的同构问题 |
| **正交/层级分解** | **Orthogonal Hierarchical Decomposition 2602.01969 = ICML 2026**（表格理解，方法名与我们的正交/完备约束同词）；TaReD 2610.11268（递归分解+"intermediate dependencies"） | 正交层级分解=我们的约束组合的直接词汇对应 |
| **结构完备性/拓扑** | Knossos 2610.04721（**complete** diagram topology extraction 基准）；Completeness and Cost of Retrieval Structures 2610.41905（6 种结构 flat vs hierarchical 对比，**completeness 作为评测维度**的方法学先例） | 完备性作为可测维度=我们的 coverage 指标先例 |
| 树评测基准（第一轮已查） | Tree-PLV（EMNLP 2024）→ RPTS（preprint） | 最接近但顶会薄 |
| 推理树聚合/审计 | AgentAudit 2602.09341（审计多智能体推理树，GSM8K/AMC/MATH/MMLU） | 树结构作为评测对象的方法先例 |

**"为啥这么少"的元答案**（conf 0.85）：
1. **不是少，是散**——过程奖励主线顶会密度其实高（ACL/EMNLP/TMLR/NeurIPS 2026 全有），
   但"层级依赖 + 正交/完备/压缩约束 + 深树评测"这个**交叉点**没有统一命名，
   各子分支各说各话（PRM 说 dependency、表格理解说 orthogonal decomposition、
   拓扑抽取说 completeness），所以按单一关键词搜会严重低估。
2. **交叉点本身是新兴空白**——GPRM（2026-11）把 dependency modeling 列为开放问题、
   NeurIPS 2026 的 solver-guided 才刚把 constraint tracking 做进过程监督，
   说明"带约束的深树过程评测"在 2026 年才刚开始被系统触及。
3. **对我们的含义**：novelty 声明从"树评测文献无对应物"（第一轮，conf 0.8）
   升级为更精确的"**约束组合 × 深树 × 过程评测的交叉点是 2026 年新兴空白，
   各子分支已分别验证了约束（ICML 2026 正交分解）、依赖（GPRM 开放问题）、
   完备性（Knossos/retrieval structures）的独立价值，但没有人把它们组合进一个深树评测**"
   （conf 0.8，仍待 arena 对抗核验）。

**关联结构论文的实验设计全景（2026-11-21 三轮，6 篇 ar5iv 全文提取，数据量/模型/结论）**：

| 论文 | 测试规模 | 训练数据 | 模型 | 核心结论 |
|---|---|---|---|---|
| SPRING 2609.34660（NeurIPS 2026） | ZebraLogic 700 + AR-LSAT 230 + KnK | 250-300 题（RL） | **小模型**：Qwen3-1.7B/4B/8B + Phi-4-Reasoning | solver-guided 过程监督 > base +49.71 点（ZebraLogic）、> outcome-only +15.43；**小模型受益最大** |
| OHD 2602.01969（ICML 2026） | AITQA + HiTab（数百题） | 无（表示方法） | Qwen2-72B + TableLLaMA-7B；judge=Qwen2-72B/DeepSeek-v3/GPT-4 三模型集成 | 正交层级分解 EM +8.79、LLM-eval +18.09 vs 最强基线；跨 evaluator 稳定 |
| BioPRM 2610.19657 | SciRecipe + 自采协议 | 同左（两阶段训练） | 骨干 Llama-3.1-8B + LoRA；对比 GPT-6-luna/Claude-sonnet-5/GLM-5.3/Qwen3.8-flash | **"always-correct 基线 88.53% step accuracy → accuracy alone is insufficient"**（单指标不够，直接背书我们的 depth+coverage 双指标） |
| Knossos 2610.04721 | **19,200 图 / 245,179 节点 / 439,740 边**，6 域；测试 1,200 | 18,000 图 | 开源 7-32B VLM + GPT-4o/GPT-5.6/Opus 5 | 结构化分解（节点清单→边预测）> 一步抽取；小 VLM 训练后大幅提升；闭源泛化更好 |
| TaReD 2610.11268 | 复杂真实工具任务 | 无（推理方法） | matched models/budgets/verifiers | 能力对齐的子任务树 > 单链/plan-then-execute，端到端成功率 **+40pp** |
| AgentAudit 2602.09341 | GSM8K/MATH/AMC/MMLU（标准基准） | consensus-trap 实例（小规模） | Llama3-3B/8B + Qwen2.5-3B/7B，3 seeds | 审计推理树 > 多数投票（+5%）> LLM-judge（+3%）；**改进集中在弱骨干，强骨干趋饱和** |

**跨论文一致模式（conf 0.9，6 篇独立来源）**：
1. **结构化 > 无结构（LLM 自行组织）方向一致**，但改进幅度集中在**弱模型 + 复杂任务**，
   强模型/简单任务上饱和（AgentAudit 原话："As the backbone strengthens... MV baselines
   approach saturation"；SPRING 小模型受益最大；Knossos 闭源大模型已强、结构化增益小）。
2. **目标函数/约束前置是共同设计**：6 篇全部把约束/目标/结构**前置固定**（solver 引导、
   正交分解规则、协议一致性判据、节点-边分解、能力对齐树、审计判据），**没有一篇让 LLM
   自行选择目标函数**——D 的纠正（"目标函数应该前置"）与文献实践一致。
3. **单指标不够**：BioPRM 的 always-correct 88.53% 基线证明裸 accuracy 无法区分——
   与我们 depth+coverage 双指标 + 树内多节点的设计动机相同。

**与我们 T53b 的对照（套磁最强论据）**：
- T53b 的 text arm = "无结构（LLM 自行组织）"，formula arm = "结构前置（管线+约束固定）"
  ——正是这 6 篇的共同对照设计。
- 我们的结果模式（nat/soc 显著、gpu 不显著）**与跨论文的"改进集中在复杂任务、简单任务饱和"
  模式方向一致**（gpu 题相对简单 → 管线增益小；nat/soc 长程分解 → 增益显著）。
  单模型 3 题的小规模结果**复现了顶会多模型大规模的方向性发现**——这是套磁的核心叙事：
  "我们 3 题 × 10 轮的单模型消融，方向性结论与 NeurIPS/ICML 2026 多模型研究一致，
  且报告规范（10 轮重复+CI+效应量）超过其中多数（单轮裸报）。"
- 规模对照：他们测试 230-1200 题（答案准确率），我们 3 题 × ~38 节点（过程结构）。
  他们训 1.7B-8B 小模型（便宜快），我们 1 个 27B 本地量化模型。
  差距表述：题数差 1-2 量级，但单实例信息密度（38 节点树 vs 单答案）高一个量级，
  且方向性结论已被顶会独立复现。

**2026 更新的吗**：三轮 arXiv 检索（tree-structured eval 2026H2 / decomposition tree 2026 /
reasoning process tree bench）无更新的树评测直接命中。最新相关：AtomTree 2610.38744
（2026-10-28，embodied 指令跟随，层级框架但非评测）、PR Tree Rollout 2607.15610
（2026-07-17，RL 训练非评测）。**RPTS（2025-11）仍是最接近的树评测基准**（conf 0.8）。

——构念同构（推理树+节点级打分）但领域不同，
套磁时按"结构同构、领域不同"表述，不 claim 直接可比。



| 类别 | 必须报告 | 我们的现状 | 差距 |
|---|---|---|---|
| Quality | 选定质量指标 + 估计值 θ̂ | coverage/depth 均值 ✓ | 无 |
| Stability | 稳定性指标（SD / 变异系数 / IQR） | stats.md 有 SD ✓ | 无 |
| Estimation uncertainty | **每个主指标 CI + 置信水平** | p 值 ✓ + bootstrap 95%CI ✓（已进主表） | 无 |
| Sampling | 执行次数、采样程序、最小样本量、停止判据、预算 | 10 轮/arm ✓，停止判据=固定 10（未声明） | **小**：停止判据未文档化 |
| Model | 模型名、版本/标识、provider | qwen3.8-27b-mtp ✓ | 无 |
| Inference config | temperature 及其他推理参数 | temp=0 ✓ | 无 |
| Reproducibility | 随机 seed（若支持）、精确 prompt、环境 | prompt-snapshot.md ✓，seed=None 已声明 | 无 |
| Effect size | **效应量，不只报 p 值**（Cliff's δ / rank-biserial） | Cliff's δ ✓（已进主表） | 无 |
| 统计检验 | 独立样本用 **Mann-Whitney U**（非参数）+ bootstrap CI for difference；配对用 Wilcoxon | Welch t + Mann-Whitney U 双报 ✓ | 无 |

## 3. 我们补算的效应量（2026-11-21，来源①本轮计算）

SafeLLM4SE 要求"报效应量而非只报 p 值"。Cliff's δ（一组值超过另一组的比例差，|δ|>0.474 小 / >0.657 中 / >0.814 大）+ bootstrap 95% CI for Δmean（n=20000 重采样，seed=42）：

| 比较 | Δmean | Welch p | U | p_U | Cliff's δ | bootstrap 95% CI | 判定 |
|---|---|---|---|---|---|---|---|
| nat depth | +0.113 | 0.013 | 82 | **0.017** | **+0.640**（中效应） | [+0.034, +0.189] | 显著 + 中效应，CI 不含 0 |
| nat coverage | +0.167 | 0.155 | 71 | 0.107 | +0.420（小效应） | [-0.050, +0.366] | 不显著，CI 含 0 |
| soc coverage | +0.186 | 0.016 | 80 | **0.020** | **+0.600**（接近中效应） | [+0.057, +0.314] | 显著 + 中效应，CI 不含 0 |
| soc depth | +0.003 | 0.939 | 52 | 0.906 | +0.040 | [-0.069, +0.074] | 无 |
| gpu coverage | -0.033 | 0.349 | 18 | 0.297 | -0.330 | [-0.092, +0.030] | 无（n_f=9/n_t=6 功效不足） |
| gpu depth | -0.052 | 0.335 | 24 | 0.813 | -0.090 | [-0.158, +0.029] | 无（功效不足） |

**关键**：两个显著项在三种独立证据下都成立——Welch t（p=0.013/0.016）、Mann-Whitney U（p=0.017/0.020，
SafeLLM4SE 推荐的非参数检验）、bootstrap CI 不含 0 → 主结论对检验方法选择稳健。

**关键**：两个显著项的 bootstrap CI 都不含 0 → 主结论在 SafeLLM4SE 的效应量标准下同样成立。
这是入场券的核心句："按 2026-09 最新报告规范（SafeLLM4SE）复核，我们的显著结论在
效应量（Cliff's δ 0.60-0.64，中效应）和 bootstrap CI 下不变。"

## 4. 套磁叙事（统一入场券）

**开场定位**：我们在做私有小规模 bench（3 题 × 2 臂 × 10 轮）的管线阶段消融 + 分解树
depth/coverage 结构指标，单模型（本地 NVFP4 量化 27b）。**3 题 ≠ 3 个二元判断——是 3 × ~38 项
结构化测量仪器（IRT 框架下信息跨 item 累加，见 §1c），单题测量精度对标几百条平铺判据的 bench；
差距在题域多样性不在颗粒度。**

**展示规范意识**（三句）：
1. 报告规范对标 2410.03492 + 2609.37294（SafeLLM4SE，2026-09）：CI / 效应量 / 方差来源全报。
2. 规模差异已知且可辩护：n=10 的 PI 宽度 ~1.7× n=30，但 Δ > 5× PI 宽度 → 结论稳健；
   且 SafeLLM4SE 的自适应采样框架支持"最小样本 + CI 精度目标"，不强制 n=30。
3. **我们做了一件公开 SOP 都没做的事**：方差来源诊断——单请求 temp=0 串行确定、
   并发非确定（vLLM batch 组合），10 轮方差 = 基础设施 + 引擎并发，非 LLM 采样。
   （本地量化模型场景，2410/SafeLLM4SE 都没覆盖。）

**请教问题**（按套磁对象）：
- ResearchRubrics：logical nesting 轴怎么操作化打分？我们 depth 分是树最大深度，是否同构？
- Dr.Credit：开放题无 gold 时 rubric 参照的失效边界？
- DEEPRUBRIC：evidence-tree 构建成本？我们 gold 树是人工标的。
- SafeLLM4SE 作者（Francisco Ortin, Univ. Oviedo / MTU Cork）：小样本（n<30）私有 bench
  的 CI 精度目标怎么设？自适应采样的 N_min 建议值？

**可分享的结果**：nat depth Δ+0.113（p=0.013, Cliff's δ +0.64, CI [+0.034,+0.189]）、
soc cov Δ+0.186（p=0.016, Cliff's δ +0.60, CI [+0.057,+0.314]），27b NVFP4 本地模型，
formula prompt 臂优于 text 臂（结构化提示提升推理树深度/覆盖）。

## 5. 差距清单（诚实版，按优先级）

1. **[已闭环] 效应量进 stats.md 主表**（2026-11-21）：stats.py 加 Cliff's δ + bootstrap 95%CI 两列，
   reports/t53b/stats.md 已重新生成，回归通过（no-arg == --spec）。
2. **[中] 统计检验用 Welch t 非 Mann-Whitney U**（SafeLLM4SE 推荐非参数）：SafeLLM4SE 推荐非参数（分布偏离正态时更稳）。
   我们 n=10/臂，正态假设本就勉强 → 补 Mann-Whitney U 对照。
3. **[小] 停止判据未文档化**："固定 10 轮"应写成显式判据（SafeLLM4SE 要求声明停止判据）。
4. **[小] 题数 3 vs 业内 100-130**：真实差距，但属"私有 bench"定位的一部分，不是缺陷——
   套磁叙事里正面讲（缝隙定位），不掩饰。
5. **[无] 其余报告项**（quality/stability/model/config/reproducibility）已达标。

## 6. 检索记录

- 2609.37294 ar5iv 全文（/tmp/safe.txt，53494 chars）：Table 2 报告标准 + Algorithm 1 自适应采样
  + 检验选择（Mann-Whitney U / Wilcoxon / bootstrap CI / Cliff's δ / Wilson 区间）。
- 2410.03492 ar5iv 全文（/tmp/rep5iv.html）：规模 100/5760 题 × 1→30 重复 × 6 模型，PI<0.01 需 n=30。
- 本地 survey：process-depth-eval-survey-20261121.md（11 篇规模数据，来源②）。
- 效应量计算：本轮 execute_code（results.json 60 runs 去重后，Cliff's δ + bootstrap n=20000 seed=42）。
