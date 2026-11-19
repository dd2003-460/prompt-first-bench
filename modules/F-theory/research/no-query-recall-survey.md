# T55：LLM“知道但未主动调用”的术语与证据调查

检索截至 2026-11-09；文献研究，不是本仓库模型实验。置信度是对**所述范围内结论**的主观判断，不是统计置信区间。文末给每篇原文位置及可点击标识；预印本结论不等于已独立复现。

## 摘要与界定

**Q1：未找到覆盖完整现象、跨研究公认的单一专名（not found，置信度中）。** 推荐工作性描述 *cue-/context-dependent access to parametric knowledge*（线索／上下文依赖的参数知识访问；这是本文描述而非声称已有的正式术语）。最接近但更窄的正式可操作概念是 **compositionality gap**：子问题都能分别回答而组合问题失败 [S1]。人类记忆的 **cue-dependent forgetting** [S2] 是类比，不是 LLM 已被证明发生同一记忆机制。**ELK** 和 **capability elicitation** 是正式相邻研究方向，不是该现象的同义词 [S3,S4]。"stored but inaccessible"、"dormant knowledge" 和知识激活是实际用语，但不应凭少数论文宣布其为全领域统一专名 [S5,S6]。

“无提示”必须操作化：对普通 LLM，若既无输入也无生成触发，模型不会自行运行；真正值得检验的是**给定实际任务和上下文，但未明确提示某条相关知识或要求提醒**，模型能否自发提及、正确应用。区分四层：①训练数据包含事实／参数可能编码；②内部可探测或单独询问可答；③当前任务真正使用；④用户没有明确询问该风险时主动提醒。①不保证②，②不保证③，③也不保证④；不输出可能是任务无关、信息不够、选择性简洁、拒答、知识缺失或推理失败，而非单一“遗忘”。本文多数来源测试②→③，④直接实证仍少。

## Q1：逐项术语判决

每个 **found** 指确有词语／方向或定义，而非自动意味着与用户现象完全等价；not found 仅表示本次查询、语料和索引范围内未找到，不能证明不存在。每项引用是来源原文片段，不把作者的推论当定义。

| 候选 | 判决与原文 | 与问题的距离 / 判决置信度 |
|---|---|---|
| **no-query recall** | **not found（目标专名）**。精确检索命中 GitHub 中无查询列出外部记忆的用法，不是参数知识现象 [W1]。近邻：开放知识评估、参数知识访问、cue-dependent forgetting [S7,S8,S2]。 | 词串有其他实际用法；中。 |
| **query-less recall** | **not found（目标专名）**。独立精确检索命中外部记忆开关/空查询，以及外部持久记忆讨论 [W2]；近邻同上。 | 非“完全无此词”；中。 |
| **latent knowledge activation** | **found（相关描述/论文方法名，不确认为统一术语）**。[S5] 引言：“models may fail to recall factual knowledge within their parameters, an issue defined as ‘stored but inaccessible’”；摘要称其方法 “externalizes latent parametric knowledge through explicit Priming”。 | 有事实存储—访问分离，但该实验仍有 query、外部检索子图和训练；中高。 |
| **eliciting latent knowledge / ELK** | **found（正式研究方向）**。[S3] 摘要：“Eliciting Latent Knowledge (ELK) aims to find patterns in a neural network’s activations that robustly track the true state of the world, even in cases where the model’s output is untrusted and hard to verify.” | 关注监督、真实性和探针，即使模型输出不可信；不专指未被提醒时遗漏；高。 |
| **knowledge ungrounding** | **not found（目标专名）**。近邻：stored but inaccessible [S5]、fact recall [S9]、cue-dependent forgetting [S2]。另有 **symbol ungrounding** [S18]，是具身语义/抽象概念的问题，不等同未调用知识。 | 检索到的是相关但不同问题；中。 |
| **dormant knowledge** | **found（描述性措辞）**。[S6] 摘要：“construct preference data to dynamically ‘Wake Up’ dormant knowledge or ‘Suppress’ blind guessing.” | 原文用于有问题时的已掌握知识但犹豫/拒答，经偏好优化训练；有用描述但尚不足证明统一定义；高（存在），低中（完全匹配）。 |
| **cue-dependent forgetting** | **found（认知科学 established 术语）**。[S2] 摘要：“Presentation of category names as retrieval cues largely removed retroactive effects and restored word recall to nearly its original level.” 接着将可用但不可访问状态称为 “an instance of cue-dependent forgetting”。 | 128 名被试的清单记忆与分类提示，属于行为类比而非模型机制证据；高。 |
| **parametric knowledge vs prompted retrieval** | **found（清楚的存储/访问区分，非固定二元专名）**。[S9] §1：“We refer to this ability to retrieve stored facts using an unseen query as Fact Recall.” [S8] 摘要：“models do not generate their best world knowledge reasoning by default”。 | 参数知识是可能的存储位置；prompted retrieval 是提取过程，两者并非互斥。事实可被上下文新提供；高。 |
| **capability elicitation / 知道但不做** | **found（正式研究问题）**。[S4] 摘要：“we evaluate the effectiveness of capability elicitation techniques by intentionally training model organisms – language models with hidden capabilities that are revealed by a password.” | 研究评估条件下能否诱发潜在能力，范围含技能、故意压制和工具使用；密码锁是人为构造，不证明普通遗漏是策略性隐藏；高。 |

