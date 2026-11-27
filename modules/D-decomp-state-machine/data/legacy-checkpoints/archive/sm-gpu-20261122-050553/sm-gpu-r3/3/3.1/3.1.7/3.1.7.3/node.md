# N215: INT8 量化质量退化的边界条件：当上下文长度增加至 32K 且 Batch Size > 4 时，INT8 权重与 KV Cache 的交互误差可能放大，导致

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69

## Claim

INT8 量化质量退化的边界条件：当上下文长度增加至 32K 且 Batch Size > 4 时，INT8 权重与 KV Cache 的交互误差可能放大，导致 MMLU 下降幅度从 1% 线性增长至 2-3% [待核验]，此时需重新评估是否超过 5% 容忍阈值或改用 W4A16 混合策略。

## Corrected Claim

INT8 量化在长上下文（如 32K）及较大 Batch Size 下，权重与 KV Cache 的交互误差可能放大，导致 MMLU 性能下降幅度增加，需重新评估是否超过容忍阈值或改用混合量化策略。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU下降幅度从1%线性增长至2-3%）和特定的边界条件（32K上下文、Batch Size > 4），这些属于硬件/模型行为的具体经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

INT8 quantization long context batch size accuracy degradation LLM
