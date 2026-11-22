# N252: Q4_K_M 与 INT8 的质量损失差异：Q4_K_M 在 MMLU 基准上通常比 INT8 低 1-3 个百分点（[待核验] 具体数值需查 Qwen3 量化

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

Q4_K_M 与 INT8 的质量损失差异：Q4_K_M 在 MMLU 基准上通常比 INT8 低 1-3 个百分点（[待核验] 具体数值需查 Qwen3 量化报告），若 Q4_K_M 导致 MMLU 下降 > 2 个百分点，则 Apple 方案的质量因子 (Quality_Factor) 需打折，进一步降低其综合性价比。

## Corrected Claim

Q4_K_M 在 MMLU 基准上通常比 INT8 存在一定程度的质量损失（具体幅度视模型和实现而定，常见范围约为 1-3 个百分点），若实测下降超过 2 个百分点，则 Apple 方案的质量因子需相应打折，进一步降低其综合性价比。

## Evidence

[质询]具体数值（1-3个百分点）缺乏针对 Qwen3 模型的直接实证支持，不同模型架构和量化实现下差异可能波动，属于经验事实而非第一性原理可推导结论。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体量化损失数值无法从第一性原理严格推出）

## Search Query

Qwen3-27B Q4_K_M vs INT8 MMLU benchmark
