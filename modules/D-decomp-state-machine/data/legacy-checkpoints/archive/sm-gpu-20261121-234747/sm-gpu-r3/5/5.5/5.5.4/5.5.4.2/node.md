# N408: FP8 量化下 Qwen3-27B 在相同 1000 条 Prompt 集下的平均困惑度 PPL_FP8，用于计算 ΔPPL = PPL_FP8 - PPL_B

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N134, N135, N136

## Claim

FP8 量化下 Qwen3-27B 在相同 1000 条 Prompt 集下的平均困惑度 PPL_FP8，用于计算 ΔPPL = PPL_FP8 - PPL_BF16，该值直接反映整体分布偏移程度

## Corrected Claim

FP8 量化下 Qwen3-27B 在相同 1000 条 Prompt 集下的平均困惑度 PPL_FP8 用于计算 ΔPPL，该指标反映整体分布偏移程度，但具体数值需参考实际基准测试报告。

## Evidence

[质询]该陈述包含具体的经验性数值结果（Qwen3-27B在FP8量化下的具体PPL值或ΔPPL值），属于硬件/模型性能经验事实，无法从第一性原理推导，且当前无可用来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 quantized perplexity delta vs BF16
