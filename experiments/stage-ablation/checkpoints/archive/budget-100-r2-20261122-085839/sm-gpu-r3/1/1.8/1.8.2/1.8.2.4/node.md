# N185: Qwen3-27B 在 AWQ (W4A16) 量化下的 MMLU 分数通常比 GPTQ 高 0.5-1.0 个百分点（例如 81.5-81.8%），这是因为 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53, N54, N55

## Claim

Qwen3-27B 在 AWQ (W4A16) 量化下的 MMLU 分数通常比 GPTQ 高 0.5-1.0 个百分点（例如 81.5-81.8%），这是因为 AWQ 保护显著权重通道，减少了关键特征的量化噪声，该差异在决策中可作为精度选择的关键依据。

## Corrected Claim

Qwen3-27B 在 AWQ (W4A16) 量化下的 MMLU 分数通常比 GPTQ 略高，这是因为 AWQ 保护显著权重通道，减少了关键特征的量化噪声，该差异在决策中可作为精度选择的参考依据。

## Evidence

[质询]具体数值（81.5-81.8%）及差异幅度（0.5-1.0个百分点）属于特定实验条件下的经验数据，不同数据集版本、评测协议或量化实现细节可能导致结果波动，且缺乏来源支持该特定数值区间。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ W4A16 MMLU score comparison GPTQ
