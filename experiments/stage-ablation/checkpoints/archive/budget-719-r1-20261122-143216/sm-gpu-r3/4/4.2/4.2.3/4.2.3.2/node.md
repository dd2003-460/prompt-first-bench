# N283: Qwen3-27B 在 INT8 精度下的 GSM8K 实测分数，需查找社区 INT8 量化模型（如 GPTQ/AWQ 版本）的评测记录，该数值用于直接计算相对

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N100

## Claim

Qwen3-27B 在 INT8 精度下的 GSM8K 实测分数，需查找社区 INT8 量化模型（如 GPTQ/AWQ 版本）的评测记录，该数值用于直接计算相对于 BF16 基线的绝对下降值，并评估是否超过 2-5 分的预期容忍区间。

## Corrected Claim

Qwen3-27B 在 INT8 精度下的 GSM8K 分数需参考特定社区量化模型（如 GPTQ/AWQ 版本）的评测记录，不同量化配置下分数存在波动，建议引用多个独立评测结果或明确指定量化配置以评估相对于 BF16 基线的下降幅度。

## Evidence

[质询]该陈述声称存在具体的“实测分数”用于计算绝对下降值，但INT8量化模型（GPTQ/AWQ）的性能高度依赖于具体的量化配置（如group size, zero-point等）和评测脚本版本，社区中不存在唯一的、公认的“Qwen3-27B INT8 GSM8K实测分数”标准值，不同来源的数据可能存在显著差异，直接引用单一数值作为基准存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为具体经验参数，非第一性原理可推导）

## Search Query

Qwen3-27B INT8 GPTQ AWQ quantization GSM8K score evaluation
