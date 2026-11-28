# N311: R_max=0.95 的实证基础：在 27B 模型的 RAG 基准测试中，当注入 1 条高相关性记忆（Relevance Score > 0.9）时，下游任务准

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

R_max=0.95 的实证基础：在 27B 模型的 RAG 基准测试中，当注入 1 条高相关性记忆（Relevance Score > 0.9）时，下游任务准确率相对于无记忆基线的提升上限约为 5-10 个百分点，归一化后召回率 R 定义为 (Acc_with - Acc_without) / Max_Possible_Uplift，最大值观测为 0.95；若 K=1 时 R 低于 0.9，说明记忆质量或相关性不足，需调整 K_ref。

## Corrected Claim

在27B模型的RAG基准测试中，注入高相关性记忆通常能带来显著准确率提升，归一化召回率R的上限接近1（具体数值如0.95取决于特定实验设定）；若K=1时R显著偏低，提示需调整记忆检索策略。

## Evidence

[质询]该陈述包含具体的经验性数值（27B模型、5-10个百分点提升、R_max=0.95），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定实验设置和数据的经验观察。缺乏公开权威文献直接支持这一特定组合下的精确数值上限。 | 逻辑自洽（归一化定义合理，量级符合RAG常见增益范围），但作为经验事实，缺乏外部来源直接支持具体数值，故降级。

## Search Query

rag memory injection accuracy uplift baseline single fact retrieval