另外 [S1] §1 精确定义：“the fraction of compositional questions that the model answers incorrectly out of all the compositional questions for which the model answers the sub-questions correctly.” 它对“问子问题知道、组合时不会用”最贴近且可实测，但要求特定的多跳任务，不能覆盖所有无提醒的主动行为。

## Q2.1 什么时候调用或不调用？（结论：情境依赖，置信度中高；主动提醒外推低）

- **组合任务更难调用**：[S10] 先筛选两个单跳问题分别可答的样本，再比较两跳推理中事实知识神经元得分。三模型 no-CoT 两事实得分相对单跳基线均降低，例如 Mistral-7B 为 −10.84% 与 −11.77%（相对变化，不是准确率百分点）。作者还做神经元增强/抑制；支持与事实访问有关，但预选样本、神经元识别和知识表征代理限制因果解释，不能断言所有失败都是未检索。另 [S1] 构造子题答对而总题错的 compositionality gap，既可能涉及组合计算也可能涉及访问。
- **无显式属性提示也可能产生内部关联**：[S11] 对 Llama 系列元素属性实验发现，中间层可探测相关但非明确询问的属性，后层按任务收缩。内部可解码不等于生成答案时采用，更不等于主动向用户提示；probe 的结果依赖模板、层和方法。它是“并非不问就完全没有激活”的反证。
- **默认方式和线索影响效果**：[S8] 四个推理模型、两个闭卷 QA，逐步思考 cue 的平均 Ex-Recall 相对无 cue **+0.8 个百分点**；GPT-OSS-20B TriviaQA 60.1→61.2、NQ 30.7→32.0。后者表中 NQ 该单项没有显著性星标；不要把整体趋势说成每个比较均显著。这是已有问题下的默认访问，而非无用户请求。
- **开放任务下输出选择也变**：[S7] 用 10,000 实体建立 BeQu，实验多数抽样 200 实体；GPT-5.4 要求不同数量三元组时，较高数量设置 recall 25.6→36.8%，precision 维持 72–85%。更长输出和目标数量是干预，LLM judge 及参照语料不完备限制真实知识判断。

## Q2.2 干预及实测（置信度：表内局部结果高；归因于纯参数激活中低）

| 干预 | 设置、对照与结果 | 限制 |
|---|---|---|
| 简单 prompt | [S8] 闭卷 QA，base 问题+答案指令对比添加 “think step-by-step”；GPT-OSS-20B 的 TriviaQA Ex-Recall 60.1→61.2%，NQ 30.7→32.0%。 | 不等于用户不问任何问题；输出抽取由另一模型做。 |
| few-shot 知识探测 | [S12] BERT-large，TREx-1p 手写模板 zero-shot 25.8%，5 train + 5 dev 配置下 ICL 手写模板 49.0%；TREx-2p 14.4→47.5%。准确率，非同题个体因果激活；few-shot 示例提供关系和答案类型信息，开发集也参与设置。 | 不可把 BitFit/连续提示调优结果称为纯 ICL；不保证每个示例都使原有事实被访问。 |
| self-interrogation / self-ask | [S1] Davinci-002，所有条件均 few-shot；Bamboogle 125 题人工判分：direct 17.6%、CoT 46.4%、self-ask 57.6%、self-ask+搜索 60.0%；2Wiki 精确匹配分别 25.4、29.8、30.0、40.1%。 | 搜索提供外部信息；Bamboogle 样本小，额外生成计算与格式混杂，不是激活的纯因果分解。 |
| 生成事实 priming | [S13] 同一 hybrid 模型切换 reasoning；抽取其推理时生成的事实，再喂给 reasoning OFF，优于等长度无语义 dummy；生成的相关事实成为后续回答的上下文。SimpleQA-Verified 中干净轨迹最终正确 41.4%，含错误事实轨迹 26.4%，这是观察相关而非随机化因果效应。 | 同时存在计算缓冲；事实生成可能幻觉。检索与验证过程使用外部模型/搜索，不能将全部效果归于纯内部机制。 |
| 递归树分解 | [S14] Llama-3.1-405B、三个 ML 领域，Recursive Taxonomy L5W5 的最终有效去重知识量约为 L2W2 饱和基准 **6 倍**；低预算下多视角策略可能更划算。 | 宽、深、叶节点数与 token 成本同时变化，6 倍**不是深度的独立因果效应**；有效性由模型裁判与去重管线估计，并非已验证真实事实总数，且未证明所有内容原先存于参数。 |
| 外部状态机 | [S15] GPT-3.5-turbo，100 个长度 10 的随机数组，最大可被 3 整除子集和：standard 14%、CoT 37%、CoT-SC 58%、SMoT 95%。SMoT 使用预定义状态与规划/执行代理。 | 数学任务非领域知识主动提醒；外部状态机、算法伪代码、代理分工与多调用混杂，不能推断只有状态机或内部知识激活造成收益。 |
| 层级遍历 | [S16] MedConceptsQA 中 DeepSeek-V3 instruct 相对 R1 的差距：直接问答 23.7 pp，结构化提示 7.5 pp；五模型家族的作者实验支持遍历指导。 | 这是两个模型之间差距的变化，不是同模型绝对准确率提升 16.2 pp；RL 与其他后训练改变权重，非单纯 prompt。 |

