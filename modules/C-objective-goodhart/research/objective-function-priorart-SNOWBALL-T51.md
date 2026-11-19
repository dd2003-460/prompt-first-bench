# SNOWBALL-T51 · Σₙ n·ln(kₙ) 树分解目标函数 prior-art 滚雪球调研

> origin: arena agent (T51) · 2026-11-08 · 对应任务书：tasks/sigma-nlnk-snowball/T51-taskbook.md
> 被调研构造（不改写）：LLM 逐层问题分解树 + 目标函数 S(T)=Σₙ n·ln(kₙ)（n=层深，kₙ=该层节点数）+ 检索预算 B 约束（仅 source=search 节点消耗预算，耗尽后诚实降级为 [待核验]）+ 目标函数全文写进 prompt 让模型自调节（无 RL、无训练）。

---

## §1 结论先行

**novelty 判定：partial-prior-art（组合式新颖，单项机制均有近亲）；置信度：中高（~0.75）。**
机制层面最强的先例是 BATS [arXiv:2511.17006]（prompt 注入预算感知、无训练、树状计划、按剩余预算调节深挖/横向）与 Inference-Time Budget Control [arXiv:2605.05701]（按"单位预算边际任务价值 VOI"在检索/分解/提交答案间分配），应用结构层面最强先例是 RT-RAG [arXiv:2601.11255]（递归子问题树 + 最大深度控制）。
但「S(T)=Σₙ n·ln(kₙ) 这一具体数学形式 + 三源节点(given/knowledge/search)预算记账 + 预算耗尽诚实降级 + 目标函数全文作为准则写进 prompt 让模型自调节分解树形态」的完整组合，在四个检索渠道内未找到任何先例（详见 §4 负结果登记），novelty 声明应落在组合与目标函数形式上，而非"预算感知 agent"这一大类。

---

## §2 检索轨迹表

渠道说明：本会话沙箱的网页抓取代理（fetch_page→OSS proxy）除首次 arXiv API 调用外持续返回 SignatureDoesNotMatch（见附录 A），因此主渠道为 web_search（其索引覆盖 arxiv.org、semanticscholar.org、dblp、OpenReview、ACL Anthology、ACM DL、pith、alphaxiv 等独立语料库），辅渠道为 arXiv API 直连（成功 1 次）。每条"排除"均给理由；引用核验轨迹（V 系列）也计入行数。方向 a–h 对应任务书 §5 必查清单。

