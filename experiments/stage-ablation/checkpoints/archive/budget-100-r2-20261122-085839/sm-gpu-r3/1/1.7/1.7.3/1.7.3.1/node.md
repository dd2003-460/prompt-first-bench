# N167: GPTQ 量化在 Qwen3-27B 上的 MMLU 得分绝对值（需基于 128-shot 或 5-shot 基准，校准集大小通常为 128-512 样本）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N50

## Claim

GPTQ 量化在 Qwen3-27B 上的 MMLU 得分绝对值（需基于 128-shot 或 5-shot 基准，校准集大小通常为 128-512 样本）

## Corrected Claim

GPTQ 量化在 Qwen3-27B 上的 MMLU 得分具体数值需查阅特定量化配置下的官方或第三方评测报告，通常量化会引入轻微的性能下降，但具体绝对值因配置而异。

## Evidence

[质询]该陈述要求提供具体的MMLU得分绝对值，但GPTQ量化后的模型性能高度依赖于具体的量化配置（如group size, damp, sym等）以及校准集的具体样本，不同实现和配置下的得分会有显著差异，且Qwen3-27B的具体量化基准数据属于经验事实，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B GPTQ INT8 MMLU score benchmark
