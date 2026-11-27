# N409: Qwen3-27B 在 AWQ INT4 量化下，MMLU 性能下降的主要原因分析（如量化误差在注意力头或 FFN 层的分布），若缺乏具体归因数据，则提供同架构

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

Qwen3-27B 在 AWQ INT4 量化下，MMLU 性能下降的主要原因分析（如量化误差在注意力头或 FFN 层的分布），若缺乏具体归因数据，则提供同架构模型（如 Llama-3-8B/70B INT4）的平均 MMLU 下降幅度（通常 1-3%）作为先验估计。

## Corrected Claim

Qwen3-27B 在 AWQ INT4 量化下，MMLU 性能下降的主要原因分析（如量化误差在注意力头或 FFN 层的分布），若缺乏具体归因数据，则提供同架构模型（如 Llama-3-8B/70B INT4）的平均 MMLU 下降幅度（通常 1-3%）作为先验估计。

## Evidence

先验知识/题面给定，逻辑校验通过
