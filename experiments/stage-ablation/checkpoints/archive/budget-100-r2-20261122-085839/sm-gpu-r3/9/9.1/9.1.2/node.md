# N288: Qwen3-27B 在 INT8 (GPTQ/AWQ) 量化下的 MMLU 分数具体数值，以及相对于 BF16 基线的绝对下降值（百分点），用于验证 1-2% 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

Qwen3-27B 在 INT8 (GPTQ/AWQ) 量化下的 MMLU 分数具体数值，以及相对于 BF16 基线的绝对下降值（百分点），用于验证 1-2% 损失区间是否适用于该特定模型架构。

## Corrected Claim

Qwen3-27B 在 INT8 (GPTQ/AWQ) 量化下的 MMLU 分数通常会有轻微下降，具体数值需查阅官方技术报告或基准测试数据，一般预期损失在 1-2% 区间内，但具体绝对下降值因量化配置而异。

## Evidence

[质询]具体数值（MMLU分数及绝对下降值）属于经验事实，且不同量化方法（GPTQ vs AWQ）及校准数据集可能导致结果差异，缺乏具体来源支持无法确定精确数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT8 GPTQ AWQ MMLU accuracy degradation