## Q2.3 ICL 本质就是 query 触发潜在知识吗？（结论：不能这么概括；置信度高）

- 支持**部分**检索成分：[S17] 真实回归数据中，带有真实语义特征名的示例优于特征匿名化，作者认为名字提示触发先验知识；但数据泄漏、名称本身的语义和任务匹配均可能参与作用。
- 反证“只有激活”：[S17] 例子标签随机化特别是在 100 个示例时恶化，说明模型也对例子输出及其中新模式敏感；不同 prompt 在学习和检索间移动，并不是排他证明。另 [S19] 的线性回归构造与训练实验证明 Transformer **可以**在激活中实现/近似梯度下降及岭回归，参数不更新也能从上下文形成新预测器；它是受控合成任务，不证明每个自然语言 ICL 都实现同一算法。
- [S12] 的 few-shot 提升也可能来自关系类型校准、标签空间和新示例，而非可识别的单一知识激活。因此更准确表述是“上下文既可提供线索来访问已有能力，也可提供本次任务的新信息和模式”。

## Q2.4 分解树深度是否是知识激活强度指标？（结论：本次未找到经验证的通用指标；置信度中）

1. [S14] 确实用 L5W5 和 L2W2 等递归主题树测**提取量—成本**，这是最直接相关证据；但同时改变深度、宽度和叶节点，且没有逐事实内部激活强度验证。其知识 frontier 明确定义为**固定管线下可提取**的有效知识集合，而非模型固有总知识。它测提取的操作结果，不是深度标定过的神经激活强度。
2. [S16] 按外部知识分类层级深度 2–6 分层，报告路径匹配和准确率（每深度 n=20）；知识图谱中的目标距离与模型生成的分解树深度不同，不能互换。模型/路径/问题难度也共同变化。
3. [S20] 使用可执行表达式树控制题目难度；简化表格 Gemma-31B 六步 85%→八步 55%，DeepSeek-v4-Flash 84%→26%，每格 100 题。深度越大反而更难；这衡量计算/检索步骤，不是激活强度。该文表格部分百分比与其所称每格 100 题有精度不一致，因此数字按原文照录，稳健性须复核。
4. [S21] 将思维链/树/图讨论为推理拓扑、计算与成本；[S22] 用树搜索最大深度（可达 64）定义预算和算法搜索空间。它们不是知识神经表征强度测量。深度还依赖粒度（token、句子或主题）、宽度、停止规则、模型和 prompt。

**若要本项目测量**：冻结同模型、提示模板和总 token/调用预算；深度 d、宽度 w 做正交实验，配相同叶节点数及相同候选事实；对每个事实用独立直接 QA 建立“可答”条件，盲审及外部证据验证。报告 `新增正确相关且去重事实数 / 成本`、有害遗漏率、错误率和同题配对置信区间；白盒时另报独立 probe 与因果 patch/ablation。深度只作为**干预/预算变量**，而非预设的“激活强度”；比较直接事实提醒、分解、状态机和等 token 空步骤对照。高风险场景应验证而非强制模型多产事实。

## 来源索引（独立来源；标识与直接原文位置）

