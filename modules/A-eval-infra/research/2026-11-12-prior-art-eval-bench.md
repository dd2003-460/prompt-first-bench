# 评测基准与 Prompt 消融先例调研（Prior Art: Eval Benchmarks）

**日期**: 2026-11-12
**origin**: ai（基于上轮 web_search 底稿 + 本轮 arXiv API 抽查验证）
**目标**: 为 pfb deepresearch 泛化 bench 提供对标依据，识别空白区与差异化切入点

---

## Q1：现有评测基准全景

### 1. GAIA

| 字段 | 内容 |
|------|------|
| 出处 | Meta AI, 2023, arXiv:2311.12983 ✅已验证 |
| 标题 | GAIA: a benchmark for General AI Assistants |
| 评什么 | 通用 AI 助手能力（多步推理、工具使用、网页浏览） |
| Judge | 规则匹配（exact match / string compare），无 LLM-judge |
| 缺陷 | 无研究质量维度；二元对错无法捕捉部分正确；任务设计偏向"找到答案"而非"产出研究报告" |
| 与我们方案重叠度 | **低** — 我们评的是研究产出质量，不是答案正确性 |
| 可借鉴点 | 任务分层设计（Level 1/2/3 难度递进）可作为我们 bench 的难度分层参考 |

### 2. Humanity's Last Exam (HLE)

| 字段 | 内容 |
|------|------|
| 出处 | Scale AI, 2025, arXiv:2501.14249 ✅已验证 |
| 标题 | Humanity's Last Exam |
| 评什么 | 前沿科学问题（数学、物理、CS 等），考察模型能否解决人类专家水平的问题 |
| Judge | 混合 judge（部分规则匹配 + 部分 LLM-judge） |
| 缺陷 | 难度分布不均（大量题目对当前模型全错或全对）；不覆盖 agent 场景；无研究过程评估 |
| 与我们方案重叠度 | **低** — 静态知识问答，非 agent 工作流 |
| 可借鉴点 | 题目来源的学科多样性设计；judge 混合策略的 trade-off 分析 |

### 3. DeepResearch Bench

| 字段 | 内容 |
|------|------|
| 出处 | 2025, arXiv:2506.11763 ✅已验证 |
| 标题 | DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents |
| 评什么 | Deep research agent 端到端能力（搜索、综合、报告生成） |
| Judge | LLM-judge + rubric（rubric 粒度较粗，通常 3-5 个维度） |
| 缺陷 | rubric 粒度粗，无法捕捉细粒度的研究质量差异；依赖单一 LLM judge 家族，有 self-enhancement bias 风险 |
| 与我们方案重叠度 | **中** — 同为 deep research agent 评测，但我们的 decomp 状态机 + 异族 judge + κ≥0.6 一致性门槛是它没有的 |
| 可借鉴点 | rubric 维度的选取方式；agent 轨迹采集格式 |

### 4. BrowseComp

| 字段 | 内容 |
|------|------|
| 出处 | Meta, 2025（无 arXiv id，仅技术报告） |
| 评什么 | 浏览器操作能力（网页导航、信息提取、多页综合） |
| Judge | LLM-as-judge |
| 缺陷 | 依赖搜索引擎 API（不可复现性强）；不评研究产出质量，只评浏览行为 |
| 与我们方案重叠度 | **低** — 评的是浏览行为，不是研究质量 |
| 可借鉴点 | 浏览器轨迹标注方法；多页信息综合的评分标准 |

### 5. SimpleQA

| 字段 | 内容 |
|------|------|
| 出处 | OpenAI, 2024（无 arXiv id，仅技术报告） |
| 评什么 | 简单事实问答（短答案，单一事实） |
| Judge | 规则匹配 + LLM 混合 |
| 缺陷 | 二元对错无法捕捉部分正确；题目太简单，对前沿模型区分度低 |
| 与我们方案重叠度 | **低** — 单点事实问答，与研究产出无关 |
| 可借鉴点 | 答案格式标准化的做法（便于自动化评分） |

### 6. FActScore

| 字段 | 内容 |
|------|------|
| 出处 | Min et al., EMNLP 2023, arXiv:2305.14251 ⚠️**底稿原写 2305.14474，已修正**（2305.14474 实际是 "Nonlocal anisotropic interactions of Coulomb type"，物理论文） |
| 标题 | FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation |
| 评什么 | 长文本的事实精确率（将文本分解为 atomic facts，逐条验证） |
| Judge | atomic fact 分解 + 逐条 LLM-judge |
| 缺陷 | 分解步骤引入噪声（LLM 分解本身可能出错）；计算成本高（每条 atomic fact 都要单独验证）；只评事实性，不评研究深度/创新性 |
| 与我们方案重叠度 | **中** — 我们的异族 judge 思路与其"逐条验证"思想相通，但我们用 decomp 状态机替代 LLM 自由分解，可控性更强 |
| 可借鉴点 | atomic fact 分解的粒度设计；逐条验证 vs 整体评分的 trade-off |

