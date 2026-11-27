# N228: Qwen3-27B 在 32K 上下文长度下的基准困惑度 (PPL_base_32K) 为 [待核验]，需引用同一数据源中 32K 上下文下的 BF16 PPL

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N73

## Claim

Qwen3-27B 在 32K 上下文长度下的基准困惑度 (PPL_base_32K) 为 [待核验]，需引用同一数据源中 32K 上下文下的 BF16 PPL 数值，用于量化长上下文本身带来的固有性能衰减，以剥离量化误差。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下的基准困惑度 (PPL_base_32K) 需引用同一数据源中 32K 上下文下的 BF16 PPL 数值，用于量化长上下文本身带来的固有性能衰减，以剥离量化误差。

## Evidence

[质询]该陈述包含具体的经验事实（Qwen3-27B在32K上下文下的BF16 PPL数值），属于硬件/模型性能指标，无法从第一性原理推导，且当前无可用来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

Qwen3-27B benchmark perplexity 32k context BF16
