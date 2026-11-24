# T-PR-17 结果：Prompt 序列消融文献滚雪球

**检索截止**：2026-11-24（UTC）
**任务书 SHA-256**：`3153398feb1af439f1fc4e80c3515685ee7c7834bd997a614dd2a0eb275fe405`
**范围**：2023–2026 年文献；重点是同一任务下的多阶段 prompt / workflow 顺序、固定中间状态续跑，以及长上下文位置效应。所有本报告引用的 arXiv ID 均直接核对过 arXiv `abs` 页；未调用 arXiv API。

> **一句话结论**：已有研究分别触及 prompt 元素/任务顺序、训练阶段顺序、固定 checkpoint 的 agent handoff，以及从推理前缀续跑；因此不能声称“LLM 顺序效应”或“checkpoint continuation”本身没有先例。当前检索未找到与本实验完全同构的设计：从同一个 SM 序列化中间状态，配对比较 canonical / 删除 verify / 阶段置换 / minimal 四种后缀序列，并以同一 gold 树 depth 指标评估。这个“未找到同构设计”是有限检索结论，不是文献不存在的证明。

## 总览 verdict

| 问题 | Verdict | 置信度（证据判断） | 边界 |
|---|---|---:|---|
| **C1 阶段/指令顺序是否有系统研究？** | **部分** | **0.76** | 有 prompt 元素顺序、单 prompt 多任务顺序、训练阶段顺序等近邻；与多调用推理 pipeline 的固定 checkpoint 后缀序列仍不完全同构。对“没有完全同构先例”的否定性判断置信度 **≤0.55**。 |
| **C2 固定中间状态换后续策略续跑是否有先例？** | **部分（强近邻）** | **0.82** | handoff benchmark 固定 repository/history/checkpoint 比较接手上下文；推理工作从同一 prefix 做不同 continuation。它们没有直接比较本实验四种 SM prompt 序列。对“没有完全同构先例”的否定性判断置信度 **≤0.55**。 |
| **C3 位置效应能否解释 pipeline 序列效应？** | **可作为中介/调节机制；不足以单独解释** | **0.88**（位置效应存在）；**0.86**（单机制不足） | 指令/证据位置对长上下文利用确有影响；它不能替代对阶段语义依赖、状态更新、工具调用与验证行为的检验。具体能解释本 SM 实验效应的比例尚未知。 |

置信度是对本次证据归类的主观判断，不是经校准的概率；否定性结论按任务纪律压低。

---

## §C1 多阶段 LLM pipeline 中的 prompt / instruction 顺序或阶段编排效应

### Verdict：**部分**（conf = 0.76）

| 判据 | Verdict | conf | 判断边界 |
|---|---|---:|---|
| 多阶段 LLM pipeline 的 prompt/instruction 顺序或编排是否有系统研究？ | 部分 | 0.76 | prompt 元素、同 prompt 多任务顺序及训练阶段顺序有实证；同一冻结 checkpoint 下的多调用后缀序列对照尚未找到，否定性判断 ≤0.55。 |

有可复现的相邻实证：在同一任务上改 prompt 元素顺序、把多个任务逐步堆入同一 prompt 后反转任务顺序，或调换后训练阶段，均有工作测过结果变化。另有不少多阶段系统做模块优化、组件删除或 workflow 搜索。但这些与“同一中间 checkpoint 下，用不同后续多调用 prompt 序列继续并比较 gold-tree depth”不是一回事。

