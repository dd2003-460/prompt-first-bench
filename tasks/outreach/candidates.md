# pfb/idea53 套磁候选表（discover 阶段）

> origin: ai · 2026-11-25 · 只读本地文献，不联网。
> 红线：姓名/机构必须本地文件可证，不可证一律 [待核验]；不臆测、不编造。
> 口径（D 2026-11-25 指令）：数量优先，覆盖 pfb/idea53 相关领域完整作者集合；合作角度一句话（基于已发表工作推断，标注推断）；优先级降权但保留。
> idea53 = GPU 瓶颈诊断的闭式测量（microarchitecture 增量贡献，信息论读数）；pfb = 1-loop 流水线在 27B 开放权重上的 stage-ablation。
> 覆盖的本地文献（16 份）：tasks/idea53-goal/submission-staging/references.bib、experiments/stage-ablation/scientisttwo-comparison.md、experiments/stage-ablation/competitor-survey.md、experiments/stage-ablation/paper-draft.md、experiments/stage-ablation/workshop-draft-metacog-20261122.md、experiments/stage-ablation/tasks/T-PR-17-result.md、experiments/stage-ablation/research/longterm-vision-survey.md、experiments/stage-ablation/research/prompt-decomposition-collision.md、experiments/stage-ablation/research/collision-snowball.md、experiments/stage-ablation/research/objective-function-priorart-SNOWBALL-T51.md、modules/D-decomp-state-machine/research/2026-11-11-idea-research.md、modules/IDEA-INDEX.md、tasks/idea53-goal/collision-final-paper-firstpass-20261125.md、research/trust-2611.10787-note.md、research/dreamcoder-lilo-stitch-collision-20261123.md、projects/AI-计算科学/D1-academic-AI/papers/*.tex（D10-D42 引用列表）。
> 来源核验闭环（2026-11-25）：① 任务书点名的 `lit-survey/IDEA-INDEX.md` 实际位于 `modules/IDEA-INDEX.md`（已覆盖）；② `tasks/idea53-goal/submission/{paper.tex,body.tex}` 是 D 本人 idea53 投稿论文（作者 Yifeng Xiao/UCAS），Related Work 为纯散文、无 \cite/\bibitem，参考文献全在 references.bib 15 条（已逐条核验全覆盖）——贡献 0 新候选；③ references.bib 15 条系统/GPU 核心源逐条比对，无遗漏。

## A. 系统/性能建模 + GPU 效率（idea53 核心交叉域）

### Samuel Williams / Andrew Waterman / David Patterson（机构 [待核验]）
- 代表工作：Roofline: Insightful Visual Performance Analysis for Multicore Architectures, CACM 2009（出处：tasks/idea53-goal/submission-staging/references.bib roofline2009，Crossref 核验 2026-11-25）
- 连接点：idea53 的 surface 判定就是 roofline 式"时间∝份额"线性归因，paper 主 claim 量化了该假设的错误率（43-56% flip）
- 合作角度（推断）：roofline 谱系的原作者，对"roofline 假设何时失效"的闭式刻画有直接兴趣
- 优先级：高 — idea53 的理论对立面即其开创的方法

### Charlene Yang / Yunsong Wang / Steven Farrell / Thorsten Kurth（机构 [待核验]）
- 代表工作：Hierarchical Roofline (arXiv:2009.05257) + Time-Based Roofline (arXiv:2009.04598)（出处：references.bib rooflineHier2020/rooflineTime2020）
- 连接点：hierarchical roofline 与 idea53 §4.5 的树状泛化（branch-level vs within-branch 分解）同构——都是把 roofline 分层
- 合作角度（推断）：他们做层级化 roofline 分解，idea53 给出层级修正量的闭式信息论度量，互为方法学互补
- 优先级：高 — 树状分解方向最直接的近邻作者

### Zhihang Yuan / Yuzhang Shang / Yang Zhou / Zhen Dong（机构 [待核验]）
- 代表工作：LLM Inference Unveiled: Survey and Roofline Model Insights (arXiv:2402.16363)（出处：references.bib rooflineLLM2024 + workshop-draft-metacog-20261122.md ref 21）
- 连接点：LLM 推理 roofline 综述，覆盖 idea53 四平台的 workload 域；idea53 的 workload prior 可与其经验分布对照
- 合作角度（推断）：把闭式瓶颈测量接到 LLM 推理 roofline 谱系，扩展其 survey 的定量深度
- 优先级：高 — LLM×roofline 交叉点作者

### Vijay Janapa Reddi（机构 [待核验]）
- 代表工作：MLSYSIM: First-Principles Infrastructure Modeling for ML Systems (arXiv:2607.02558)（出处：references.bib mlsysim2026，arXiv API 核验）
- 连接点：22-walls binding-constraint solver，闭式第一性原理瓶颈判定——idea53 碰撞核查标的同族度最高方向之一
- 合作角度（推断）：同为"闭式+第一性原理"瓶颈判定，可对比 walls 框架与 surface-vs-deep 修正量
- 优先级：高 — 闭式瓶颈判定同族

### Aaron Jarmusch / Sunita Chandrasekaran（机构 [待核验]）
- 代表工作：Microbenchmark-Driven Analytical Performance Modeling Across Modern GPU Architectures (arXiv:2605.04178)（出处：references.bib microbenchAnalytic2026）
- 连接点：B200/MI300A 跨平台解析建模（MAE 8.4%）；idea53 是纯 spec 闭式（不跑 microbenchmark），两者构成"解析+微基准"vs"纯闭式"的方法学对照
- 合作角度（推断）：用他们的 microbenchmark 数据验证 idea53 闭式预测（外部验证正是 idea53 的 Limitations 第一条）
- 优先级：高 — 可直接补 idea53 的外部验证缺口

### Sven Hepkema / Bowen Wu / Christos Kozyrakis（机构 [待核验]）
- 代表工作：Over the Memory Wall, Into the Instruction Wall (arXiv:2608.13696)（出处：references.bib memoryWallFlip2026）
- 连接点：L4→GH200 瓶颈翻转实证——与 idea53 的 flip rate（43-56%）概念相邻，他们是经验实测，idea53 是闭式预测
- 合作角度（推断）：用 idea53 闭式模型预测其观察到的瓶颈翻转，把经验发现升级为可计算量
- 优先级：高 — 瓶颈翻转方向的直接对话者

### Pol Recasens / Ferran Agullo / Yue Zhu（机构 [待核验]）
- 代表工作：Mind the Memory Gap: GPU Bottlenecks in Large-Batch LLM Inference (arXiv:2503.08311)（出处：references.bib memoryGap2025）
- 连接点：large-batch 仍 memory-bound 的反常识实证；idea53 的 workload prior 是均匀 Dirichlet，其发现正对应 prior 偏移场景
- 合作角度（推断）：用其 large-batch 工况做 idea53 非均匀 prior 的实测锚点
- 优先级：中 — 特定工况的实证锚点

### Chaitanya Poolla / Rahul Saxena（机构 [待核验]）
- 代表工作：On Extending Amdahl's Law to Learn Computer Performance (arXiv:2110.07822)（出处：references.bib amdahlExt2021）
- 连接点：Amdahl 定律扩展做性能学习——idea53 的 related work 把 Amdahl 式分解列为"rates 当给定输入"的代表
- 合作角度（推断）：把"判断本身"作为测量对象的闭式量引入 Amdahl 扩展框架
- 优先级：中 — Amdahl 谱系延伸

### Andrzej Karbowski（机构 [待核验]）
- 代表工作：Amdahl's and Gustafson-Barsis Laws Revisited (arXiv:0809.1177)（出处：references.bib amdahl2008）
- 连接点：idea53 paper §8 直接引用的 Amdahl 式分解锚点
- 合作角度（推断）：速率律视角下"判断增量"的封闭解是其框架的自然延伸
- 优先级：低 — 经典锚点，连接较间接

### Y. He（机构 [待核验]）
- 代表工作：Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration (arXiv:2611.24733)（出处：workshop-draft-metacog-20261122.md ref 6）
- 连接点：NPU 设计空间探索的机理批评器——硬件设计侧的"机制判断"，与 idea53 的微架构判断同域
- 合作角度（推断）：闭式瓶颈测量可作为其设计空间搜索的先验约束
- 优先级：中 — 硬件设计侧交叉

### SA-Scheduler 团队（TODAES 2026, DOI 10.1145/3842670；机构 [待核验]；作者本地仅存 "Zhang and Zhang and Wang and others"，全名 [待核验]）
- 代表工作：Structure-Derived Bottleneck-Aware Scheduling for Multitasking MCM-GPUs（出处：references.bib saScheduler2026，Crossref 核验）
- 连接点：kernel 结构先验→解析瓶颈模型→不跑 runtime profiling 判 regime——idea53 碰撞核查标的同族度最高近邻（用途=调度，无信息论读数）
- 合作角度（推断）：把其解析瓶颈模型升级为带信息论读数的增量贡献测量
- 优先级：高 — 同族度最高近邻（需先补全作者名单）

### AMALI 团队（ISCA'25, DOI 10.1145/3695053.3731064；机构 [待核验]；作者本地仅存 "Cao and Wu and Chen and An and others"，全名 [待核验]）
- 代表工作：AMALI: An Analytical Model for Accurately Modeling LLM Inference on Modern GPUs（出处：references.bib amali2025）
- 连接点：原文口径"GPU analytical model 帮 architect 快速精确定位瓶颈"——idea53 碰撞核查的"最难一击"引文锚点
- 合作角度（推断）：AMALI 解析模型 + idea53 增量贡献度量 = 分析模型的"判断质量"量化
- 优先级：高 — 最难一击的近邻（需先补全作者名单）

### Zeju Li / Jianyuan Zhong / Ziyang Zheng / Xiangyu Wen / Zhijian Xu / Yingying Cheng / Fan Zhang / Qiang Xu（机构 [待核验]）
- 代表工作：Making Slow Thinking Faster: Compressing LLM Chain-of-Thought via Step Entropy (arXiv:2508.03346)（出处：references.bib stepEntropy2025）
- 连接点：step 级信息论测量推理轨迹——idea53 的 H(D|S) 信息论读数与 step-entropy 同属"推理过程的信息度量"，但 idea53 是从 spec 闭式导出而非观测
- 合作角度（推断）：step-entropy（观测侧）与闭式增量贡献（推导侧）的互验
- 优先级：高 — 信息论×推理过程交叉点

### Alex Kraskov / Florian Stögbauer / Peter Grassberger（机构 [待核验]）
- 代表工作：Estimating Mutual Information, Phys Rev E 2004（出处：references.bib kraskov2004，Crossref 核验）
- 连接点：idea53 的 H(D|S) 信息论读数的 estimation 方法学锚点
- 合作角度（推断）：MI 估计方法学对闭式 MI 的有限样本校正
- 优先级：低 — 方法学锚点，连接较间接

### Colin F. Camerer / Anders Dreber / Falk Holzmeister / Kate Ho（et al.）（机构 [待核验]）
- 代表工作：Evaluating the Replicability of Social Science Experiments in Nature and Science, Nat Hum Behav 2018（出处：references.bib camerer2018）
- 连接点：预注册+多实验室复制范式先例（60+ labs）——idea53 预注册协议的惯例锚点
- 合作角度（推断）：预注册实验设计的跨域合作（idea53 的 prereg 协议可借其多实验室框架）
- 优先级：低 — 惯例锚点

## B. LLM 研究自动化 / deep research（pfb 主域）

### Jaehyun Nam / Jinsung Yoon 等（Google Cloud AI Research；出处：scientisttwo-comparison.md 头部）
- 代表工作：ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI (arXiv:2609.19644)
- 连接点：pfb 的头号对标系统（6 agent 组闭环自主科研）；scientisttwo-comparison.md 已给出互补点：pfb 的 dual-judge 可靠性检验 + 流程组件消融归因正是其缺失的两块
- 合作角度（推断）：把 pfb 的流程归因方法用于其 6 个 agent 组的消融（其自身"填补空白点"表已承认缺流程组件归因）
- 优先级：高 — 互补关系最明确的对标系统作者

### E. B. Avraham（et al.；机构 [待核验]）
- 代表工作：DREAM: Deep Research Evaluation with Agentic Metrics, ACL 2026 pp.9879-9904, DOI 10.18653/v1/2026.acl-long.448（出处：paper-draft.md ref 5 + workshop-draft-metacog-20261122.md ref 1 + competitor-survey.md）
- 连接点：DREAM 的 citation grounding 评测结论是 pfb 三道闸的动机来源；pfb 评分器已吸收 DREAM 维度
- 合作角度（推断）：pfb 的交叉验证置信度（双源印证升级）可作为 DREAM 缺的"来源可信度"维度补全
- 优先级：高 — 评测维度互补

### J. Wei / X. Wang / D. Schuurmans 等（机构 [待核验]）
- 代表工作：Chain-of-Thought Prompting (arXiv:2201.11903) + BrowseComp (arXiv:2504.12516)（出处：paper-draft.md ref 1/14）
- 连接点：CoT 是 pfb 分解树的推理基座；BrowseComp 是 pfb 边界划定用的基准（persistent retrieval 不可测维度）
- 合作角度（推断）：pfb 的 stage-ablation 归因方法可用于 CoT 类流程组件的贡献测量
- 优先级：中 — 基座方法作者，连接面广但深

### S. Yao / D. Yu / J. Zhao 等（机构 [待核验]）
- 代表工作：Tree of Thoughts (arXiv:2305.10601)（出处：paper-draft.md ref 2）
- 连接点：ToT 的树状推理与 idea53 的分解树结构同构；idea53 测"树中深层节点的增量贡献"正是 ToT 类结构缺的定量测量
- 合作角度（推断）：给 ToT 类树结构加"节点增量贡献"的信息论度量
- 优先级：中 — 树结构推理的方法学近邻

### Y. Shao / Y. Jiang / T. A. Kanell 等（机构 [待核验]）
- 代表工作：STORM (arXiv:2402.14207, NAACL 2024)（出处：paper-draft.md ref 27 + prompt-decomposition-collision.md）
- 连接点：多 persona 专家对话→大纲→正文；pfb 的 decomp 阶段对标其大纲生成
- 合作角度（推断）：decomp 前置质检模块（缺口标注+留空）可作为 STORM 流程的可选组件
- 优先级：中 — deep research 主流系统作者

### M. Du / B. Xu / C. Zhu 等（机构 [待核验]）
- 代表工作：DeepResearch Bench (arXiv:2506.11763, ICLR'26)（出处：paper-draft.md ref 28 + longterm-vision-survey.md）
- 连接点：RACE 四维评分（Comprehensiveness/Depth/Instruction/Readability）是 pfb 评分器的对标尺子
- 合作角度（推断）：pfb 的自研 5 题 stage-ablation 可作为 RACE 维度"为什么涨"的归因补充
- 优先级：中 — 基准设计方

### Y. Zheng / D. Fu / X. Hu 等（机构 [待核验]）
- 代表工作：DeepResearcher: Scaling Deep Research via RL in Real-world Environments (arXiv:2504.03160, EMNLP 2025)（出处：paper-draft.md ref 29）
- 连接点：RL 训练的 deep research agent；pfb 测的是"无训练、prompt 层流程"的贡献——两者构成训练侧 vs 流程侧的对照
- 合作角度（推断）：pfb 的流程归因可指导其 RL reward 设计（哪些流程组件值得进 reward）
- 优先级：中 — 训练侧对照

### G. Mialon / C. Fourrier / C. Swift / T. Wolf / Y. LeCun / T. Scialom（机构 [待核验]）
- 代表工作：GAIA (arXiv:2311.12983)（出处：paper-draft.md ref 7）
- 连接点：通用 AI 助手基准，pfb 的 no-tool 设置与其 tool 设置的边界对照
- 合作角度（推断）：连接较弱，仅基准边界参照
- 优先级：低 — 边界参照

### X. Liu 等（机构 [待核验]）
- 代表工作：AgentBench (arXiv:2308.03688, ICLR 2024)（出处：paper-draft.md ref 8）
- 连接点：agent 能力评测基准
- 合作角度（推断）：pfb 的机械判分层（M5 来源锚定率）可作为其评测的补充维度
- 优先级：低 — 边界参照

### O. Yoran 等（机构 [待核验]）
- 代表工作：τ-bench (arXiv:2406.12045)（出处：paper-draft.md ref 9；另见 IDEA-INDEX #49 量化消融引用 τ²-bench）
- 连接点：工具-agent-用户交互基准；#49 的量化消融在其上观察到"分数不变但过程恶化"
- 合作角度（推断）：过程质量测量（pfb 的 M 维度）与 τ-bench 终端分数的背离分析
- 优先级：低 — 边界参照

### A. Maharana 等（机构 [待核验]）
- 代表工作：LoCoMo (arXiv:2402.17753, ACL 2024)（出处：paper-draft.md ref 10）
- 连接点：长上下文对话记忆基准
- 合作角度（推断）：连接弱，仅引用列表出现
- 优先级：低 — 边界参照

### S. Zhou / F. F. Xu / H. Zhu 等（机构 [待核验]）
- 代表工作：WebArena (arXiv:2307.13854, ICLR 2024)（出处：paper-draft.md ref 11）
- 连接点：真实 web 环境 agent 基准
- 合作角度（推断）：连接弱，仅引用列表出现
- 优先级：低 — 边界参照

### C. E. Jimenez / J. Yang / A. Wettig 等（机构 [待核验]）
- 代表工作：SWE-bench (arXiv:2310.06770, ICLR 2024)（出处：paper-draft.md ref 12 + T-PR-17-result.md 多处）
- 连接点：SWE 任务基准；T-PR-17 的 handoff 近邻文献（Handoff Debt/HSC-Bench/Handoff Tax）都在 SWE-bench 上做
- 合作角度（推断）：pfb 的阶段顺序消融方法可迁移到 agent handoff 场景
- 优先级：低 — 基准参照

### J. S. Chan / N. Chowdhury / O. Jaffe 等（机构 [待核验]）
- 代表工作：MLE-bench (arXiv:2410.07095, ICLR 2025)（出处：paper-draft.md ref 13）
- 连接点：ML 工程 agent 基准
- 合作角度（推断）：连接弱，仅引用列表出现
- 优先级：低 — 边界参照

### Assaf Elovic（GitHub: assafelovic；机构 [待核验]）
- 代表工作：GPT Researcher（github.com/assafelovic/gpt-researcher，30k star，MIT）（出处：competitor-survey.md §1/§3 + 本地 clone runs/d1-gpt-researcher/README.md）
- 连接点：pfb 的 L1 工程基线（D1 判据"S5 ≥ GPT Researcher"的直接对象）；competitor-survey 已解剖其代码（无阶段门禁/无回执）
- 合作角度（推断）：把 pfb 的 gates.py 式阶段门禁作为其流水线的可选插件（其 citation grounding 弱正是 DREAM 指出的）
- 优先级：高 — pfb 直接打的对象，工程合作可行性最高

### navinsreyas（GitHub；机构 [待核验]；真名 [待核验]）
- 代表工作：research-agent（LangGraph, MIT；显式来源权威度打分：base 0.5 + authority +0.2 + freshness +0.2 + depth +0.1）（出处：competitor-survey.md §1）
- 连接点：唯一见到显式来源权威度打分的开源项目——pfb 的交叉验证置信度（双源印证）是其单源打分的升级
- 合作角度（推断）：把其启发式 scorer 升级为双源印证结构
- 优先级：中 — 来源可信度方向的直接近邻（需先确认身份）

### OPPO OpenResearcher 团队（arXiv:2603.20278, EMNLP 2026 main.42；机构 [待核验]；作者名单本地未存，[待核验]）
- 代表工作：OpenResearcher（离线语料 15M doc + 三原语合成 97K 轨迹→SFT 30B-A3B）（出处：competitor-survey.md §1）
- 连接点：训练透明的 deep research pipeline；BrowseComp-Plus 54.8%
- 合作角度（推断）：pfb 的流程归因可用于其轨迹合成的质量控制
- 优先级：中 — 训练透明 pipeline（需先补全作者名单）

### 阿里 Tongyi DeepResearch 团队（30.5B MoE；机构 [待核验]；作者名单本地未存，[待核验]）
- 代表工作：Tongyi DeepResearch（RL 长程搜索，开源权重）（出处：competitor-survey.md §1）
- 连接点：DREAM 中 CI≈1.03（几乎不做 claim 落地）——正是 pfb 三道闸要解的问题
- 合作角度（推断）：pfb 的 claim grounding 维度可作为其评测补充
- 优先级：中 — 工业级 RL deep research（需先补全作者名单）

### BATS 团队（UC Santa Barbara / Google / NYU；出处：objective-function-priorart-SNOWBALL-T51.md 条目 1，机构本地可证）
- 代表工作：Budget-Aware Tool-Use Enables Effective Agent Scaling (arXiv:2511.17006)
- 连接点：预算感知的 agent scaling——pfb 的 15-run 预算扫描与臂间 Pareto 与其同构
- 合作角度（推断）：pfb 的预算扫描数据可作其 budget-aware scaling 的流程侧数据点
- 优先级：中 — 预算 scaling 方向

### Jin et al.（机构 [待核验]）
- 代表工作：Search-R1: Training LLMs to Reason and Leverage Search Engines with RL (arXiv:2503.09516)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 5）
- 连接点：RL 训练的搜索推理——pfb 的 no-training prompt 层流程与其构成训练侧对照
- 合作角度（推断）：连接较弱，训练侧对照
- 优先级：低 — 训练侧对照

### Li et al.（DeepRetrieval；机构 [待核验]）
- 代表工作：DeepRetrieval: Hacking Real Search Engines and Retrievers with RL (arXiv:2503.00223)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 6）
- 连接点：RL 黑客化真实搜索引擎——pfb 的工具臂（S7T/S7F/S7V）的检索侧近邻
- 合作角度（推断）：连接较弱
- 优先级：低 — 检索侧对照

### Muennighoff et al.（机构 [待核验]）
- 代表工作：s1: Simple test-time scaling (arXiv:2501.19393)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 8）
- 连接点：test-time scaling 简化版——pfb 臂间复杂度递增的 scaling 参照
- 合作角度（推断）：连接较弱
- 优先级：低 — scaling 参照

### Li et al.（Budget Guidance；机构 [待核验]）
- 代表工作：Steering LLM Thinking with Budget Guidance (arXiv:2506.13752)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 9）
- 连接点：预算引导推理——与 TALE 同族的预算注入方向
- 合作角度（推断）：pfb 的树结构目标函数 vs 标量预算引导
- 优先级：低 — 预算注入方向

### Yang et al.（OPRO；机构 [待核验]）
- 代表工作：Large Language Models as Optimizers (arXiv:2309.03409)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 10）
- 连接点：LLM 当优化器——pfb 的"目标函数写进 prompt"的对照（优化对象不同）
- 合作角度（推断）：连接较弱
- 优先级：低 — 优化器参照

### Kwon et al.（机构 [待核验]）
- 代表工作：Reward Design with Language Models (arXiv:2303.00001, ICLR'23)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 12）
- 连接点：LLM 设计 reward——pfb S_α 闭式目标函数的生成式对照
- 合作角度（推断）：连接较弱
- 优先级：低 — reward 设计参照

### Ortiz et al.（机构 [待核验]）
- 代表工作：Tree of Problems (arXiv:2410.06634)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 16）
- 连接点：显式 breadth×depth 分解树（collision 核查采纳的近邻）——与 pfb 分解树结构同构
- 合作角度（推断）：给 Tree of Problems 加"节点增量贡献"的信息论度量
- 优先级：中 — 分解树方向直接近邻

### Zhang et al.（TRQA；机构 [待核验]）
- 代表工作：Tree-of-Reasoning Question Decomposition (AAAI'24, DOI 10.1609/aaai.v38i17.29928)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 17）
- 连接点：问题分解树 QA——pfb 分解树的 QA 侧近邻
- 合作角度（推断）：连接较弱
- 优先级：低 — 分解树参照

### Press et al.（机构 [待核验]）
- 代表工作：Self-Ask (arXiv:2210.03350)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 19）
- 连接点：组合性 gap 的分解测量——pfb M4 缺口识别维度的方法学参照
- 合作角度（推断）：连接较弱
- 优先级：低 — 组合性参照

### Trivedi et al.（机构 [待核验]）
- 代表工作：IRCoT (arXiv:2212.10509, ACL'23)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 20）
- 连接点：检索与 CoT 交错——pfb 工具臂 S7 系列的近邻
- 合作角度（推断）：连接较弱
- 优先级：低 — 检索交错参照

### Khot et al.（机构 [待核验]）
- 代表工作：Decomposed Prompting (arXiv:2210.02406)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 21）
- 连接点：模块化分解 prompt——pfb decomp 阶段的早期先例
- 合作角度（推断）：连接较弱
- 优先级：低 — 分解 prompt 参照

### Jeong et al.（机构 [待核验]）
- 代表工作：Adaptive-RAG (arXiv:2403.14403, NAACL'24)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 24）
- 连接点：按问题复杂度自适应检索策略——pfb 的"按题型适配 prompt 风格"结论与其同方向
- 合作角度（推断）：pfb 的臂间题型分析可作其自适应策略的判据
- 优先级：中 — 复杂度自适应方向

### Asai et al.（机构 [待核验]）
- 代表工作：Self-RAG (arXiv:2310.11511)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 25）
- 连接点：自反思检索生成——pfb S7V（draft-then-verify）的训练侧对照
- 合作角度（推断）：连接较弱
- 优先级：低 — 自反思参照

### Jiang et al.（FLARE；机构 [待核验]）
- 代表工作：Active Retrieval Augmented Generation (arXiv:2305.06983, EMNLP'23)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 26）
- 连接点：主动检索——pfb 工具臂的检索触发机制参照
- 合作角度（推断）：连接较弱
- 优先级：低 — 主动检索参照

### Jha et al.（机构 [待核验]）
- 代表工作：Fundamental Limits of Prompt Compression: A Rate-Distortion Approach (arXiv:2407.15504, NeurIPS'24)（出处：objective-function-priorart-SNOWBALL-T51.md 条目 30 + longterm-vision-survey.md §6）
- 连接点：prompt 压缩的率失真极限——pfb #32（压缩即智能）与 idea53 信息论读数的理论锚点
- 合作角度（推断）：率失真框架下"分解树压缩"的形式化
- 优先级：中 — 压缩理论锚点

### Ellis / Wong / Nye / Tenenbaum 等（机构 [待核验]）
- 代表工作：DreamCoder (arXiv:2006.08381)（出处：dreamcoder-lilo-stitch-collision-20261123.md）
- 连接点：程序合成库学习——pfb 的"分解树=库"类比（#54 claim 库）的方法学参照
- 合作角度（推断）：连接较弱
- 优先级：低 — 库学习参照

### Bowers / Olausson / Wong / Grand / Tenenbaum / Ellis / Solar-Lezama（机构 [待核验]）
- 代表工作：STITCH: Top-Down Synthesis for Library Learning (arXiv:2211.16605)（出处：dreamcoder-lilo-stitch-collision-20261123.md）
- 连接点：语料引导的 top-down 库合成——pfb #54（claim 库复用）的压缩器本体参照
- 合作角度（推断）：连接较弱
- 优先级：低 — 库合成参照

### D. Zhou / N. Schärli / L. Hou 等（机构 [待核验]）
- 代表工作：Least-to-Most Prompting (arXiv:2205.10625, ICLR 2023)（出处：paper-draft.md ref 16）
- 连接点：逐步分解链是 pfb 分解树的最早 prompt 形态；pfb 测"分解深度/宽度的增量贡献"正是 L2M 缺的定量层
- 合作角度（推断）：把 L2M 的分解步数升级为带闭式边际贡献的结构目标
- 优先级：中 — 分解谱系锚点

### L. Wang / W. Xu / Y. Lan 等（机构 [待核验]）
- 代表工作：Plan-and-Solve Prompting (arXiv:2305.04091, ACL 2023)（出处：paper-draft.md ref 17）
- 连接点：显式"先生成计划再执行"两阶段——pfb 的 decompose→research 两阶段同构
- 合作角度（推断）：pfb 的 stage-ablation 归因可量化其 plan 阶段的增量贡献
- 优先级：中 — 两阶段分解近邻

### S. Schulhoff / M. Ilie / N. Balepur 等（机构 [待核验]）
- 代表工作：The Prompt Report: A Systematic Survey of Prompt Engineering Techniques (arXiv:2406.06608)（出处：paper-draft.md ref 18）
- 连接点：prompt 工程技术分类学——pfb 的 prompt-stage 消融落在该分类学的可测维度上
- 合作角度（推断）：用 pfb 的消融方法学给其分类学补"各技术增量贡献"的定量列
- 优先级：中 — 分类学宿主

### K. Tian / E. Mitchell / A. Zhou 等（机构 [待核验]）
- 代表工作：Just Ask for Calibration (arXiv:2305.14975, EMNLP 2023)（出处：paper-draft.md ref 20）
- 连接点：校准置信度 elicitation——pfb 的 judge 置信度/verbalized confidence 测量同域
- 合作角度（推断）：其校准策略可作 pfb judge 置信度校准的对照基线
- 优先级：中 — 校准方向

## C. 推理过程测量 / 元认知 / 统计保证（pfb 测量层交叉域）

### J.-F. Ton（et al.；机构 [待核验]）
- 代表工作：Understanding Chain-of-Thought in LLMs through Information Theory (arXiv:2411.11984, ICML 2025)（出处：workshop-draft-metacog-20261122.md ref 17 + IDEA-INDEX #53）
- 连接点：step 级 IG（信息增益）测量 CoT——idea53 的强近邻之一（IDEA-review 标的"2411.11984 ICML2025 step级IG"）；idea53 把 step 级 IG 推广为闭式+预注册的增量贡献测量
- 合作角度（推断）：观测侧 step-IG 与闭式增量贡献的互验；深度梯度实证是其未覆盖的
- 优先级：高 — idea53 信息论测量的最直接近邻

### A. Panickssery（et al.；机构 [待核验]）
- 代表工作：LLM Evaluators Recognize and Favor Their Own Generations (arXiv:2404.13076)（出处：workshop-draft-metacog-20261122.md ref 12 + metacognition-rsi-survey-20261122.md）
- 连接点：judge self-preference bias——pfb 的核心科学发现"judge identity 翻转结论"（同族 +0.129 vs 异族 -0.187）是该 bias 的结构性实例
- 合作角度（推断）：pfb 的 dual-judge（同族+异族）设计可作为其 bias 测量的流程化方案
- 优先级：高 — judge 可靠性方向的直接对话者

### J. Yang（et al.；机构 [待核验]）
- 代表工作：Quantifying and Mitigating Self-Preference Bias of LLM Judges (arXiv:2604.22891)（出处：workshop-draft-metacog-20261122.md ref 19）
- 连接点：20 模型规模的 self-preference 量化——pfb 的 judge identity 发现与其同域
- 合作角度（推断）：pfb 的异族 judge 对照可作为其 mitigation 方案的验证场景
- 优先级：中 — self-preference 量化方向

### J. Pombal（et al.；机构 [待核验]）
- 代表工作：Self-Preference Bias in Rubric-Based Evaluation of LLMs (arXiv:2604.06996)（出处：workshop-draft-metacog-20261122.md ref 13）
- 连接点：rubric 判分下的 self-preference 持续存在——pfb 的机械判分层（无 LLM in the loop）是结构性免疫方案
- 合作角度（推断）：机械判分层 vs rubric 判分的 bias 对照
- 优先级：中 — rubric 评测 bias 方向

### F. Scholten（et al.；机构 [待核验]）
- 代表工作：Metacognitive Myopia in Large Language Models (arXiv:2408.05568)（出处：workshop-draft-metacog-20261122.md ref 14）
- 连接点：LLM 元认知近视——pfb 的 metacog 轴（workshop 稿）与其同域
- 合作角度（推断）：pfb 的 [待核验] 脚手架实验（#51）可测"脚手架移除后自发监控还剩多少"
- 优先级：中 — 元认知方向

### H. Tamoyan（et al.；机构 [待核验]）
- 代表工作：Factual Self-Awareness in Language Models (arXiv:2505.21399)（出处：workshop-draft-metacog-20261122.md ref 16）
- 连接点：事实自我意识的表征与 scaling——pfb 的 M5 来源锚定率是其行为侧测量
- 合作角度（推断）：表征侧（probing）与行为侧（锚定率）的自我意识对照
- 优先级：低 — 同域但连接较远

### X. Bai（et al.；机构 [待核验]）
- 代表工作：Know Thyself? On the Incapability and Implications of AI Self-Recognition (arXiv:2510.03399)（出处：workshop-draft-metacog-20261122.md ref 2）
- 连接点：self-recognition 接近 chance——pfb 的 judge 同族/异族设计正是绕开 self-recognition 的方案
- 合作角度（推断）：连接较弱，仅 bias 文献链一环
- 优先级：低 — bias 文献链

### Y. Yao（et al.；机构 [待核验]）
- 代表工作：Dr. Bench: A Multidimensional Evaluation for Deep Research Agents (arXiv:2510.02190)（出处：workshop-draft-metacog-20261122.md ref 20）
- 连接点：deep research 多维评测——与 DREAM/RACE 并列的第三把尺子
- 合作角度（推断）：pfb 的流程归因维度可作为其多维评测的补充
- 优先级：中 — 评测维度互补

### Zihe Gao / Zhengling Qi / Yifan Cui（浙江大学 / 乔治华盛顿大学；出处：research/trust-2611.10787-note.md §0）
- 代表工作：Trustworthy Recursive Self-Improvement with Statistical Guarantees (arXiv:2611.10787)
- 连接点：RSI 门控的统计保证（e-value + FER 预算）——pfb 的 stage 门禁（gates.py）是其"接受哪个流程改动"问题的无统计保证版；pfb 预注册+held-out 正是其验证池思想的简化
- 合作角度（推断）：把 TRUST 的 e-value 门控引入 pfb 的阶段推进（gate 从规则判分升级为统计保证）
- 优先级：高 — 统计保证×流程门控交叉，机构本地可证

### B. Estermann / R. Wattenhofer（机构 [待核验]——本地仅存姓氏）
- 代表工作：Reasoning Effort and Problem Complexity: A Scaling Analysis in LLMs (arXiv:2503.15113)（出处：workshop-draft-metacog-20261122.md ref 3）
- 连接点：推理努力×问题复杂度的 scaling——pfb 的 6 臂复杂度递增设计与其同构
- 合作角度（推断）：pfb 的臂间增量数据可作其 scaling 分析的流程侧补充
- 优先级：中 — 复杂度 scaling 方向

### R. Ganz / M. Shpigel Nacson / A. Kalyanpur / R. Litman（机构 [待核验]）
- 代表工作：The Handoff Tax (arXiv:2608.24358)（出处：workshop-draft-metacog-20261122.md ref 4 + T-PR-17-result.md）
- 连接点：T-PR-17 标的 C2 强同构近邻（conf 0.80）——agent 交接的信息损耗，与 pfb 阶段间信息传递同构
- 合作角度（推断）：pfb 的 checkpoint 设计（#50 路径依赖实验）与其 handoff 测量互补
- 优先级：中 — T-PR-17 强同构近邻

### D. KC / A. Budathoki（机构 [待核验]）
- 代表工作：Handoff Debt (arXiv:2606.02875, EMNLP 2026)（出处：workshop-draft-metacog-20261122.md ref 9 + T-PR-17-result.md）
- 连接点：coding agent 接手中断任务的 rediscovery 成本——pfb 的"每 run 独立重新发现"（rep 间 claim 重叠仅 4.7%）是其同现象
- 合作角度（推断）：claim 库（#54 应用 A）作为 handoff debt 的缓解机制
- 优先级：中 — handoff 方向

### W. Li / G. Li / D. Li / K. Maeda / T. Ogawa / M. Haseyama（机构 [待核验]）
- 代表工作：Benchmarking Task Takeover Across Agent Handoffs / HSC-Bench (arXiv:2610.36523)（出处：workshop-draft-metacog-20261122.md ref 10 + T-PR-17-result.md）
- 连接点：1039 任务固定 checkpoint 的接手表现——与 T-PR-17 的同 checkpoint 设计同构
- 合作角度（推断）：pfb 的阶段序列消融可迁移到其 receiver 条件设计
- 优先级：低 — handoff 基准

### A. B. Lorup（机构 [待核验]）
- 代表工作：Stage-Replay Divergence Follows the KV Cache (arXiv:2607.28495)（出处：workshop-draft-metacog-20261122.md ref 11）
- 连接点：KV cache 精度控制与 stage replay——pfb 的 checkpoint-as-cache 实验（Idea 2）与其同域
- 合作角度（推断）：KV cache 精度对 stage 重放的影响与 pfb 臂间一致性对照
- 优先级：低 — KV cache 方向

### C. Snell / J. Lee / K. Xu / A. Kumar（机构 [待核验]）
- 代表工作：Scaling LLM Test-Time Compute Optimally (arXiv:2408.03314)（出处：workshop-draft-metacog-20261122.md ref 15）
- 连接点：test-time compute scaling——pfb 的 15-run 预算扫描与其同构
- 合作角度（推断）：pfb 的预算扫描数据可作其 test-time scaling 的流程侧数据点
- 优先级：低 — 预算 scaling 方向

### Marom（单名；机构 [待核验]）
- 代表工作：UtilityMax Prompting (arXiv:2603.11583)（出处：longterm-vision-survey.md §2 + prompt-decomposition-collision.md）
- 连接点：把效用函数写进 prompt 令 LLM 显式分量推理——pfb 的 #30（prompt 显式目标函数驱动 hack）与其同机制
- 合作角度（推断）：其 prompt-form 消融范式可直接借给 pfb S_α 实验（survey 已判"不同构但范式可借"）
- 优先级：中 — prompt 目标函数方向（需补全全名）

### Han et al.（机构 [待核验]）
- 代表工作：TALE (arXiv:2412.18547, ACL'25 Findings)（出处：longterm-vision-survey.md §2）
- 连接点：token 预算写进 prompt + 模型自估预算——pfb 的 #36/#37 终点目标函数（U(T)=C·A·S−λ·cost）与其预算注入同构
- 合作角度（推断）：pfb 的树结构目标函数 vs TALE 的标量预算——结构化的预算注入
- 优先级：中 — 预算注入方向（需补全作者名单）

### Y. Du（et al.；机构 [待核验]）
- 代表工作：DeepResearch Bench RACE/FACT 方法（arXiv:2506.11763 同文，此处按 survey 署名口径）——与 B 节 M. Du 为同一工作的不同署名位置，合并计 1 人
- 连接点：同 B 节 DeepResearch Bench
- 合作角度（推断）：同 B 节
- 优先级：中 — 与 B 节合并

### M. Xiong / Z. Hu / X. He 等（机构 [待核验]）
- 代表工作：Can LLMs Express Their Uncertainty? (arXiv:2306.13063, ICLR 2024)（出处：paper-draft.md ref 3）
- 连接点：置信度 elicitation 实证评测——pfb 的 verbalized confidence 测量同域
- 合作角度（推断）：其 elicitation 策略矩阵可作 pfb judge 置信度采集的对照设计
- 优先级：中 — 不确定性测量方向

### S. Kadavath / T. Conerly / A. Askell 等（机构 [待核验]）
- 代表工作：Language Models (Mostly) Know What They Know (arXiv:2207.05221)（出处：paper-draft.md ref 4 + L49；stages/02/research.md 核验 E2）
- 连接点：paper-draft.md L49 将其与 Xiong 并列引用于"LLMs 普遍过度自信"——pfb 的 M2 置信度测量正针对该过度自信问题
- 合作角度（推断）：其自评置信度方向与 pfb 的 M2 同域，可作 pfb 置信度测量的对照基线
- 优先级：中 — 过度自信/自评置信度方向

### S. Lin / J. Hilton / O. Evans（机构 [待核验]）
- 代表工作：Teaching Models to Express Their Uncertainty in Words (arXiv:2205.14334, TMLR 2022)（出处：paper-draft.md ref 19）
- 连接点：verbalized uncertainty 的奠基工作——pfb 的 verbalized confidence 直接继承该范式
- 合作角度（推断）：pfb 的 stage 级置信度分解是其"整句置信度"的细粒度延伸
- 优先级：中 — 范式源头

### L. Kuhn / Y. Gal / S. Farquhar（机构 [待核验]）
- 代表工作：Semantic Uncertainty (arXiv:2302.09664, ICLR 2023 Spotlight)（出处：paper-draft.md ref 21）
- 连接点：语义不变性下的不确定性估计——pfb 的"同义改写鲁棒性"检验同思路
- 合作角度（推断）：语义聚类置信度可作 pfb judge verdict 方差分析的补充维度
- 优先级：低 — 方法学相邻

### L. Meyer / S. Rossi / W. Chen / T. Laurent / Y. Li（机构 [待核验]）
- 代表工作：An Analysis of Training-Free Self-Reported Confidence in Language Models (arXiv:2609.20541)（出处：paper-draft.md ref 22 + L51；stages/02/research.md N20）
- 连接点：本地口径（N20）= 同批 TriviaQA 上对比 verbalized / P(True) / 3-sample agreement 三信号：verbalized 最强（AUROC 0.956/0.937）、三样本一致性明显更弱（0.765/0.790），且 3 次采样放大共有误解——直接解释 pfb M2 在 S6 跳到 0.618 而 S0 仅 0.037
- 合作角度（推断）：其三信号对比框架可作 pfb 置信度信号选择的对照设计
- 优先级：中 — 自评置信度同域

### Y. Xu / A. Wang / J. Ren 等（机构 [待核验]）
- 代表工作：When Words Fall Short: Iterative Synergy Between Verbalized Reasoning and Hidden Features for LLM Confidence Estimation (arXiv:2609.34454)（出处：paper-draft.md ref 23 + L51；stages/02/research.md N21）
- 连接点：本地口径（N21）= 反方证据：内置 confidence estimator 可显著优于 verbalized confidence；paper-draft.md L51 引其"post-retrieval evidence confidence 优于 post-answer verbalized"——pfb 的 M2 是 verbalized 路线，该结论直接约束 pfb 置信度读数的上界
- 合作角度（推断）：其"语言置信度非上界"结论可作为 pfb M2 提升归因（prompt 层效应 vs 内部读出）的对照
- 优先级：中 — verbalized 置信度上界的反方证据

### S. Es / J. James / L. Espinosa-Anke / S. Schockaert（机构 [待核验]）
- 代表工作：RAGAs (arXiv:2309.15217, EACL 2024 Demo)（出处：paper-draft.md ref 24）
- 连接点：RAG 自动评测框架——pfb 的 citation-grounding 门（gate 2）与其 faithfulness 指标同域
- 合作角度（推断）：RAGAs 指标可作 pfb 三门中引用门的交叉验证
- 优先级：中 — 引用门交叉验证

### J. Saad-Falcon / O. Khattab / C. Potts / M. Zaharia（机构 [待核验]）
- 代表工作：ARES (arXiv:2311.09476, NAACL 2024)（出处：paper-draft.md ref 25；stages/02/research.md N13）
- 连接点：本地口径（N13）= 用合成训练数据微调轻量 judge + PPI 校正，是"用 LLM 当评测器但要纠偏"的范式——与 pfb 的 dual-judge 可靠性同题
- 合作角度（推断）：其 PPI 校正方法可迁移到 pfb 的 judge 可靠性纠偏
- 优先级：中 — judge 校准同域

### D. Ru / L. Qiu / X. Hu 等（机构 [待核验]）
- 代表工作：RAGChecker (arXiv:2408.08067, NeurIPS 2024 D&B)（出处：paper-draft.md ref 26；stages/02/research.md N14）
- 连接点：本地口径（N14）= 把检索与生成分开诊断的细粒度指标（claim-level precision/recall）——与 pfb S7V 的 claim-level 验证同构
- 合作角度（推断）：其 claim-level 指标可作 pfb S7V 验证的对照坐标系
- 优先级：低 — 诊断维度相邻



### R. Meyes / M. Lu / C. Waubert de Puiseau / T. Meisen（机构 [待核验]）
- 代表工作：Ablation Studies in Artificial Neural Networks (arXiv:1901.08644)（出处：paper-draft.md ref 30）
- 连接点：消融方法学综述——pfb 的 stage-ablation 是其"组件贡献测量"在 agent 流水线的迁移
- 合作角度（推断）：其消融分类学可作 pfb stage-ablation 的方法学定位参照
- 优先级：低 — 方法学参照

### E. Miller（机构 [待核验]）
- 代表工作：Adding Error Bars to Evals: A Statistical Approach to LM Evaluations (arXiv:2411.00640)（出处：paper-draft.md ref 31；modules/F-theory/research/interpretability/literature-survey.md 条目 3-7）
- 连接点：本地口径 = 聚类 SE 可比朴素 SE 大 3 倍以上、比较两配置必须做 item-level 配对差、给出功效公式（δ、α、β→n）——pfb 的 n=5 功效限制与 ±0.10 噪声地板正是其问题域
- 合作角度（推断）：其功效公式可直接算出 pfb 各 arm 效应所需最小 n，配对差方法可重做 pfb 的 S1→S5 比较
- 优先级：高 — pfb 统计层最直接的方法学供给者

### C. Park / J. Yoon / S. Han / H. Moon / H. Lim（机构 [待核验]）
- 代表工作：AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop QA over Scientific Citation Graphs (arXiv:2609.34428, NeurIPS 2026 E&D)（出处：paper-draft.md ref 32）
- 连接点：多跳引用图诊断基准——pfb 的 citation-grounding 门同域
- 合作角度（推断）：pfb 的引用门可在其基准上做多跳扩展测试
- 优先级：低 — 基准同域

### G. Dominici / T. McMillan / F. Barez / M. Langheinrich / M. Gjoreski（机构 [待核验]）
- 代表工作：CausalCoT: Mitigating Attention Leakage via Context Isolation (arXiv:2610.31639)（出处：paper-draft.md ref 33）
- 连接点：CoT 中注意力泄漏的因果隔离——pfb 的 stage 隔离（context isolation）同思路
- 合作角度（推断）：其隔离机制可作 pfb stage 边界设计的对照
- 优先级：低 — 隔离机制相邻

### I. Khan / T. V. Nguyen / Y. Xia 等（机构 [待核验]）
- 代表工作：Role-Enhanced Zero-Shot CoT: A Large-Scale Evaluation (arXiv:2610.29073)（出处：paper-draft.md ref 34）
- 连接点：role 增强 CoT 的大规模评测——pfb 的 prompt-stage 消融同方法学
- 合作角度（推断）：pfb 的消融归因可量化其 role 组件的增量贡献
- 优先级：低 — 评测方法学相邻

### K. C. Ayyagari（机构 [待核验]）
- 代表工作：Pinned and Still Unstable: Within-Judge Verdict Variance and the Noise Floor of LLM-as-Judge Leaderboards (arXiv:2609.33044)（出处：paper-draft.md ref 35）
- 连接点：judge 内部 verdict 方差与噪声地板——与 pfb 的 ±0.10 噪声地板测量直接同题
- 合作角度（推断）：pfb 的 45-run 重打分数据可作其噪声地板模型的独立验证
- 优先级：高 — judge 噪声地板同题作者

### S. Chae / M. Kim / D. Jung / S. Choi / S. Jung（机构 [待核验]）
- 代表工作：Self- and Other-Labels Induce Bidirectional Bias in LLM Judges (arXiv:2608.18091, Findings EMNLP 2026)（出处：paper-draft.md ref 36）
- 连接点：judge 双向偏差——pfb 的 same-family judge self-preference 风险同域
- 合作角度（推断）：其偏差方向分析可并入 pfb 的 judge 可靠性诊断
- 优先级：中 — judge 偏差同域

### V. Kumar / D. Rathore / A. Moitra（机构 [待核验]）
- 代表工作：All Verdicts are Not Equal: Rethinking LLM Judge Reliability (arXiv:2610.12083, AACL-IJCNLP 2026)（出处：paper-draft.md ref 37）
- 连接点：judge 可靠性重思——pfb 的 dual-judge 可靠性是同一问题的实证侧
- 合作角度（推断）：pfb 的异族 judge 对照可作其可靠性框架的验证场景
- 优先级：高 — judge 可靠性同题

### Y. Yin / J. Wu / A. Kumar / S. Novotney / D. Liu / E. Babinsky（机构 [待核验]）
- 代表工作：The Judge Can Debias Itself (arXiv:2610.24320)（出处：paper-draft.md ref 38）
- 连接点：judge 自去偏——pfb 的 judge 偏差测量是其去偏的前置
- 合作角度（推断）：pfb 的偏差量化可作其自去偏效果的度量
- 优先级：中 — 去偏前置测量

### V. Polshkov / M. Pitera / J. Yang 等（机构 [待核验]）
- 代表工作：WANDR: A Benchmark for Wide and Deep Research (arXiv:2608.14747)（出处：paper-draft.md ref 39）
- 连接点："wide and deep" 研究基准——pfb 的分解树"深×广"目标函数正对应其两维
- 合作角度（推断）：S_α 的 n·ln kₙ 结构效用可直接用作 WANDR 类任务的生成目标
- 优先级：中 — 深广两维同构

### Y.-C. Hsiao（机构 [待核验]）
- 代表工作：Rethinking Verbalized Confidence for LLM-as-a-Judge (arXiv:2609.10996)（出处：paper-draft.md ref 40）
- 连接点：judge 的 verbalized confidence 兼容性漂移——pfb 的 judge 置信度测量同域
- 合作角度（推断）：其兼容性分析可解释 pfb 跨 judge 的置信度漂移
- 优先级：低 — 置信度细节

### D. Ghosh / S. Kumar / A. Garg（机构 [待核验]）
- 代表工作：Confidence Signal Validity in LLMs (arXiv:2610.25846)（出处：paper-draft.md ref 41）
- 连接点：置信度信号效度——pfb 的 judge 置信度效度检验同题
- 合作角度（推断）：其效度指标可作 pfb judge 置信度的验证标准
- 优先级：低 — 效度细节

### N. Schwager / S. Münker / A. Plum / A. Rettinger（机构 [待核验]）
- 代表工作：Token Probabilities as Confidence Estimators: A Calibration Study (arXiv:2611.07735, WNUT 2026)（出处：paper-draft.md ref 42 + L51）
- 连接点：本地口径（L51）= open-weight logprobs 随规模退化（ECE 0.20→0.006 需微调）——pfb 的 M2 走 verbalized 路线，该结论支持 pfb 不依赖 logprob 通道的选择
- 合作角度（推断）：其 logprob 退化结论可作 pfb 坚持 verbalized 路线的依据佐证
- 优先级：低 — 校准细节

## D. 目标函数 / reward / 压缩（pfb 理论层交叉域）

### Ng / Harada / Russell（机构 [待核验]）
- 代表工作：Policy Invariance Under Reward Transformations, ICML 1999（出处：longterm-vision-survey.md §6）
- 连接点：PBRS 策略不变性定理——pfb #32（压缩即智能当分解目标函数）的理论锚点之一
- 合作角度（推断）：连接弱，经典锚点
- 优先级：低 — 经典锚点

### Ma et al.（NVIDIA/UPenn；出处：longterm-vision-survey.md §L1）
- 代表工作：Eureka (arXiv:2310.12931, ICLR'24)（出处：longterm-vision-survey.md）
- 连接点：LLM 写可执行 reward 代码——pfb 的 S_α 闭式目标函数是其"手写版"
- 合作角度（推断）：pfb 的闭式目标函数 vs Eureka 的生成式 reward——可解释性对照
- 优先级：低 — reward 生成方向

### Faldor / Zhang / Cully / Clune（机构 [待核验]；出处：longterm-vision-survey.md §L3）
- 代表工作：OMNI-EPIC (arXiv:2405.15568, ICLR'25)（出处：longterm-vision-survey.md）
- 连接点：基础模型生成环境+reward 函数——pfb 的"目标函数与环境共同生成"是其近邻
- 合作角度（推断）：连接较弱，AI-Generating-Algorithms 路线参照
- 优先级：低 — 环境生成方向

### Yang et al.（NeurIPS'19；机构 [待核验]）
- 代表工作：Envelope MOQ-Learning (arXiv:1908.08342)（出处：longterm-vision-survey.md §5）
- 连接点：偏好向量条件的全 Pareto 空间学习——pfb #5（top-k 探针）与预算 Pareto 的理论参照
- 合作角度（推断）：连接较弱，Pareto 理论锚点
- 优先级：低 — Pareto 理论锚点

### Chen et al.（NeurIPS'21；机构 [待核验]）
- 代表工作：Decision Transformer (arXiv:2106.01345)（出处：longterm-vision-survey.md §5）
- 连接点：return-conditioned 序列建模——pfb 的"把期望结果写进条件"的零训练类比
- 合作角度（推断）：连接较弱，条件控制参照
- 优先级：低 — 条件控制参照

### Gunjal et al.（机构 [待核验]）
- 代表工作：Rubrics as Rewards (arXiv:2507.17746)（出处：longterm-vision-survey.md §3）
- 连接点：实例级 rubric 转 reward 进 GRPO——pfb S_α 的"自然语言版 reward"近邻（survey 判 Q3 窗口在收窄）
- 合作角度（推断）：S_α 闭式函数 vs rubric 加权和——可解释性对照
- 优先级：中 — rubric-as-reward 方向（窗口收窄中）

### Huang et al.（机构 [待核验]）
- 代表工作：RL with Rubric Anchors (arXiv:2508.12790)（出处：longterm-vision-survey.md §3）
- 连接点：~10K rubric 数据集+Rubicon 框架
- 合作角度（推断）：连接较弱，rubric 数据参照
- 优先级：低 — rubric 数据参照

### Viswanathan et al.（机构 [待核验]）
- 代表工作：Checklists are Better than Reward Models (arXiv:2507.18624)（出处：longterm-vision-survey.md §3）
- 连接点：checklist 替代 reward model——pfb 的机械判分层（无 LLM）与其同精神
- 合作角度（推断）：机械判分层 vs checklist 的 bias 对照
- 优先级：低 — checklist 方向

### Estevez-Velarde / Piad-Morffis et al.（COLING'20；机构 [待核验]）
- 代表工作：AutoGOAL（ACL Anthology 2020.coling-main.317）（出处：longterm-vision-survey.md §L5）
- 连接点：概率文法进化搜索 ML 管线（目标函数由用户给）——pfb 的"目标函数本身可学习"是其 gap
- 合作角度（推断）：连接较弱，管线搜索参照
- 优先级：低 — 管线搜索参照

### Xie et al.（机构 [待核验]；全名本地未存）
- 代表工作：Text2Reward (arXiv:2309.11489, ICLR'24)（出处：longterm-vision-survey.md §L1）
- 连接点：NL 目标→稠密 shaped reward 程序——"从任务描述自动推导目标函数"的原型之一
- 合作角度（推断）：pfb 的闭式结构目标函数（S_α）可作其 reward 程序的结构性约束
- 优先级：中 — 目标函数自动生成谱系

### AhmadiTeshnizi et al.（机构 [待核验]；全名本地未存）
- 代表工作：OptiMUS / OptiMUS-0.3 (arXiv:2310.06116 / 2407.19633)（出处：longterm-vision-survey.md §L1/§5）
- 连接点：LLM 生成优化目标函数 + 求解器闭环验证——"目标函数自动生成+真值闭环"原型
- 合作角度（推断）：pfb 的独立 judge 覆盖率机制可作其求解器闭环的推理管线对应物
- 优先级：中 — 目标函数闭环验证

### λ-RLM（Y-Combinator for LLMs）团队（arXiv:2603.20105；机构 [待核验]；作者名单本地未存）
- 代表工作：受限运行时 Split/Map/Reduce 组合子递归分解，结构参数 (k\*, τ\*, d) 显式化（出处：longterm-vision-survey.md §3 条目 3）
- 连接点：survey 判"半同构（最接近的工程形态）"——深广参数显式可解析但由外部 planner 注入
- 合作角度（推断）：把其外部 planner 计算注入的结构参数换成模型可读的闭式目标函数（S_α 用法）
- 优先级：中 — 最接近工程形态，结构参数同构

### IBC/VOI 推理时预算控制团队（arXiv:2605.05701；机构 [待核验]；作者名单本地未存）
- 代表工作：运行时按"单位预算边际任务价值"在检索/分解/提交间选点（出处：longterm-vision-survey.md §3 条目 5）
- 连接点：边际思想与 S_α 的 Δ=ln((kₙ+1)/kₙ) 同源——外部启发式打分 vs prompt 内闭式公式
- 合作角度（推断）：用闭式边际公式替换其 critic 值变化启发式，做消融对照
- 优先级：中 — 边际价值同源

### AMFT 团队（arXiv:2508.06944；机构 [待核验]；作者名单本地未存）
- 代表工作：把 SFT/RL 平衡权重 μ 当可学习参数做元梯度优化（出处：longterm-vision-survey.md §5 条目 5）
- 连接点："α 类权衡参数可被元学习"的直接存在性证明（pfb Q4/G7 关键证据）
- 合作角度（推断）：pfb 的 α 在线调节 + 其元梯度路径 = 双层可辨识性的接合点
- 优先级：中 — α 元学习存在性证明

## E. 信息论 / 压缩理论锚点（D1-academic-AI 引用列表）

### N. Tishby / N. Zaslavsky（机构 [待核验]）
- 代表工作：Exploring deep neural networks via the information bottleneck (arXiv:1511.06071)（出处：projects/AI-计算科学/D1-academic-AI/papers/d32-info-theoretic-phase-transition/arxiv-source/d32-info-theoretic.tex thebibliography）
- 连接点：information bottleneck 原理——idea53 的 H(D|S) 分解与 IB 的压缩-预测权衡同构
- 合作角度（推断）：IB 视角下"深层判断的增量信息"的形式化
- 优先级：中 — 信息论方法学锚点

### R. Shwartz-Ziv / N. Tishby（机构 [待核验]）
- 代表工作：Opening the black box (ICML 2017)（出处：同上 d32 tex）
- 连接点：IB 的经验验证——idea53 的"从 spec 闭式导出"是其"从数据拟合"的对偶
- 合作角度（推断）：连接较弱，IB 经验侧参照
- 优先级：低 — IB 经验侧

### A. Saxe / J. McClelland / S. Ganguli（机构 [待核验]）
- 代表工作：Information bottleneck in deep learning (NeurIPS 2021)（出处：同上 d32 tex）
- 连接点：IB 在深度学习中的角色
- 合作角度（推断）：连接较弱
- 优先级：低 — IB 参照

### E. Weng（机构 [待核验]）
- 代表工作：Mutual information bounds on neural network generalization (arXiv:2004.09080)（出处：同上 d32 tex）
- 连接点：MI 界——idea53 的 MI 读数的界参照
- 合作角度（推断）：连接较弱
- 优先级：低 — MI 界参照

### J. Kaplan / S. McCandlish / T. Henighan / T. B. Brown（机构 [待核验]）
- 代表工作：Scaling laws for neural language models (arXiv:2001.08361)（出处：workshop-draft-metacog-20261122.md ref 8 + D1-academic-AI papers 多处）
- 连接点：scaling law——pfb 的"27B 开放权重"定位与 compute-optimal 参照
- 合作角度（推断）：连接较弱，scaling 锚点
- 优先级：低 — scaling 锚点

### J. Hoffmann / S. Borgeaud / A. Mensch（et al.）（机构 [待核验]）
- 代表工作：Training Compute-Optimal Large Language Models (arXiv:2203.15556)（出处：同上）
- 连接点：compute-optimal——pfb 的"27B 本地能跑"定位的 compute 参照
- 合作角度（推断）：连接较弱
- 优先级：低 — compute 锚点

### L. Cheng（机构 [待核验]）
- 代表工作：Co-discovery phase transitions in high-velocity scientific fields（arXiv 2026，D1-academic-AI/S12-1 自引）（出处：projects/AI-计算科学/D1-academic-AI/papers/s18-1-kolmogorov-router/s18-1-kolmogorov-router.tex + S17-1.tex）
- 连接点：科学发现的共发现相变——pfb 的"研究自动化"域的科学计量学参照
- 合作角度（推断）：连接较弱，科学计量学参照
- 优先级：低 — 科学计量学参照

### E. Goldfeld（机构 [待核验]）
- 代表工作：The problem-space perspective on scientific discovery（出处：projects/AI-计算科学/D1-academic-AI/papers/s12-1-co-discovery-phase-transition/co-discovery-phase-transition.tex）
- 连接点：problem-space 视角——pfb 的"分解树=激活子图"（#48）与其同域
- 合作角度（推断）：连接较弱，problem-space 参照
- 优先级：低 — problem-space 参照

## 汇总

- 候选总数：**117 条**（高 18 / 中 46 / 低 53；其中 Y. Du 一条为指向 B 节 M. Du 的合并指针，实际唯一人/团队 116；4 个团队作者名单本地不全标 [待核验]：SA-Scheduler、AMALI、OPPO OpenResearcher、阿里 Tongyi DeepResearch；另有多处仅存单名/et al./匿名团队）
- 覆盖本地文献 16 份（见文件头）
- 机构可证 4 处：ScientistTwo=Google Cloud AI Research（scientisttwo-comparison.md）、TRUST=浙大/乔治华盛顿（trust-2611.10787-note.md）、BATS=UCSB/Google/NYU（objective-function-priorart-SNOWBALL-T51.md）、Eureka= NVIDIA/UPenn（longterm-vision-survey.md §L1）；其余机构一律 [待核验]
- 邮箱：本地文献无任何邮箱信息，全部 [待核验]（discover 阶段不联网，不补）