### 7. RAGAS

| 字段 | 内容 |
|------|------|
| 出处 | GitHub: explodinggradients/RAGAS（开源框架，无正式论文） |
| 评什么 | RAG 系统质量（faithfulness / answer relevance / context relevance） |
| Judge | 混合指标（部分规则 + 部分 LLM） |
| 缺陷 | 依赖 reference answer（需要 ground truth）；指标定义模糊（faithfulness 的计算方式有多种解释）；不覆盖 agent 场景 |
| 与我们方案重叠度 | **低** — RAG 系统评测，非研究 agent |
| 可借鉴点 | faithfulness 指标的设计思路（答案是否被上下文支持）可迁移到"研究结论是否被引用文献支持" |

### 8. HELM

| 字段 | 内容 |
|------|------|
| 出处 | Stanford CRFM, arXiv:2211.09110 ✅已验证 |
| 标题 | Holistic Evaluation of Language Models |
| 评什么 | 多维 holistic 评估（accuracy / calibration / robustness / fairness / efficiency / toxicity） |
| Judge | 各维度独立评分（规则 + LLM 混合） |
| 缺陷 | 不覆盖 agent 场景；holistic 但浅层（每个维度都是单点指标，无过程评估）；维护成本高 |
| 与我们方案重叠度 | **低** — 静态 LM 评测，非 agent 工作流 |
| 可借鉴点 | 多维度正交设计原则（避免指标间高度相关）；calibration 指标可迁移到 judge 一致性评估 |

### 9. ResearchRubrics

| 字段 | 内容 |
|------|------|
| 出处 | ICLR 2026（具体作者待确认 [待核验]） |
| 评什么 | 研究质量（专家手写 rubric，2593 条 criteria） |
| Judge | 专家 rubric + LLM 对照评分 |
| 缺陷 | 构建成本极高（2593 条 criterion 需领域专家手写）；rubric 固化后难以适配新研究方向 |
| 与我们方案重叠度 | **中** — 同为研究质量评测，但我们的 decomp 状态机自动生成 rubric 骨架，降低人工成本 |
| 可借鉴点 | rubric 条目结构（criterion + weight + scoring guide）；专家标注流程 |

### 10. HaluEval

| 字段 | 内容 |
|------|------|
| 出处 | Li et al., EMNLP 2023, arXiv:2305.11747 ✅已验证 |
| 标题 | HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models |
| 评什么 | 幻觉识别（给定文本，判断哪些 span 是幻觉） |
| Judge | 人工标注 span（ground truth） |
| 缺陷 | 识别幻觉 ≠ 防幻觉（被动检测，非主动预防）；标注成本高；不覆盖研究场景 |
| 与我们方案重叠度 | **低** — 幻觉检测，非研究质量评估 |
| 可借鉴点 | span-level 标注方法可迁移到"研究报告中哪些论断缺乏文献支持"的检测 |

---

## Q2：Prompt 因果消融先例

**检索结论：未发现「固定开源小模型 + 不同 prompt 臂 + 测下游研究产出质量」的公开工作。**（弱推断：本次检索未发现，不代表不存在）

最接近的工作：

### ODR+ (Open Deep Research Agent)

| 字段 | 内容 |
|------|------|
| 出处 | arXiv:2508.10152 ✅已验证 |
| 标题 | Improving and Evaluating Open Deep Research Agents |
| 核心方法 | 改三处策略（非纯 prompt 消融）：搜索策略、综合策略、报告生成策略 |
| 与我们方案重叠度 | **低** — 改的是策略组件，不是 prompt 变量；且使用闭源模型 |
| 可借鉴点 | 策略组件的模块化设计（便于后续做单变量消融） |

### DR Tulu

| 字段 | 内容 |
|------|------|
| 出处 | HF paper 2511.19399（HuggingFace 技术报告） |
| 核心方法 | RL 训练 deep research agent，prompt 只是其中一层（RL reward 设计更重要） |
| 与我们方案重叠度 | **低** — RL 训练路线，非 prompt 消融 |
| 可借鉴点 | reward 函数设计（如何量化"研究质量好"） |

### PromptBreeder