| 反例 / 近邻 | 实际操纵与结果 | 与 T-PR-17 的差别 |
|---|---|---|
| Di Maio & Gozzi, *Degradation of Multi-Task Prompting Across Six NLP Tasks and LLM Families*, *Electronics* 14(21), 4349 (2025)（[论文页](https://www.mdpi.com/2079-9292/14/21/4349)；web 查询 #3 结果 [1](https://www.mdpi.com/2079-9292/14/21/4349)） | 在同一组 NLP 任务的增量多任务 prompting 中反转任务引入顺序，报告顺序变化会改变部分任务表现；这是最直接的 prompt/task-order 近邻。 | 多个 task instruction 堆在**一个 prompt**，不是阶段间多次调用；逆序实验仍把 JSON 任务固定在首位，也没有穷举排列。方法部分称只在两个模型上做逆序，而结果部分又报告六个模型，存在方法/结果口径不一致，引用时应注明。 |
| Ying, Vazquez & Xu, “Prompt engineering using order-of-addition experiments…”（2026，[arXiv:2607.05537](https://arxiv.org/abs/2607.05537)；web 查询 #2 结果 [2](https://arxiv.org/html/2607.05537v1)） | 将 order-of-addition 设计用于静态 prompt 的元素/指令顺序，系统估计排列效应并搜索较优配置；适合说明 prompt 顺序本身可以被设计成实验变量。 | 排的是**同一 prompt 内的组成元素**，不是先后运行的阶段、状态转移或多轮 suffix policy。 |
| Wu et al., “From Seeing to Thinking…”（ICML 2026，[arXiv:2605.20177](https://arxiv.org/abs/2605.20177)；web 查询 #1 结果 [2](https://arxiv.org/html/2605.20177v1)） | 将 VLM 后训练拆为视觉感知、文本推理、视觉推理阶段，比较 staged/merged 训练及若干阶段次序和阶段消融。 | 属于训练数据/参数更新的 curriculum 顺序，不是推理时保持模型固定、仅更换 prompt 序列。可视为“阶段顺序可能重要”的外部支持，不能当作本实验的直接先例。 |
| Suppa et al., “RAGthoven at SemEval-2026 Task 1…”（SemEval 2026，[ACL Anthology](https://aclanthology.org/2026.semeval-1.416/)，[arXiv:2607.13189](https://arxiv.org/abs/2607.13189)；web 查询 #14 结果 [1](https://aclanthology.org/2026.semeval-1.416/)） | 实际系统包含 Planner → Writer → Reflector → Judge 多阶段流程，报告十种配置并探索 agentic tool-calling 变体；作者未在 held-out 英文样本中观察到 agentic 版本优于非 agentic pipeline 的明显质量优势。 | 是多阶段 pipeline 的实验案例，但没有在同任务、同初始状态下系统置换阶段顺序，也没有 canonical / verify deletion / minimal 的配对比较。 |
| MIPRO（EMNLP 2024，[arXiv:2406.11695](https://arxiv.org/abs/2406.11695)；web 查询 #23 结果 [1](https://arxiv.org/abs/2406.11695)）；AFlow（[arXiv:2410.10762](https://arxiv.org/abs/2410.10762)） | 前者优化多阶段 LM program 的模块指令/示例；后者搜索代码化 workflow 图。它们说明多阶段程序结构和模块 prompt 是活跃研究对象。 | 优化模块内容/搜索图结构，不等于从一个冻结 checkpoint 开始，对可比的后续阶段序列做受控因果对照。 |
| PIVOT（[arXiv:2605.11225](https://arxiv.org/abs/2605.11225)；web 查询 #20 结果 [2](https://arxiv.org/html/2605.11225)） | PLAN–INSPECT–EVOLVE–VERIFY 式流程做阶段消融，局部修复时保留已验证前缀并重生成后缀。 | 是 stage ablation 与 prefix-preserving repair 近邻；并未对同一中间状态比较多套后续 prompt 序列。 |

**归纳**：不能把本项目写成“首次发现 prompt 顺序会影响 LLM”或“首次消融多阶段 workflow”。较窄、较稳妥的潜在增量是：**对一个有持久树状态/索引/验证结果的多调用 pipeline，配对固定起始 checkpoint，比较后续 prompt 序列政策，并用连续 gold-tree depth 及成本共同评估**。该“同构设计未找到”的置信度最多 **0.55**；本次检索不能支持绝对首创声明。

---

## §C2 从中间状态用不同后续策略续跑并比较终态

### Verdict：**部分（强近邻）**（conf = 0.82）

| 判据 | Verdict | conf | 判断边界 |
|---|---|---:|---|
| 固定中间状态换后续策略续跑、比较终态是否有先例？ | 部分（强近邻） | 0.82 | handoff/context 表示与 reasoning-prefix continuation 均有先例；同一 SM checkpoint 上的四种阶段后缀序列未找到，否定性判断 ≤0.55。 |

“接手同一 checkpoint 后，给 successor 不同上下文/交接信息，观察后续成功率或成本”已有相当接近的 benchmark；推理轨迹研究也会从同一部分 reasoning prefix 采样不同 continuation。因此路径依赖/续跑作为研究问题并不空白，但任务域、干预对象和终点指标与本 SM 设计仍有差别。

| 反例 / 近邻 | 固定什么、改变什么 | 与 T-PR-17 的差别 |
|---|---|---|
| *Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks*（EMNLP 2026，[ACL Anthology](https://aclanthology.org/2026.emnlp-main.738/)，[arXiv:2606.02875](https://arxiv.org/abs/2606.02875)；web 查询 #4 结果 [3](https://aclanthology.org/2026.emnlp-main.738.pdf)） | 在固定的 repository checkpoint / handoff point 上比较 repo-only、raw trace、summary notes、structured notes 四种 successor handoff view；75 个 SWE-bench Verified source tasks 产生 181 个 handoff points，并测接手后的解决率、agent events 和 tokens。 | **强 checkpoint 设计近邻**；改变的是 predecessor 信息如何呈现给接手 agent，不是相同 SM 树状态下 canonical、删 verify、置换或 minimal 的阶段 prompt suffix。主要结果还包括成本，不是 gold 树深度。 |
| *Benchmarking Task Takeover Across Agent Handoffs* / HSC-Bench（[arXiv:2610.36523](https://arxiv.org/abs/2610.36523)；web 查询 #4 结果 [2](https://arxiv.org/html/2610.36523v1)） | 1,039 个任务；固定 source history 与 handoff point，比较接收模型、structured state、recent transcript 等上下文条件；包括 300 个 repository evidence-recovery 与 739 个 state-dependent continuation tasks。 | 同 checkpoint / history 的接手表现近邻；主要研究 context representation 与 receiver 差异，而非一个模型按不同 SM 阶段序列继续。按 2026-11-24 可核实状态称 arXiv preprint；页面出现的 ACM Web Conference 2027 是未来会期，不据此称已发表/接收。 |
| *The Handoff Tax*（[arXiv:2608.24358](https://arxiv.org/abs/2608.24358)；web 查询 #17 结果 [1](https://www.alphaxiv.org/abs/2608.24358)） | 在 SWE-bench Verified 接手任务中保留 repository 工作区，改变是否向 successor 传递完整轨迹/summary 等信息，并在多个 handoff 点比较模型交接方向；报告效果依赖 predecessor/successor 能力方向。 | 强固定 repository-checkpoint 近邻，但操纵的是跨模型轨迹/交接信息，不是同一 SM 内部的阶段顺序。 |
| Zhu et al., *Dissecting Failure Dynamics in Large Language Model Reasoning*（ACL 2026，[ACL Anthology](https://aclanthology.org/2026.acl-long.401/)，[arXiv:2604.14528](https://arxiv.org/abs/2604.14528)；web 查询 #11 结果 [4](https://aclanthology.org/2026.acl-long.401/)） | 在同一个有效 reasoning prefix 上生成不同局部 continuation（含不同的短提示/分支），分析失败是否可从同一状态恢复；论文报告一部分错误轨迹可由替代 continuation 修复。 | 是“相同前缀、不同续写”的直接机制近邻；状态是单条推理轨迹的文本 prefix，不是有工具、索引、核验状态的 agent checkpoint，也不测试四种阶段序列。 |
| *Beyond the Last Answer*（ICLR 2026 OpenReview submission，**Reject**；[OpenReview 记录](https://openreview.net/forum?id=r57fj2b5N9)，[arXiv:2504.20708](https://arxiv.org/abs/2504.20708)；web 查询 #6 结果 [5](https://arxiv.org/pdf/2504.20708)） | 从一条 reasoning trace 的多个 subthought 端点分别续写，再汇总答案；OpenReview 记录明确为 ICLR 2026 Reject。 | 说明从中间推理点续写已有研究；不是固定单 checkpoint 下对不同 pipeline prompt suffix 的控制实验。审稿人指出采样预算/自一致性 baseline 等限制，不能把该工作当成强结论证明。 |
| *Probing the Trajectories of Reasoning Traces*（NeurIPS 2026 E&D，[arXiv:2601.23163](https://arxiv.org/abs/2601.23163)；web 查询 #19 结果 [1](https://arxiv.org/pdf/2601.23163)）；AgentBaton（[arXiv:2610.35959](https://arxiv.org/abs/2610.35959)；web 查询 #18 结果 [1](https://arxiv.org/html/2610.35959v1)） | 前者截断/重注入部分 reasoning trace 并控制续写条件；后者改变 agent handoff 方向、时机和 context transfer。 | 前者不是有状态多阶段工具 pipeline；后者不是固定同一个 SM checkpoint 的阶段顺序对照。两者是 trajectory/suffix 与 transfer 的邻近研究。 |

**归纳**：C2 不应写成“无人从中间状态继续”。更准确的差异化陈述是：当前近邻分别研究 **handoff 表示/信息量** 或 **reasoning prefix 的局部替代续写**；本实验将这些问题落实为同一 SM 树 checkpoint 上的 **阶段级 suffix policy 干预**，并观察 depth、验证状态和成本。对“没找到完全同构先例”的置信度 **≤0.55**。

---

## §C3 长上下文指令位置效应与 pipeline 序列效应

### Verdict：**位置效应是可信的中介/调节机制，但不足以单独解释序列效应**

| 判据 | Verdict | conf | 判断边界 |
|---|---|---:|---|
| 长上下文位置效应能否传导到 pipeline 序列效应？ | 能贡献一部分，但不足以单独解释 | 0.88 / 0.86 | 位置敏感性证据强；其对本 SM 实验的效应大小未知，且不能替代状态更新、工具与语义依赖机制。 |

| 文献 | 与位置机制相关的实证 | 对本实验的含义 |
|---|---|---|
| Liu et al., *Lost in the Middle*（TACL 2024，[论文页](https://aclanthology.org/2024.tacl-1.9/)，[arXiv:2307.03172](https://arxiv.org/abs/2307.03172)；web 查询 #7 结果 [3](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long)） | 在长上下文 QA / retrieval 中移动关键信息位置；表现常在开头或末尾较好、在中段下降。 | 重新排序或删除阶段会改变指令相对位置、上下文长度及其到生成位置的距离，可能改变模型能否取用某条阶段指令/证据。 |
| Liu et al., *Instruction Position Matters in Sequence Generation with LLMs*（Findings ACL 2024，[ACL Anthology](https://aclanthology.org/2024.findings-acl.693/)；web 查询 #22 结果 [1](https://aclanthology.org/2024.findings-acl.693/)） | 在指令微调样本的串接序列中，将任务指令从输入前移到输入后并与传统排列比较；报告翻译、摘要等序列生成表现改善。 | 支持指令位置会影响学习/生成表现，但这是训练数据布局干预，并非固定模型推理时重排同一 prompt，更非跨调用状态转移。 |
| Veseli et al., *Positional Biases Shift as Inputs Approach Context Window Limits*（COLM 2025，[OpenReview](https://openreview.net/forum?id=vlUk8z8LaM)，[arXiv:2508.07479](https://arxiv.org/abs/2508.07479)） | 以输入长度相对模型 context window 衡量位置偏差；报告 LiM 在输入较短时明显，接近窗口上限时 primacy 变弱、recency 相对稳定，可能转为距离末端偏差。 | 不应把“长 prompt 一律 U-shaped lost-in-middle”当成固定规律；必须记录实际 token length / window ratio，并在目标模型上测。 |
| Guo & Vosoughi, *Serial Position Effects of Large Language Models*（Findings ACL 2025，[ACL Anthology](https://aclanthology.org/2025.findings-acl.52/)；web 查询 #21 结果 [1](https://aclanthology.org/2025.findings-acl.52/)） | 分析 LLM 的 serial-position effects，并讨论位置与任务、模型及 prompt 形态之间的差异。 | 作为一般位置敏感性近邻；不是 pipeline stage order 的因果研究。 |

**机制映射与边界**：

1. `阶段顺序/删减 → 指令与证据的 token 位置、长度、recency 改变 → 阶段指令被注意/检索的概率改变 → 后续输出改变`，这条传导路径合理，且有长上下文位置研究支持。
2. 对“阶段重排”而言，位置通常是**处理后的中介**，不只是外生混杂因素：若目标是估计整套序列改变的总效应，应保留位置路径；若要声称是阶段语义/依赖本身产生影响，则需另设长度匹配、位置 counterbalance 等对照。删除 verify / minimal 同时改变 token 数、调用数、指令位置和外部检索/核验信息量，不能把效应只归因于“少了 verify 语义”。
3. 若各阶段是分开的 API 调用，lost-in-middle 对单次调用内部历史的影响仍可能存在，但它不能解释 verify 是否执行、工具返回了什么、树状态/索引如何更新、后续节点是否引用正确 parent 等跨阶段状态转移。
4. 所以 C3 的结论是：位置效应可能解释总序列效应的一部分，尤其是长上下文和 prompt 长度变化条件；它不足以单独说明终态 depth 差异。对位置效应“可能参与”的信心高；对其在本实验中特定贡献大小的信心低，需实验分离。

---

## OpenReview 2025–2026 定向核验

按任务要求对 2025–2026 的 OpenReview 论文/投稿单独查验。下表是近邻，不等于精确先例；状态按 2026-11-24 页面记录。

| OpenReview 记录 | 页面所示状态 | 相关性与不匹配处 |
|---|---|---|
| [HMAW, RVvXOrP2qm](https://openreview.net/forum?id=RVvXOrP2qm) | ICLR 2025 Workshop LLM Reason and Plan，Published | 先分层构造 prompt 再生成答案；是多阶段 prompt hierarchy，但无同一 checkpoint 的阶段次序消融。 |
| [Workflows vs Agents for Code Translation, U1emjvJ7Gi](https://openreview.net/forum?id=U1emjvJ7Gi) | NeurIPS 2025 DL4C poster | 对比固定 script 与 MCP agent，并隔离 syntax-repair 阶段；不是 prompt 阶段排列/续跑对照。 |
| [HIDO, 9FAm023EmI](https://openreview.net/forum?id=9FAm023EmI) | NeurIPS 2025 poster | many-shot demonstration order 优化；顺序对象是示例而非 pipeline stages。 |
| [Beyond the Last Answer, r57fj2b5N9](https://openreview.net/forum?id=r57fj2b5N9) | ICLR 2026 submission，Reject | 同一 reasoning trace 的 subthought continuation 近邻；不含 stateful SM 阶段变体。 |
| [TAVO, dkbQwUp9gW](https://openreview.net/forum?id=dkbQwUp9gW) | ICLR 2026 submission，Withdrawn | 轨迹级 prompt 优化/credit assignment；优化 prompt，不是固定 checkpoint 下的后续序列因果比较。 |
| [Context Bias Calibration, UubLs3lUfk](https://openreview.net/forum?id=UubLs3lUfk) | ICLR 2026 submission，Reject | 多轮 agent 中周期性裁剪 context 以减轻 conversational inertia；是历史长度/上下文干预近邻，不是 SM stage-order 实验。 |
| [COLM 位置偏差, vlUk8z8LaM](https://openreview.net/forum?id=vlUk8z8LaM) | COLM 2025，Accepted | C3 位置效应的直接来源；研究输入长度和证据位置，不是阶段序列。 |

本次定向 OpenReview 搜索没有发现与四臂 SM 后缀序列实验完全一致的记录；由于论坛搜索及关键词存在覆盖盲区，该否定性判断 conf ≤0.55。

---

## §检索记录

**渠道**：web search（发现候选）、arXiv `abs` / HTML（核对 ID 与方法）、ACL Anthology（核对正式出版元数据/摘要）、OpenReview（核对投稿/会议状态）；另读取了本仓库任务书、实验分解及相关阶段消融背景。下列为本次复核的逐字查询及检索结果；候选进入结论前再以原始页面核对。搜索结果页仅作发现线索，非原始论文页面不作为单独证据。 正文括号中的“web 查询 #n 结果 [m](URL)”表示第 n 条查询的 m 号结果，链接沿用该结果的原 URL。

### Web search 查询记录

| # | 通道 | 原样 query | 结果 / 处理 |
|---:|---|---|---|
| 1 | Web search | `"stage order" LLM pipeline prompt ablation different ordering stages 2025 2026` | 找到 VLM 后训练阶段顺序工作（arXiv:2605.20177）及训练 recipe 类候选；保留前者作阶段顺序近邻，不误作推理 prompt 序列先例。 |
| 2 | Web search | `multi-stage prompt sequence ordering LLM workflow stage permutation experiment` | 命中 prompt order-of-addition（arXiv:2607.05537）、procedural step ordering、ICL example ordering 等；区分同一 prompt/示例排序与跨调用 pipeline stage。 |
| 3 | Web search | `task order multi-task prompting reverse order sequence LLM fixed dataset` | 命中 Di Maio & Gozzi 的固定任务序列及逆序实验；另有 Set-Based Prompting，后者处理输入子序列顺序，不是多阶段 agent pipeline。 |
| 4 | Web search | `fixed checkpoint agent handoff context transfer successor performance LLM benchmark` | 命中 Handoff Debt 与 HSC-Bench；作为 C2 强近邻，随后读原文方法。 |
| 5 | Web search | `handoff same repository checkpoint raw trace summary structured notes successor agent performance` | 命中 Handoff Debt 的四种 handoff view、Handoff Tax 及固定 repository 状态比较；只把原论文作为证据。 |
| 6 | Web search | `intermediate state continuation reasoning trajectory same prefix alternative continuation LLM prompt` | 命中 GUARD、ThinkReset、Beyond the Last Answer、Prefix-GRPO。Prefix-GRPO 的 arXiv 记录显示因 Pass@8 使用不完整任务集而撤稿，未作为可靠结果依据。 |
| 7 | Web search | `lost in the middle instruction position long context serial position effects LLM 2025 2026` | 命中 LiM、指令位置、相对 context-window 长度与 serial-position 研究；据正式 TACL/ACL/OpenReview 页面核对。 |
| 8 | Web search（OpenReview 定向） | `site:openreview.net/forum LLM stage order workflow pipeline ablation 2025 2026` | 返回阶段化 workflow、训练/规划和模块级近邻；未见同一固定 checkpoint 的 prompt-stage 后缀比较。候选逐项按 OpenReview 页面复核。 |
| 9 | Web search（OpenReview 定向） | `site:openreview.net/forum LLM agent handoff checkpoint continuation intermediate state 2025 2026` | 返回多轮 context、handoff/trajectory 等近邻；未将搜索摘要直接当作状态结论，改查 OpenReview 原页。 |
| 10 | Web search | `pipeline stages permutation prompt order experiment LLM multi-stage 2024 2025` | 命中 MIPRO 多阶段模块 prompt 优化、prompt-element ordering 等；用来划分“优化模块”与“重排阶段”的差别。 |
| 11 | Web search | `"Dissecting Failure Dynamics in Large Language Model Reasoning" OpenReview 2604.14528 venue` | 核实 GUARD 为 ACL 2026 long paper（ACL Anthology 2026.acl-long.401）；用作 same-prefix local continuation 近邻。 |
| 12 | Web search | `"InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning" ICLR 2026` | 找到 ICLR 2026 出版记录；作为训练时局部纠错近邻，不作固定推理 prompt 序列先例。 |
| 13 | Web search | `"Stage-Replay Divergence Follows the KV Cache" 2607.28495 venue` | 找到固定 token prefix / live-vs-prefill KV 状态比较；搜索索引另显示可能的 GEM workshop 元数据，但 arXiv abs 未列 venue、未以 ACL Anthology 核实，因此不据此标注 venue。 |
| 14 | Web search | `"RAGthoven at SemEval-2026 Task 1" 2607.13189 stage ablation venue` | 核实 SemEval 2026 ACL Anthology 正式页面；作为 pipeline 实例，不视为 stage-order 对照。 |
| 15 | Web search | `"Stage-Replay Divergence Follows the KV Cache" ACL GEM 2026` | 精确 venue 查询未返回可核实的 ACL Anthology 书目页；出版地位仍不确定，故本报告只按 arXiv 记录描述。 |
| 16 | Web search | `"2607.05537" publication venue "Prompt engineering using order-of-addition experiments"` | 结果仅支持 arXiv:2607.05537 记录；未核实正式 venue，因此写作 arXiv 预印本。 |
| 17 | Web search | `"The Handoff Tax" arXiv 2608.24358 agent handoff checkpoint` | 找到 Handoff Tax 的 handoff 方向/时点/context transfer 对照；用于 C2 强近邻。搜索结果页为发现入口，报告引用 arXiv abs。 |
| 18 | Web search | `"AgentBaton" 2610.35959 agent handoff context transfer arXiv` | 命中 AgentBaton 原始 arXiv HTML，核实其在 workspace handoff 后续跑并比较 history/logfile transfer。 |
| 19 | Web search | `"Probing the Trajectories of Reasoning Traces" 2601.23163 NeurIPS 2026` | 核实 trajectory truncation/reinjection、长度/形式/token 对照及 NeurIPS 2026 E&D 标注；作 reasoning-prefix 近邻。 |
| 20 | Web search | `"PIVOT" 2605.11225 PLAN INSPECT EVOLVE VERIFY arXiv` | 核实四阶段轨迹修复、保留已验证 prefix 重写 suffix，并做各阶段删除消融；不是同 checkpoint 多套 pipeline 序列。 |
| 21 | Web search | `"Serial Position Effects of Large Language Models" ACL Anthology 2025` | 返回 ACL Anthology 正式记录；用于一般 serial-position 近邻，不外推为 pipeline stage order。 |
| 22 | Web search | `"Instruction Position Matters in Sequence Generation with Large Language Models" ACL Anthology 2024` | 返回 Findings ACL 2024 正式记录和摘要；支持指令位置对序列生成有影响。 |
| 23 | Web search | `"MIPRO" 2406.11695 EMNLP 2024 multi-stage language model programs` | 返回 arXiv/HTML 原始页面；核实 MIPRO 是多阶段 LM program 的模块指令/示例优化，不能等同阶段重排。 |
| 24 | Web search | `"Positional Biases Shift as Inputs Approach Context Window Limits" COLM 2025 OpenReview 2508.07479` | 搜索引擎返回相关二手综述及引用；正式状态和发现由本报告直接读取的 COLM OpenReview 与 arXiv abs 页面核验，未引用二手页作事实依据。 |

### 原始页面核验与 OpenReview 检索记录

- **arXiv `abs` 直核**：本报告引用的 ID `2307.03172`、`2406.11695`、`2410.10762`、`2504.20708`、`2508.07479`、`2601.23163`、`2604.14528`、`2605.11225`、`2605.20177`、`2606.02875`、`2607.05537`、`2607.13189`、`2607.28495`、`2608.24358`、`2610.35959`、`2610.36523` 均通过对应 `https://arxiv.org/abs/<id>` 页面核对标题、作者/摘要及页面可见的出版状态。另核对 `2601.14209`、`2511.09700`、`2607.19395`；后者因撤稿仅记为排除项。
- **ACL Anthology**：核对 *Handoff Debt* `2026.emnlp-main.738`、GUARD `2026.acl-long.401`、RAGthoven `2026.semeval-1.416`、*Lost in the Middle* `2024.tacl-1.9`、*Instruction Position Matters* `2024.findings-acl.693`、*Serial Position Effects* `2025.findings-acl.52`。
- **OpenReview 原页**：除上表 ID 外，候选 `a7Qa4CcHak` 直接打开实际为 *Terminal-Bench*，并非 AgentBaton，已排除；`sRJPXKCHxU` 跳转登录页，无法直接核实，未引用。AgentBaton 使用 arXiv abs `2610.35959`，不使用错误 OpenReview ID。
- **已排除/降权**：`2607.19395` 标记 withdrawn，作者说明部分 Pass@8 值使用不完整 task set；未用于支撑任何效果结论。HSC-Bench 页面中的未来 2027 venue 字样不当作当前已接收证据。

### 首轮滚雪球检索主题（作为补充记录）

此前检索还覆盖：workflow/stage order、checkpoint/handoff、position bias；ICML/NeurIPS/ICLR 2025–2026 的 OpenReview-only 论文；Handoff Debt、HSC-Bench、AgentBaton、固定 handoff/checkpoint；以及 MIPRO、AFlow、PIVOT、reasoning-trace continuation。首轮原始 query 逐字串未在当前工作记录中保留，因此不把以下主题伪称为 verbatim query；其使用的关键 arXiv ID 和 OpenReview 页面均按上面的原始页面核验。检索结果包括 HMAW（RVvXOrP2qm）、Workflows vs Agents（U1emjvJ7Gi）、HIDO（9FAm023EmI）、TAVO（dkbQwUp9gW）、Beyond the Last Answer（r57fj2b5N9）、COLM position-bias（vlUk8z8LaM）等。

---

## §方法学缺口与 T-PR-17 设计建议

1. **先定义估计量，别把四个变体当作同一单因子。**
   - *Operational total effect*：实际删除 verify / 改用 minimal 后，质量与 token、工具调用成本一起变化；这回答“能否简化流程”。
   - *Sequence-mechanism effect*：阶段语义/执行次序本身的作用；需额外控制 token 长度、指令位置、可用 evidence 和计算预算。两种问题应分别报告。
2. **冻结并审计同一 checkpoint。** 每个 task × seed × L1/L2/L3 checkpoint 复制成只读分支；核对节点 ID、`parent_ids` 闭包、层级/索引、verified/degraded 状态、corrected claim、证据、轮数、配置和随机种子。分解记录明确标注 `parent_ids` 持久化风险；实验前先做 JSON schema + parent-link integrity 检查。任何一臂的恢复失败都记录为结果，不静默剔除。
3. **把外部信息和状态副作用分开。** 若 verify 会联网/过滤/改写节点，删除 verify 不只是删一段文字，也改变证据集与树状态。若研究目标是“verify 阶段整体的 operational value”，保留该复合干预并报告 tool calls / evidence；若要识别 prompt 序列本身的作用，应冻结同一 evidence snapshot 并 replay 工具返回，另设 live-tool 条件。
4. **对照 prompt 长度、位置和可执行预算。** canonical、permutation 及 stage removal 改变指令位置、上下文长度和后续生成距离。至少记录各调用 token 数与 context-window 比例；将同一阶段内容在可行位置间 counterbalance；对 minimal 加长度匹配的中性/格式控制版本。建议同时报告自然成本预算与等 token/等 tool-call 预算两种结果，不把“省了预算”误当成纯语义效果。
5. **预先定义可置换阶段集合。** 若某阶段依赖 verify 结果或 parent/index 字段，在它之前运行 verify 可能是刻意违反依赖；应明确区分“可执行的拓扑顺序”与“依赖破坏压力测试”，记录失败/无效调用，避免将结构错误混成一般顺序噪声。
6. **成对重复并以 task/checkpoint 为统计单位。** 每个 variant 从同一状态成对运行、随机化执行顺序；模型/API 版本、解码参数、max depth、工具环境和输出预算固定或分层。≥3 reps 只是最低起点，单一 GPU 题外推有限；建议增加独立题目/多个 checkpoint。用按 task/checkpoint 聚类的 bootstrap CI 或配对分析，报告效应量和方差；若要声称“无影响”，需预设最小重要效应并做等效性检验，而不是用“不显著”代替“相同”。
7. **depth 分数需避免奖励浅树或节点膨胀。** 预注册 gold-tree 连续评分，至少并列报告深度、节点覆盖/precision、parent-link 正确率、verified 比例、重复/缺失状态和失败率；盲化评分并估计 judge 噪声。保留 token / tool / wall-time 成本曲线，分别说明“更深”与“更省”。
8. **说明 checkpoint 的状态层级。** JSON 树状态、对话文本历史与模型运行时 KV/cache 不是同一状态。*Stage-Replay Divergence Follows the KV Cache*（[arXiv:2607.28495](https://arxiv.org/abs/2607.28495)）在单一 Qwen2.5-derived 设置中报告：相同 token prefix 的 fresh prefill 与 retained live cache 可能产生不同后缀；这是一个实现相关的警示，不应泛化为所有 API。若本实验只能序列化树 JSON 和文本 prompt，应将 treatment 定义为“同一 text/SM checkpoint 的重建续跑”，不要宣称恢复了完全相同的隐状态/KV checkpoint。

**执行前最低验收**：冻结 checkpoint → 校验 parent/index 与 evidence → 先跑一组可行 permutation smoke test → 输出每臂实际 prompt/token/工具调用清单 → 再开正式配对 runs。按 decomp 计划的每 cell ≥3 reps 可作 pilot，但不足以单独支持强无效结论；judge 差异小于既有噪声时应报告“当前设计不可检测”，而非“序列无影响”。

---

## 对外 claim 建议

建议表述：**“已有研究研究 prompt/order sensitivity、阶段化 workflow、agent handoff 和从 reasoning prefix 续跑；我们未在本次检索中发现与固定 SM checkpoint 上四种后续 prompt 序列、并以 gold-tree depth 比较的完全同构实验。我们提出并测试的是一个更窄的 stateful pipeline suffix-ablation 设计。”**

不要写成：“首次证明 LLM 有顺序效应”“此前没有 checkpoint continuation 实验”或“lost-in-the-middle 已解释我们的 pipeline 差异”。