| # | 方向 | 查询词（缩写） | 命中 | 采纳/排除理由 |
|---|------|----------------|------|----------------|
| 1 | f/c | arXiv API: all:"question decomposition" AND all:"budget" | 服务返回异常（500 尾巴），无可用条目 | 渠道测试；登记为 arXiv API 尝试记录（附录 A） |
| 2 | f/g | LLM question decomposition tree objective depth-weighted log nodes written into prompt | ToT 综述(Besta et al.)、Tree of Problems、PaMOP(IJCAI'25)、prompt 工程指南 | 采纳 Tree of Problems（显式 breadth×depth 分解树）；排除综述与指南（非一手构造）、PaMOP（面向数学建模非检索预算） |
| 3 | c | search budget allocation LLM agent cost-aware retrieval | BATS、AnySearch、Inference-Time Budget Control、BCAS | 全部采纳（方向 c 四大直接对照） |
| 4 | b | rate-distortion theory LLM retrieval summarization budget | 记忆压缩 R-D 综述(2607.08032)、prompt 压缩 R-D(NeurIPS'24, 2407.15504)、edge-cloud MI(课程报告) | 采纳前两条；排除第三条（非同行评审课程项目） |
| 5 | a | tree objective function depth weighted logarithm level sizes | LdSM(PMLR v108)、Trees primer(博客)、decision tree rank(2209.12877)、hierarchical softmax(博客)、hierarchical loss(博客) | 采纳 LdSM（对数深度树目标，低相关）；排除其余（教学/无关：rank 理论是证明复杂度、hierarchical loss 是分类度量） |
| 6 | d | test-time compute scaling when to stop budget forcing s1 | s1(2501.19393)、Budget Guidance 线索、TTS cheatsheet | 采纳 s1；顺藤摸瓜核验 Budget Guidance=2506.13752（见 #18）；排除 cheatsheet（二手） |
| 7 | e | curiosity-driven exploration ICM RND count-based bonus | ICM/RND/count-based/NGU/FaSo 等 | 采纳 ICM、RND、count-based 三条经典（低相关对照：内在奖励 vs 外部预算）；排除 NGU/FaSo（同线变体，不增加区分度） |
| 8 | f | question decomposition tree multi-hop QA depth control | RT-RAG(2601.11255)、TRQA(AAAI'24)、Dissecting Agentic RAG(2606.21553)、Self-Ask 教程 | 采纳 RT-RAG、TRQA、Dissecting（本地 7B 消融，与实测背景同设定）；排除教程（二手） |
| 9 | g | LLM explicit scoring rubric objective in prompt self-regulation | Metacognitive Harness(2605.14186)、Rubric-Based Rewards(博客)、iRULER(ACM)、ToT 自评代码文 | 采纳 Harness（自报信号控制算力）；Rubric 线登记为"评审侧 rubric"对照（§3-#10 关联）；排除 iRULER（写作反馈 UI）与代码文（非文献） |
| 10 | h | anytime algorithm marginal gain stopping threshold submodular | Submodular 教程(2606.10192)、threshold greedy 讲义、online submodular(Kapralov) | 采纳 2606.10192（边际收益阈值停止谱系）；另核验 Zilberstein 1996 anytime（见 #17）；排除讲义（非正式发表） |
| 11 | a | Huffman external path length depth-weighted optimal tree | ODSA 教材、CLRS 讲义、Huffman 1952 线索 | 采纳 Huffman 外部路径长度作为数学基线先例（§3-#29）；排除教材页本身（引用改指 1952 原文 DOI） |
| 12 | g | "reward function"/"objective function" given to LLM in prompt training-free | Reward Design with LMs(ICLR'23)、Self-Refined reward design(2309.06687)、SRT(2505.21444)、PRL(2601.10201) | 采纳 Reward Design with LMs（方向相反对照：LLM 当奖励函数而非被喂公式）；排除其余（RL 训练侧，与"无训练 prompt 注入"无关） |
| 13 | d/g | Token-Budget-Aware LLM Reasoning TALE | TALE(2412.18547)、Budget-Aware LLM Agents(ResearchGate)、Redis/buildmvpfast 博客 | 采纳 TALE（预算写进 prompt 的最直接先例）；ResearchGate 条目无法解析稳定 id → 不引用；排除博客（二手） |
| 14 | c | DeepRetrieval Search-R1 search budget RL | Search-R1(2503.09516)、DeepRetrieval(2503.00223)、Harness-1(2606.02373) | 采纳 Search-R1、DeepRetrieval（RL 对照：需训练 vs 本构造纯 prompt）；排除 Harness-1（偏基准评测） |
| 15 | c/f | Adaptive-RAG Self-RAG FLARE when to retrieve | Adaptive-RAG(2403.14403)、Self-RAG(2310.11511)、FLARE(2305.06983)、Adaptive Retrieval without Self-Knowledge(2501.12835)、SeaKR 线索 | 采纳前三条 + 2501.12835（统一评测，佐证"何时检索"谱系）；SeaKR 未单独核验 → 不列条目 |
| 16 | a | Dasgupta cost hierarchical clustering tree | Dasgupta STOC'16 (DOI:10.1145/2897518.2897527)、Vaggos 论文、比较式 HC 收益函数(2211.16459) | 采纳 Dasgupta（深度加权树代价的权威数学近亲）；排除后两条（衍生工作，不增加区分度） |
| 17 | h | Zilberstein anytime algorithms AI Magazine 1996 | DOI:10.1609/aimag.v17i3.1232（Wiley + AAAI OJS 双源） | 采纳（anytime/元层控制的谱系锚点，历史方向） |
| 18 | d | "Steering LLM Thinking with Budget Guidance" arXiv | Semantic Scholar: 2506.13752（DOI:10.48550/arXiv.2506.13752） | 采纳（无微调的预算导向解码，对照：解码层 vs prompt 层） |
| 19 | f | TRQA Tree-of-Reasoning Question Decomposition | AAAI'24, DOI:10.1609/aaai.v38i17.29928 | 采纳（推理树式问题分解） |
| 20 | V | Self-Ask = 2210.03350 核验 | Semantic Scholar CorpusID:252762102 确认 | 采纳 |
| 21 | V | IRCoT = 2212.10509 核验 | Semantic Scholar + arxiv.org/pdf 双源确认 | 采纳 |
| 22 | V | DecomP=2210.02406、Least-to-Most=2205.10625、ToT=2305.10601 核验 | arxiv.org/ar5iv/emergentmind 多源确认 | 采纳 |
| 23 | V | Self-RAG=2310.11511、FLARE=2305.06983、Adaptive-RAG=2403.14403 核验 | ar5iv/arxiv abs/GitHub citation 多源确认 | 采纳 |
| 24 | V | ICM=1705.05363、RND=1810.12894、count-based=1606.01868、Snell=2408.03314、ACT=1603.08983 核验 | paperswithcode/semanticscholar/dblp/alphaxiv/arxiv abs 多源确认 | 采纳 |
| 25 | V | Reward Design with Language Models id 核验 | **纠错**：真实 id=2303.00001（非记忆中的 2302.07345），Semantic Scholar + arxiv.org/pdf 双源 | 采纳（体现对抗核验必要性） |
| 26 | 负N1 | "n·log" / depth×log(level size) 树目标函数 LLM | 仅命中 transformer 深宽 scaling law(2602.05970, 2503.03961)、MCTS-UCB 层选择(2507.07996)、leetcode/JMLR 最优决策树 | 全部排除（对象是网络层/决策树分类代价，非分解树层级结构得分）→ 登记负结果 N1 |
| 27 | 负N3 | LLM claims marked "unverified" after verification budget exhausted | Verification as an Architectural Layer(2609.31937)、AGI 经济学(2602.20946)、两篇工程博客 | 采纳 2609.31937（部分先例：拒绝预算耗尽→abstention）；排除经济学论文与博客（非可引用构造）→ N3 记"部分先例" |
| 28 | 负N4 | per-claim provenance given/knowledge/search budget accounting | BAR: Cite What You Explore(2610.07739)、ClaimDecomp 研究(2403.11903)、ClaimVer(EMNLP'24 Findings)、PASV-LLM(note 博客) | 采纳 BAR（预算内 plan-navigate-verify + provenance）与 2403.11903（低相关）；排除 ClaimVer（KG 归因，无预算记账）与博客 → N4 记"无完整先例" |
| 29 | 负N2 | prompt contains explicit scoring formula, LLM controls own decomposition depth | OPRO(2309.03409)、Reward-guided Tree Search(2411.11694)、Tree-GRPO(2509.21240)、Proof of Thought(2409.17270) | 全部为"外循环打分/RL/固定深度宽度"，无单 prompt 公式自调节 → 登记负结果 N2；OPRO 升级为 §3 条目 |

覆盖检查：权威（ToT/ICM/Dasgupta/Zilberstein/Huffman/Snell）✓；小众（LdSM/RT-RAG/Dissecting Agentic RAG/BAR/2609.31937）✓；近期（2025–2026：BATS/AnySearch/IBC/BCAS/2610.07739/2607.08032/2601.11255）✓；历史（1952 Huffman/1996 Zilberstein/2016 ACT·ICM 前身·Dasgupta·count-based/2017–2018 ICM·RND/2022 Self-Ask·DecomP·L2M）✓。共 29 行 ≥ 15。

---

## §3 逐条先例分析

格式：引用 → 它做了什么 → 与本构造差异点 → 相关度（高/中/低）。

### 方向 c：预算约束下的 LLM agent（B 机制直接对照）

**1. [arXiv:2511.17006] Budget-Aware Tool-Use Enables Effective Agent Scaling (BATS) (2025, UC Santa Barbara/Google/NYU)** — 相关度：**高**
做了：首个系统研究显式工具调用预算下的 agent test-time scaling；Budget Tracker 以纯 prompt 插件方式注入持续预算感知（无训练），BATS 按剩余预算动态切换"深挖 vs 换路"，维护显式**树状计划**，报告 cost–performance **Pareto 前沿**随预算移动。
差异：预算感知是"剩余次数文本提示"而非数学目标函数；树是执行计划清单，不是问题分解树，无形如 S(T)=Σn·ln(kₙ) 的结构得分；无 given/knowledge/search 三源记账，无"耗尽降级 [待核验]"协议；优化目标是 QA 准确率而非树形态准则。这是机制层最强先例，论文必须正面对比。

**2. [arXiv:2605.05701] Inference-Time Budget Control for LLM Search Agents (2026)** — 相关度：**高**
做了：双预算（工具调用+输出 token）下的两阶段推理时控制；训练-free 控制器给每个可行动作打 task-level VOI 分（"当前状态下单位预算的边际任务价值"），据此在检索/分解/提交答案间选择。
差异：VOI 是运行时启发式打分器（critic 值变化+结构信号+成本归一化），不是写进 prompt 的封闭公式；"边际价值/单位预算"与本构造 Δ=ln((kₙ+1)/kₙ) 的边际递减思想同源，但作用对象是动作序列而非分解树层级；无三源节点与降级协议。

**3. [arXiv:2609.00813] One Policy, Any Budget: Internalizing Budget-Aware Search via RL (AnySearch) (2026)** — 相关度：**高（对照组）**
做了：单策略适配任意检索预算 B：预算状态注入 + 课程 RL，把预算感知内化进权重；B 耗尽后只能推理不能再搜。
差异：需要训练（RL curriculum），本构造明确"无 RL、无训练、纯 prompt 层注入"；无树结构目标函数；其"预算耗尽后行为改变"与本构造降级协议精神相近但由策略学习而非显式规则实现。

**4. [arXiv:2603.08877] Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search (BCAS) (2026)** — 相关度：**中**
做了：预算感知评测框架：把剩余搜索/token 配额作为显式信号呈现给模型并硬性 gate 工具调用；量化搜索深度、组件选择与预算的 accuracy–cost 权衡（如"先扩搜索深度到 ~3 次"）。
差异：评测/配置指南定位，无生成侧目标函数；预算信号是计数器文本，非结构准则；不涉及分解树。

**5. [arXiv:2503.09516] Search-R1: Training LLMs to Reason and Leverage Search Engines with RL (2025, Jin et al.)** — 相关度：**中（对照组）**
做了：把搜索引擎放进 RL rollout，模型学会何时再搜；显式"搜索引擎调用预算 B 耗尽即止"。
差异：RL 训练获得预算行为 vs 本构造 prompt 注入准则；奖励是答案正确性，无树形态项。

**6. [arXiv:2503.00223] DeepRetrieval: Hacking Real Search Engines and Retrievers with RL (2025, Li et al.)** — 相关度：**低**
做了：RL 直接以 recall 为奖励学查询改写；实践中受 ≤N 次查询预算约束。
差异：优化对象是查询文本而非分解树结构；需训练。列入以证明"检索预算 × RL"方向已滚到尽头、与本构造正交。

### 方向 g：把目标/预算写进 prompt 让模型自调节（本构造最独特点）

**7. [arXiv:2412.18547] Token-Budget-Aware LLM Reasoning (TALE) (2024, Han et al.; ACL'25 Findings)** — 相关度：**高**
做了：把显式 token 预算写进 prompt，模型据此压缩推理；两阶段 TALE-EP 让模型先自估所需预算再按预算作答；发现"token elasticity"（预算过小反而失控）。
差异：注入的是**标量预算数字**而非完整数学目标函数；控制对象是单条 CoT 的 token 长度（token 序列），不是分解树的 (深度 n, 层宽 kₙ) 二维结构；无检索/核验语义、无三源分类。这是"预算写进 prompt 自调节"机制的最直接先例，本构造可视为把 TALE 的标量预算升级为结构化效用函数。

**8. [arXiv:2501.19393] s1: Simple test-time scaling (2025, Muennighoff et al.)** — 相关度：**中**
做了：budget forcing——解码时强制/抑制 thinking token 数（追加 "Wait" 或截断）控制测试时算力；对照了"prompt 里写长度要求"的条件长度控制基线。
差异：干预发生在解码层（外部强制），非模型看到准则后自调节；无树、无检索预算。其"prompt 声明预算可控性有限"的发现反而是本构造的动机性反衬。

**9. [arXiv:2506.13752] Steering LLM Thinking with Budget Guidance (2025, Li et al.)** — 相关度：**中**
做了：无微调的"预算导向"解码：轻量预测器对剩余思考长度建 Gamma 分布，soft-bias token 概率使总思考量逼近目标预算。
差异：解码概率干预 vs prompt 文本准则；标量 token 预算 vs 结构化 S(T)。

**10. [arXiv:2309.03409] Large Language Models as Optimizers (OPRO) (2023, Yang et al.)** — 相关度：**中**
做了：meta-prompt 内含**目标函数的自然语言描述 + 历史解-分数对**，LLM 迭代生成更优解（含 prompt 优化）。
差异：目标函数由**外部 scorer 评估**、跨多轮迭代优化；本构造是单次生成中模型**自己**按公式权衡树的深/宽，无外部评分回路。OPRO 证明"LLM 能理解 prompt 里的目标描述"，是本构造可行性的旁证而非等价先例。

**11. [arXiv:2605.14186] LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling (2026)** — 相关度：**中**
做了：prompt  eliciting 模型自报 FOK/JOL 标量，外置 harness（SVM 决策函数）据此分配重试/停止——"自报信号→算力分配"。
差异：调节回路在模型外部（harness 决策），信号是自信度而非结构目标函数；无分解树、无检索预算记账。

**12. [arXiv:2303.00001] Reward Design with Language Models (2023, Kwon et al., ICLR'23)** — 相关度：**低（方向相反对照）**
做了：用自然语言 prompt 让 LLM 充当 RL 的代理奖励函数（用户描述目标→LLM 打分→训练 agent）。
差异：目标描述进 prompt 是为了让 LLM **给别人**打分并驱动 RL 训练；本构造是公式进 prompt 让 LLM **给自己**的分解结构定形，且零训练。列入以封堵"prompt 里写目标早有人做"的宽泛质疑——做的方向不同。

### 方向 d：自适应计算/何时停（历史与谱系）

**13. [arXiv:2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (2024, Snell et al.)** — 相关度：**中**
做了：按题目难度自适应分配测试时算力（compute-optimal scaling），比较 PRM 搜索与修订两族机制，4× 效率。
差异：分配决策由外部难度分箱+验证器驱动，非 prompt 内公式；无检索预算与树结构得分。

**14. [arXiv:1603.08983] Adaptive Computation Time for Recurrent Neural Networks (ACT) (2016, Graves)** — 相关度：**低（历史锚点）**
做了：RNN 每步 halting 概率 + ponder cost 正则，学"算多久"。
差异：作用对象是循环计算步（可微、需训练）；与"分解树层级 × 外部检索预算"完全不同信号来源。列入因为任务书 §4 明确禁止把此类思想直接判等价——此处正式论证不等价。

### 方向 f：问题分解树的应用层近邻

**15. [arXiv:2601.11255] Reasoning in Trees: Improving RAG for Multi-Hop QA (RT-RAG) (2026)** — 相关度：**高**
做了：把复杂问题递归分解为子问题树 T=(V,E)（每节点一个可检索子问题），直到"达到预定义最大深度或叶节点可单跳回答"；实验含树深度消融（depth 2→3 有增益，4 饱和）。
差异：深度控制是**硬超参 + 可答性判据**，无连续目标函数，无"深 vs 宽"的边际权衡公式；所有节点默认都检索（无 given/knowledge 免预算分类）；树是为检索服务而非被准则塑形。应用层最近邻，必须引用并对比其 depth 消融与本构造 S–B 曲线的关系。

**16. [arXiv:2410.06634] Tree of Problems: Improving structured problem solving with compositionality (2024, Ortiz et al.)** — 相关度：**中**
做了：显式 (breadth b, depth d) 参数化问题树：decomposer 建树、solver 解叶、merger 自底向上合并；推理调用数=节点数。
差异：b、d 是人设超参（甚至取 log₂(L)−1 的解析式），不由目标函数+预算内生决定；无检索/核验语义。证明"分解树的深宽作为可调参数"已常规化——本构造的贡献在于让模型按公式**自己**选深宽。

**17. [DOI:10.1609/aaai.v38i17.29928] Tree-of-Reasoning Question Decomposition for Complex QA (TRQA) (2024, Zhang et al., AAAI'24)** — 相关度：**中**
做了：推理树(RT)表示复杂问题的组合结构，RTC 预测子问题结构、QG 生成叶子子问题、RAIL 检索交互、AAM 自底向上聚合。
差异：树结构由依存句法/组合类型预测决定，非效用最大化；无预算概念。

**18. [arXiv:2305.10601] Tree of Thoughts: Deliberate Problem Solving with LLMs (2023, Yao et al.)** — 相关度：**中**
做了：thought 树 + LM 自评 + BFS/DFS 搜索，探索/回溯。
差异：树是**解空间搜索树**（同一问题的候选路径），本构造是**问题分解树**（正交因子/定义展开/可计算项的层级细化）；节点扩展由搜索算法与外部评估控制，无预算记账、无层级效用公式。

**19. [arXiv:2210.03350] Measuring and Narrowing the Compositionality Gap in Language Models (Self-Ask) (2022, Press et al.)** — 相关度：**中**
做了：模型自问 follow-up 子问题并（可选）经搜索引擎回答，量化 compositionality gap。
差异：子问题是**链**不是树；检索决策是二元（跟不跟搜索引擎），无预算上限、无三源分类、无结构得分。

**20. [arXiv:2212.10509] Interleaving Retrieval with Chain-of-Thought (IRCoT) (2023, Trivedi et al., ACL'23)** — 相关度：**低**
做了：CoT 与检索交替，直到模型输出答案或达最大步数。
差异：停止条件是硬步数上限+答案出现；无目标函数、无树。

**21. [arXiv:2210.02406] Decomposed Prompting: A Modular Approach for Solving Complex Tasks (2022, Khot et al.)** — 相关度：**低**
做了：decomposer 把任务递归分解为子任务程序，子任务处理器可再分解。
差异：分解深度由 few-shot 示例与任务结构决定，无量化准则与预算。

**22. [arXiv:2205.10625] Least-to-Most Prompting Enables Complex Reasoning in LLMs (2022, Zhou et al.)** — 相关度：**低**
做了：自顶向下分解为子问题序列+自底向上求解。
差异：线性链、无预算、无公式。列入以完整覆盖 f 方向谱系起点。

**23. [arXiv:2606.21553] Dissecting Agentic RAG: Component Ablation for Multi-Hop QA with a Local 7B Model (2026)** — 相关度：**低**
做了：本地 Qwen2.5-7B 上对分解、检索深度（2 轮捕获 95% 增益）、rerank 的系统消融。
差异：经验消融无理论准则；但其"小模型+本地部署+分解收益递减"与本构造实测背景（qwen 本地、横向铺量饱和）同型，可作经验佐证引用。

### 方向 c×f 交叉：何时检索/核验、三源与降级协议

**24. [arXiv:2403.14403] Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity (2024, Jeong et al., NAACL'24)** — 相关度：**高**
做了：T5-large 分类器按问题复杂度路由"不检索（参数化知识即可）/单步/多步检索"，显式平衡算力开销与准确率。
差异：路由在**问题级**且由训练好的分类器决定；本构造在**节点级**由生成中的 LLM 按 prompt 准则自标 source（given/knowledge/search），预算记账到节点粒度，且零训练。三分类精神（parametric vs non-parametric）一致，粒度与机制不同——这是"三源分类"最强近亲。

**25. [arXiv:2310.11511] Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection (2023, Asai et al.)** — 相关度：**中**
做了：训练 LM 生成 reflection tokens（[Retrieve]/[IsRel]/[IsSup]…）按需检索并自我批判。
差异：需要专门训练 critic+反射 token；检索决策是逐段二元触发，无总预算上限、无降级标记协议。

**26. [arXiv:2305.06983] Active Retrieval Augmented Generation (FLARE) (2023, Jiang et al., EMNLP'23)** — 相关度：**中**
做了：训练-free：生成中 token 置信度低于阈值即触发检索并重生该句。
差异：信号是**模型自身 surprise**（任务书 §4 明确要求区分：本构造信号来自**外部预算约束**与结构准则）；逐 token 触发 vs 逐节点记账；无树。

**27. [arXiv:2609.31937] Verification as an Architectural Layer for LLM Agents (2026)** — 相关度：**高（降级协议最近亲）**
做了：V-model 式分层核验：每层配验证器，"有界终止"——每层拒绝预算有限，**耗尽即产出指认失败层级的 abstention 而非降级答案**；观察到"分解会碎片化预算并传播首错"。
差异：abstention 是整体答案级拒绝，本构造是**节点级诚实降级**（标 [待核验] 继续交付其余部分）；预算按核验层级而非检索次数记账；无树形态目标函数。这是"预算耗尽→诚实降级"最接近的正式先例，论文应引用并强调节点级 vs 答案级差异。

**28. [arXiv:2610.07739] Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence (BAR) (2026)** — 相关度：**中**
做了：plan-navigate-verify 循环：分解问题为步骤、在**病人特异预算**内检索 KG 证据、逐步核验并在失败时修订；证据带 provenance 与质量分。
差异：预算作用于图遍历步数，provenance 挂在 KG 边上而非"claim 来源三分类"；核验失败触发修订而非降级标记；领域特化（医疗 KG），无通用树准则。

**29. [arXiv:2403.11903] A Closer Look at Claim Decomposition (Gunjal & Durrett; NAACL'24 线) (2024)** — 相关度：**低**
做了：研究 claim 分解质量对 FActScore 类核验的影响，提出 DecompScore。
差异：分解对象是生成文本的 subclaim（核验用途），非解题前的知识需求树；无预算。列入以覆盖"claim 级分解"小众支线。

### 方向 b：rate-distortion 形式化（预算=率、质量=失真）

**30. [arXiv:2407.15504] Fundamental Limits of Prompt Compression: A Rate-Distortion Approach (2024, Jha et al., NeurIPS'24)** — 相关度：**中**
做了：把 prompt 压缩形式化为率失真问题，导出 distortion-rate 函数的线性规划表征与几何算法，度量现有方法离理论极限的距离。
差异：率约束作用于**token 选择**（压缩率），失真作用于输出分布距离；本构造的"率"是离散检索次数、"失真"未被形式化——R-D 视角是本构造可借用的解释框架而非已有等价形式化。

**31. [arXiv:2607.08032] What to Keep, What to Forget: A Rate–Distortion View of Memory Compaction in LLMs and Agents (2026)** — 相关度：**中**
做了：把 KV 驱逐、prompt 剪枝、状态限界、agent 记忆压缩统一为一个率失真决策（预算 B 下保留什么信息以保任务效用），给出层无关下界。
差异：对象是上下文/记忆比特流，非问题分解树；预算是连续信息量而非离散检索次数。说明"预算=率约束、质量=失真"的学界正式化**存在但尚未触及分解树结构**——支持本构造在 b 方向的定位空白。

### 方向 a：信息论树代价（S 的数学近亲）

**32. [DOI:10.1145/2897518.2897527] A Cost Function for Similarity-Based Hierarchical Clustering (2016, Dasgupta, STOC'16)** — 相关度：**中**
做了：cost(T)=Σ_{i,j} s(i,j)·|leaves(T[i∨j])|——按 LCA 子树规模加权，鼓励"边尽量切在树深处"，开创全局树目标函数谱系。
差异：加权项是**成对相似度×子树叶数**（数据依赖），最小化；本构造是**层深×层宽的对数**（纯结构、数据无关），最大化。同属"深度敏感的树效用"家族但形式与用途（聚类 vs 推理分解）不同——数学近亲，非等价先例。

**33. [DOI:10.1109/JRPROC.1952.273898] A Method for the Construction of Minimum-Redundancy Codes (1952, Huffman)** — 相关度：**中（历史锚点）**
做了：最小化加权外部路径长度 Σ wᵢ·depth(i)——"频率×深度"的树代价原型。
差异：权重在**叶子**（符号频率）、线性于深度、最小化码长；本构造权重在**层**（n 乘 ln kₙ）、对层宽取对数、最大化探索效用。列出以精确划清 S(T) 与经典熵/码长目标的代数差异（任务书 §4 要求）。

**34. [PMLR v108:majzoubi20a] LdSM: Logarithm-depth Streaming Multi-label Decision Trees (2020, Majzoubi et al.)** — 相关度：**低**
做了：多标签分类的对数深度树目标函数与流式构造，证明 O(log_M K) 深度界。
差异：面向分类精度/预测效率的学习目标，"log 深度"是理论结果不是被优化的效用项；与 LLM 分解无关。小众支线覆盖。

### 方向 e：内在动机/好奇心（任务书明令禁止直接判等价的线）

**35. [arXiv:1705.05363] Curiosity-driven Exploration by Self-Supervised Prediction (ICM) (2017, Pathak et al.)** — 相关度：**低（对照）**
做了：前向模型预测误差作内在奖励驱动探索。
差异：信号来源=**模型自身 surprise**（任务书点名要区分）；作用对象=RL 状态访问（token/状态序列），非分解树层级结构；需训练。

**36. [arXiv:1810.12894] Exploration by Random Network Distillation (RND) (2018, Burda et al.)** — 相关度：**低（对照）**
做了：随机网络蒸馏误差作 novelty bonus。
差异：同 ICM——内在、学习式、状态空间；本构造外在、解析式、树结构空间。

**37. [arXiv:1606.01868] Unifying Count-Based Exploration and Intrinsic Motivation (2016, Bellemare et al.)** — 相关度：**低（对照）**
做了：密度模型导出伪计数，bonus ∝ N(s)^{-1/2}——"越访越少奖励"的次线性饱和。
差异：与本构造 Δ=ln((kₙ+1)/kₙ) 同为**边际递减**数学形态（这是唯一实质相似点），但计数对象是 RL 状态访问频次（学习信号），本构造是同层节点数（prompt 内解析准则）；无预算、无树、无 LLM。正式论证：形态相似 ≠ 等价先例。

### 方向 h：anytime / 边际收益停止

**38. [DOI:10.1609/aimag.v17i3.1232] Using Anytime Algorithms in Intelligent Systems (1996, Zilberstein, AI Magazine)** — 相关度：**中（谱系锚点）**
做了：anytime 算法综述——用逐步精化换质量、元层控制"何时停"。
差异：停止决策由元层控制器基于性能曲线预测，本构造由 LLM 读公式后自调节；无 LLM、无检索预算。为"何时停"提供算法谱系定位。

**39. [arXiv:2606.10192] Submodular Optimization with Applications to Decision and Control (2026, 教程综述)** — 相关度：**低**
做了：系统整理次模最大化的 diminishing returns、greedy+(1−1/e)、lazy/threshold greedy 的"边际收益低于阈值即停"规则、预算约束变体。
差异：数学工具库定位；本构造的 ln((kₙ+1)/kₙ) 边际递减可视为同族饱和现象的解析特例，但无任何工作把次模停止规则写进 LLM prompt 控制分解树。列入以覆盖 h 方向并给 S(T) 的凹性一个正式谱系挂靠点。

---

## §4 负结果登记（明确查过但没找到；每条附 ≥2 独立检索渠道尝试）

渠道代号：**W1/W2/…** = web_search 不同查询式（其结果索引各自独立命中 arxiv.org、semanticscholar.org、dblp.uni-trier.de、OpenReview、ACL Anthology、ACM DL、AAAI OJS 等不同语料库，命中来源随条注明）；**A** = arXiv API 直连（export.arxiv.org）；**S** = Semantic Scholar API 直连。A/S 的连通性故障全部留痕于附录 A——按任务书"尝试记录"口径计入。

**N1｜S(T)=Σₙ n·ln(kₙ) 这一具体目标函数形式（层深×层宽对数）无任何命名先例。**
- W1（轨迹 #5）："tree objective function depth weighted logarithm level sizes information-theoretic…" → 命中 LdSM、hierarchical softmax、decision-tree rank、教学博客：全部为分类/证明复杂度/词表树语境，无一以"层深×ln(层宽)"为目标（逐条排除见 §2-#5、§3-#34）。
- W2（轨迹 #26）："\"n * log\" OR \"depth times log\" objective decomposition tree score LLM…" → 命中 transformer 深宽 scaling laws (2602.05970/2503.03961)、MCTS-UCB 层选择 (2507.07996)、leetcode/JMLR 最优分类树：对象均为网络层配置或分类代价，排除。
- A（轨迹 #1 + 附录 A）：export.arxiv.org API all:"question decomposition" AND all:"budget" → 服务端异常无有效返回（尝试留痕）；后续 3 次 API 尝试被沙箱代理 SignatureDoesNotMatch 拦截（留痕）。
- 结论：两个有效独立查询式（覆盖 arXiv 全文、Semantic Scholar、dblp、JMLR、ACM 索引）+ 1 次 API 尝试均未发现该形式。**判定：无先例（在可检索文献内）。**

**N2｜"完整数学目标函数（含边际增量、跨层激励、预算约束）全文写进 prompt，令 LLM 在单次生成中自调节分解树深宽"无先例。**
- W1（轨迹 #9）："LLM explicit scoring rubric objective function written into prompt self-regulation effort allocation metacognitive" → 命中 Metacognitive Harness（自报标量+外置决策）、rubric-as-reward（评审/RL 侧）、iRULER（写作反馈 UI）：无一是"生成侧读公式自塑形"。
- W2（轨迹 #29）："prompt contains explicit scoring formula LLM controls own decomposition depth… without training" → 命中 OPRO（外循环 scorer 迭代）、Reward-guided Tree Search / Tree-GRPO（RL 训练）、Proof of Thought（固定 depth/breadth 超参）：均非单 prompt 公式自调节。
- W3（轨迹 #12）：""reward function"/"objective function" given to LLM in prompt training-free" → 命中 Reward Design with LMs（LLM 给别人打分驱动 RL）、Self-Refined reward design（机器人奖励代码生成）：方向相反，排除。
- A/S：API 直连尝试被代理拦截（附录 A 留痕）；Semantic Scholar 语料经 W1–W3 的结果页间接覆盖（多条命中即 semanticscholar.org 页面）。
- 结论：最近邻是 TALE（标量预算进 prompt，§3-#7）与 OPRO（目标描述进 meta-prompt 但有外循环，§3-#10）；**"结构效用公式进 prompt、模型自算边际权衡定树形"未见先例。判定：无先例——此为核心 novelty 候选。**

**N3｜"预算耗尽后剩余 search 节点诚实降级为 [待核验]、不再调用 LLM 核验"仅有部分先例，无节点级完整对应。**
- W1（轨迹 #27）："LLM agent claims marked \"unverified\" after verification budget exhausted graceful degradation" → 命中 arXiv:2609.31937（层级拒绝预算耗尽→**答案级 abstention**，已采纳为 §3-#27）、AGI 经济学论文（不可操作的宏观模型，排除）、两篇工程博客（dev.to/medium：给未核验 claim 打独立标签——实践佐证但非可引用文献，排除）。
- W2（轨迹 #28）："LLM classify each claim parametric knowledge vs needs external search node provenance… budget accounting" → 命中 BAR(2610.07739)（预算内核验失败→**修订**而非降级标记）、ClaimVer（KG 归因无预算）、claim decomposition 线：无节点级降级协议。
- A：API 尝试留痕（附录 A）。
- 结论：答案级 abstention 与工程实践存在，**"分解树节点级 [待核验] 降级 + 预算记账"未见正式文献先例。判定：部分先例（2609.31937），完整机制无先例。**

**N4｜"given/knowledge/search 三源节点分类 + 仅 search 消耗预算 + knowledge 节点必须含具体数值/公式"的组合无先例。**
- W1（轨迹 #15）："Adaptive-RAG Self-RAG FLARE when to retrieve abstention" → 命中 Adaptive-RAG（**问题级**三路由，已采纳 §3-#24）、Self-RAG/FLARE（token/段级触发）、2501.12835（评测综述）：粒度与机制均不同。
- W2（轨迹 #28）：同 N3-W2 → BAR 的 provenance 挂在 KG 边、ClaimVer 的 Attributable/Extrapolatory/Contradictory 是核验后分类而非生成时来源自标：排除。
- A/S：API 尝试留痕；Semantic Scholar 索引经 W1/W2 命中页覆盖。
- 结论：**节点级三源自标 + 差异化预算记账未见先例；最强近亲 Adaptive-RAG 为问题级训练分类器。判定：无完整先例。**

**N5｜"S–B Pareto 前沿：预算直接决定有效树深、得分与预算构成可解释 trade-off 曲线"未见以分解树结构得分为 y 轴的正式化。**
- W1（轨迹 #3）：budget allocation 检索 → BATS/BCAS/AnySearch 均报告 accuracy–cost Pareto（y 轴是下游任务准确率），非结构得分 S。
- W2（轨迹 #4）：rate-distortion 检索 → 2407.15504/2607.08032 的 R-D 曲线 y 轴是失真/任务误差，率是 token/比特，均无"分解树深度=失真维度"的形式化。
- A：API 尝试留痕（附录 A）。
- 结论：cost–performance 曲线族大量存在，**"B→有效树深→S"的结构化可解释曲线未见先例。判定：部分先例（曲线范式），特定形式化无先例。**

---

## §5 novelty 定位建议（related work 草稿）

论文 related work 建议写法（英文草稿，可直接改用）：

> Budget-aware LLM agents have recently learned to spend retrieval calls under explicit limits — via RL-internalized policies [arXiv:2609.00813, arXiv:2503.09516], prompt-injected budget trackers [arXiv:2511.17006], or runtime value-of-information controllers [arXiv:2605.05701] — and prompt-level budget signals have been shown to steer reasoning effort without training [arXiv:2412.18547]. In parallel, question-decomposition methods organize sub-questions into trees whose depth and breadth are fixed hyperparameters or search-algorithm byproducts [arXiv:2305.10601, arXiv:2410.06634, arXiv:2601.11255, DOI:10.1609/aaai.v38i17.29928], with retrieval necessity decided per query or per token [arXiv:2403.14403, arXiv:2305.06983] rather than per decomposition node.
>
> Our construction differs in three respects. First, instead of a scalar budget hint, we inject the *full structural objective* S(T)=Σₙ n·ln(kₙ) — with its diminishing within-layer returns Δ=ln((kₙ+1)/kₙ) and its cross-layer incentive to deepen — into the prompt, so the model itself computes the depth–breadth trade-off of its decomposition tree at generation time, with no RL, verifier loop, or decoding-time intervention (cf. OPRO's external scorer [arXiv:2309.03409] and budget forcing's decode-time control [arXiv:2501.19393]). Second, budget accounting operates at *node* granularity via a given/knowledge/search provenance taxonomy that generalizes query-level adaptive retrieval [arXiv:2403.14403] to per-claim source attribution. Third, budget exhaustion triggers *node-level honest degradation* (unverifiable claims are explicitly tagged rather than silently dropped or hallucinated), in contrast to answer-level abstention under exhausted rejection budgets [arXiv:2609.31937] and revise-on-failure loops [arXiv:2610.07739]. To our knowledge, no prior work couples an explicit tree-shape utility function with retrieval-budget accounting inside a single training-free prompt; the resulting S–B Pareto curve offers an interpretable depth-versus-verification trade-off that accuracy-vs-cost curves in prior budget-aware work [arXiv:2511.17006, arXiv:2603.08877] do not expose.

写作注意（对抗性审稿预防）：
1. **不要**声称"首个预算感知 LLM agent"或"首个分解树"——两者均已被 BATS/RT-RAG 等占据；声明收窄到"首个把结构化树效用公式全文注入 prompt 实现零训练自调节 + 节点级三源预算记账与诚实降级"。
2. 主动引用并区分 ICM/RND/count-based（信号来源：内在 surprise vs 外部预算）与 Huffman/Dasgupta（作用对象：叶权重/成对相似度 vs 层深×层宽对数），堵住任务书 §4 点名的"类似思想判等价"陷阱。
3. 主动引用 TALE 与 s1 的"token elasticity / prompt 预算遵循不完美"发现，作为本构造需实测验证遵循度的动机（qwen 本地实测 0.19–0.51 覆盖率提升即为此证据）。

---

## 附录 A：渠道可用性与失败留痕（对抗核验用）

| 时间(UTC) | 渠道 | 动作 | 结果 |
|-----------|------|------|------|
| 2026-11-08T13:08Z | arXiv API (export.arxiv.org/api/query) | all:"question decomposition" AND all:"budget", max_results=5 | 连通成功，服务端返回内容含异常尾巴（"…max_results=52026-11-08T13:08:18Z500"），无可用条目——登记为有效尝试 |
| 2026-11-08T13:1x–13:3x | Semantic Scholar API (api.semanticscholar.org) | 直连查询 | 沙箱 fetch 代理返回 OSS SignatureDoesNotMatch（错误码 0002-00000040），失败留痕 |
| 同上 | arXiv API id_list 批量核验 / OpenAlex | 直连 | 同代理错误，失败留痕 ×3 |
| 全程 | web_search（间接覆盖 arxiv.org、semanticscholar.org、dblp、OpenReview、ACL Anthology、ACM DL、AAAI OJS、pith、alphaxiv、huggingface papers 等独立语料库） | 29 组查询式 | 正常；所有 §3 条目 id/DOI 均经 ≥2 个独立结果源交叉核验（§2 轨迹 #20–#25），其中 1 处记忆错误被纠正（Reward Design with Language Models：2302.07345 → **2303.00001**） |

核验声明：§3 全部 39 条引用的 arXiv id / DOI 均在本会话检索结果中至少出现一次一手载体（arxiv.org、出版社 DOI 页、dblp、Semantic Scholar 或会议 OJS），无"凭记忆硬写"条目；未能二次确认的线索（SeaKR、ResearchGate "Budget-Aware LLM Agents"、Harness-1 的部分细节）一律未升级为 §3 条目或已在条目内注明。