- [S1] Press et al., *Measuring and Narrowing the Compositionality Gap*, [arXiv:2210.03350](https://arxiv.org/html/2210.03350), 摘要、§1、§3.4 表1。
- [S2] Tulving & Psotka, *Retroactive inhibition in free recall* (1971), [DOI:10.1037/h0030185](https://doi.org/10.1037/h0030185), [可读摘要](https://www.researchgate.net/publication/232435248_Retroactive_inhibition_in_free_recall_Inaccessibility_of_information_available_in_the_memory_store)。
- [S3] Mallen et al., *Eliciting Latent Knowledge from “Quirky” Language Models*, [arXiv:2312.01037v4](https://arxiv.org/html/2312.01037v4), 摘要。
- [S4] Hofstätter et al., *The Elicitation Game*, [arXiv:2502.02180v3](https://arxiv.org/html/2502.02180v3), 摘要、§1；摘要和引言对 steering 成效表述有细微差异，本文不依赖其具体结论。
- [S5] Ying et al., *From Storage to Access*, [arXiv:2608.18581v1](https://arxiv.org/html/2608.18581v1), 摘要、§1。
- [S6] Lu et al., *Knowing When to Speak*, [DOI:10.18653/2026.findings-emnlp.2451](https://doi.org/10.18653/2026.findings-emnlp.2451), [ACL 摘要](https://aclanthology.org/2026.findings-emnlp.2451/)。
- [S7] Giordano & Razniewski, *Beyond Questions*, [arXiv:2605.26937v1](https://arxiv.org/html/2605.26937v1), 摘要、§6.5、§8。
- [S8] Ma & Hewitt, *Improving Parametric Knowledge Access*, [arXiv:2602.22193v1](https://arxiv.org/html/2602.22193v1), §3 表1、§4。
- [S9] Zhang et al., *Understanding Fact Recall in Language Models*, [arXiv:2505.16178v2](https://arxiv.org/html/2505.16178v2), §1。
- [S10] Wang et al., *Unveiling Factual Recall Behaviors through Knowledge Neurons*, [DOI:10.18653/v1/2024.emnlp-main.420](https://doi.org/10.18653/v1/2024.emnlp-main.420), [PDF](https://aclanthology.org/2024.emnlp-main.420.pdf), §4 表1、§5。
- [S11] Lei & Cooper, *Representation and Recall of Interwoven Structured Knowledge*, [arXiv:2502.10871v1](https://arxiv.org/html/2502.10871v1), 摘要、§2、§4。
- [S12] He et al., *An Empirical Study on Few-shot Knowledge Probing*, [arXiv:2109.02772](https://arxiv.org/abs/2109.02772), [全文](https://ar5iv.labs.arxiv.org/html/2109.02772), §4 表2。
- [S13] Gekhman et al., *Thinking to Recall*, [arXiv:2603.09906v1](https://arxiv.org/html/2603.09906v1), 摘要、§5.1–5.3。
- [S14] Yang et al., *Probing the Knowledge Boundary*, [arXiv:2602.00959v2](https://arxiv.org/html/2602.00959v2), §3–4；预印本，树效应归因与裁判真实性有限。
- [S15] Liu & Shuai, *SMoT: Think in State Machine*, [arXiv:2312.17445v1](https://arxiv.org/html/2312.17445v1), §6.1 表1。
- [S16] Zhang et al., *Reinforcement Learning Improves Traversal of Parametric Knowledge*, [arXiv:2511.05933v2](https://arxiv.org/html/2511.05933v2), §2–4。
- [S17] Nafar et al., *Learning vs Retrieval*, [arXiv:2409.04318v2](https://arxiv.org/html/2409.04318v2), 摘要、§3.3–3.4。
- [S18] Dove, *Symbol ungrounding*, [DOI:10.1098/rstb.2023.0149](https://doi.org/10.1098/rstb.2023.0149), 原刊页面不可抓取；参看该 [关联综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC11391292/) §3。
- [S19] Akyürek et al., *What Learning Algorithm Is In-Context Learning?*, [arXiv:2211.15661](https://arxiv.org/abs/2211.15661), [PDF](https://arxiv.org/pdf/2211.15661), 摘要、§1。
- [S20] Larsen et al., *V-FiLLM*, [arXiv:2608.11047v1](https://arxiv.org/html/2608.11047v1), §4.3、§5.1 表3。
- [S21] Besta et al., *Demystifying Chains, Trees, and Graphs of Thoughts*, [arXiv:2401.14295v3](https://arxiv.org/html/2401.14295v3), 摘要、§I。
- [S22] Feng et al., *AlphaZero-Like Tree-Search*, [arXiv:2309.17179v2](https://arxiv.org/html/2309.17179v2), 摘要、§3、附录 E.5。
- [W1] [GitHub 空查询召回示例](https://github.com/romiluz13/Memongo/issues/115)；软件用法，非论文。
- [W2] [GitHub query-less recall](https://github.com/cryogenized-spec/Elara-Angelic-Utility-Applet/pull/111)；软件用法，非论文。

检索细节、实际查询和否定结论范围见 `no-query-recall-search-log.json`。未做穷尽式系统综述；结果受索引、英文关键词和截止日期限制。
