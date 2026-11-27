# N240: Qwen3-27B 在 NVFP4/W4 量化下的困惑度 (PPL_W4) 实测值，用于评估极低精度下是否突破 5% PPL 增加上限，若突破则需引入质量损失修

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N62

## Claim

Qwen3-27B 在 NVFP4/W4 量化下的困惑度 (PPL_W4) 实测值，用于评估极低精度下是否突破 5% PPL 增加上限，若突破则需引入质量损失修正因子 [待核验：需检索具体量化评测数据]

## Corrected Claim

Qwen3-27B 在 NVFP4/W4 量化下的困惑度 (PPL_W4) 实测值需进一步检索确认，以评估是否突破 5% PPL 增加上限；若突破则需引入质量损失修正因子。

## Evidence

[质询]该陈述包含具体的经验性数值指标（PPL_W4实测值）及特定模型（Qwen3-27B）在特定量化方案（NVFP4/W4）下的性能表现，属于硬件/模型规格类经验事实，无法从第一性原理推导，且当前无可用来源支持其具体数值或结论。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体PPL数值或是否突破5%上限）

## Search Query

Qwen3-27B 4-bit quantization perplexity loss benchmark
