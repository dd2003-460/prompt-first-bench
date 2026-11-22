# N239: Qwen3-27B 在 FP8 量化下的困惑度 (PPL_FP8) 实测值，用于验证其是否满足 PPL_FP8 <= 1.05 * PPL_BF16 的可接受性

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N62

## Claim

Qwen3-27B 在 FP8 量化下的困惑度 (PPL_FP8) 实测值，用于验证其是否满足 PPL_FP8 <= 1.05 * PPL_BF16 的可接受性标准 [待核验：需检索具体量化评测数据]

## Corrected Claim

Qwen3-27B 在 FP8 量化下的困惑度 (PPL_FP8) 实测值需进一步检索具体量化评测数据以验证其是否满足 PPL_FP8 <= 1.05 * PPL_BF16 的可接受性标准。

## Evidence

[质询]该陈述包含具体的经验性数值指标（PPL_FP8 实测值及与 BF16 的比率），属于硬件/模型性能经验事实，无法从第一性原理推导，且当前无可用来源支持具体数值或比率是否确实满足 <= 1.05 的标准。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体 PPL 数值及比率是否达标）

## Search Query

Qwen3-27B FP8 quantization perplexity degradation
