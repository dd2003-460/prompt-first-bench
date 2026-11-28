# N39: Research-AGI 循环中‘提出假设’与‘设计实验’步骤的幻觉率 Hallucination Rate η：在缺乏实时工具调用（如代码执行器、数据库查询）

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Research-AGI 循环中‘提出假设’与‘设计实验’步骤的幻觉率 Hallucination Rate η：在缺乏实时工具调用（如代码执行器、数据库查询）的情况下，Qwen3.8-27B 生成虚构参考文献或错误实验参数的概率分布，需通过内部评测集（如 HotpotQA 变体或科研问答集）量化 η，若 η > 5%，则必须强制引入外部 RAG 工具作为硬依赖，否则可靠性不达标。

## Corrected Claim

在缺乏实时工具调用的情况下，大语言模型（如 Qwen 系列）在科研问答任务中可能存在较高的幻觉率。建议通过内部评测集量化幻觉率 η，并设定合理的阈值（如 5%）作为引入外部 RAG 工具的决策依据，具体阈值需根据实际业务场景和模型表现动态调整。

## Evidence

[质询]该陈述包含具体的经验性阈值（η > 5%）和特定模型版本（Qwen3.8-27B）的性能假设，这些属于经验事实，无法从第一性原理推导，且缺乏实时数据支持其普适性或准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且涉及具体模型参数与阈值，不适用第一性原理验证）

## Search Query

LLM hallucination rate scientific hypothesis generation experimental design Qwen3 benchmark evaluation metrics