| 字段 | 内容 |
|------|------|
| 出处 | arXiv:2309.16797 ✅已验证 |
| 标题 | Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution |
| 核心方法 | 进化式 prompt 优化（变异 + 选择），目标是单轮任务分数 |
| 与我们方案重叠度 | **低** — 优化目标是单轮任务性能，非下游研究产出质量；无控制变量（同时改多个 prompt） |
| 可借鉴点 | 进化算法的变异算子设计；prompt 空间的表示方法 |

**→ 空白区确认**：「固定开源小模型 + 单变量 prompt 消融 + 下游研究产出质量指标」这个组合在公开文献中未见。这是我们的独特切入点。

---

## Q3：差异化设计点的理论支撑

### 异族 Judge（Cross-family LLM Judge）

| 字段 | 内容 |
|------|------|
| 理论支撑 | Zheng et al., arXiv:2306.05685 ✅已验证（"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"）记录了 self-enhancement bias（LLM 倾向给同家族模型更高分） |
| 现状 | 有理论支撑，但**无公开 bench 以此为方法论核心**（大多数 bench 用单一 LLM judge 或混合 judge，但未系统性用异族 judge 消除 bias） |
| 与我们方案重叠度 | **高** — 这是我们方案的核心设计之一 |
| 可借鉴点 | MT-Bench 的 pairwise comparison 协议（比 pointwise scoring 更稳健） |

### Decomp 状态机作为独立 Prompt 消融变量

| 字段 | 内容 |
|------|------|
| 现状 | **独特设计**，公开文献中未见将 decomp 状态机作为 prompt 消融变量的工作 |
| 与我们方案重叠度 | **高** — 这是我们方案的核心创新 |
| 可借鉴点 | 无直接先例，需自行设计消融实验 |

### κ ≥ 0.6 一致性门槛

| 字段 | 内容 |
|------|------|
| 现状 | LLM-judge 文献中**少见显式要求** judge 一致性达到 Cohen's κ ≥ 0.6（大多数工作只报告 accuracy 或 correlation，不设最低门槛） |
| 与我们方案重叠度 | **高** — 这是我们方案的质量保障机制 |
| 可借鉴点 | 可参考 inter-rater reliability 文献（psychometrics 领域）的 κ 计算方法 |

---

## 抽查验证记录

| arXiv ID | 预期标题 | 实际标题 | 状态 |
|----------|----------|----------|------|
| 2311.12983 | GAIA: a benchmark for General AI Assistants | GAIA: a benchmark for General AI Assistants | ✅ 一致 |
| 2501.14249 | Humanity's Last Exam | Humanity's Last Exam | ✅ 一致 |
| 2506.11763 | DeepResearch Bench | DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents | ✅ 一致 |
| 2305.14474 | FActScore (Min et al.) | Nonlocal anisotropic interactions of Coulomb type | ❌ **不一致，已修正为 2305.14251** |
| 2306.05685 | Judging LLM-as-a-Judge | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | ✅ 一致 |
| 2508.10152 | ODR+ | Improving and Evaluating Open Deep Research Agents | ✅ 一致 |
| 2309.16797 | PromptBreeder | Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution | ✅ 一致 |
| 2305.11747 | HaluEval | HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models | ✅ 一致 |
| 2211.09110 | HELM | Holistic Evaluation of Language Models | ✅ 一致 |

**修正记录**：FActScore 的 arXiv id 从 `2305.14474` 修正为 `2305.14251`（通过 arXiv API 标题搜索确认）。

---

## Confidence 自评

### 强证据（arXiv API 直接验证，标题完全一致）
- GAIA (2311.12983)、HLE (2501.14249)、DeepResearch Bench (2506.11763)、HELM (2211.09110)、HaluEval (2305.11747)、MT-Bench/Chatbot Arena (2306.05685)、ODR+ (2508.10152)、PromptBreeder (2309.16797)
- FActScore 正确 id 为 2305.14251（已通过 API 标题搜索确认）

### 中等证据（来自上轮 web_search 底稿，未在本轮独立验证）
- BrowseComp（Meta 2025，无 arXiv id，仅技术报告）
- SimpleQA（OpenAI 2024，无 arXiv id，仅技术报告）
- RAGAS（GitHub 开源框架，无正式论文）
- ResearchRubrics（ICLR 2026，具体作者和细节 [待核验]）
- DR Tulu（HF paper 2511.19399，未在本轮验证）

### 弱推断（检索未发现，不等于不存在）
- Q2 结论「固定开源小模型 + 不同 prompt 臂 + 测下游研究产出质量的公开工作不存在」— 基于本次检索关键词组合，未穷尽所有可能的表述方式
- 「异族 judge 无公开 bench 以此为方法论核心」— 基于本次检索，可能有未收录的工作