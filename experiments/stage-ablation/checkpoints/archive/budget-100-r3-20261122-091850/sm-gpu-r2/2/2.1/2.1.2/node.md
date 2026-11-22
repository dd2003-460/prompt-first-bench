# N46: Qwen3-27B 在 BF16 精度下的基准 MMLU 准确率，作为后续量化方案准确率下降的绝对基准，典型值预期在 75%-85% 之间 [待核验]。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

Qwen3-27B 在 BF16 精度下的基准 MMLU 准确率，作为后续量化方案准确率下降的绝对基准，典型值预期在 75%-85% 之间 [待核验]。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的基准 MMLU 准确率通常处于较高水平（约 75%-85% 区间），具体数值需以官方技术报告或标准评测结果为准，作为量化方案准确率下降的相对基准。

## Evidence

[质询]具体数值范围（75%-85%）属于经验事实，不同评测集版本（如 MMLU 5-shot vs 0-shot）及具体模型微调版本可能导致准确率波动，且缺乏直接来源支持该特定区间的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B BF16 MMLU accuracy benchmark
