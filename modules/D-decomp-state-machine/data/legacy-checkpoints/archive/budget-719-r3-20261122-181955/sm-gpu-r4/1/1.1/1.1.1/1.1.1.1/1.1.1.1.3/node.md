# N409: INT4 量化对 Qwen3-27B 质量损失的具体量化：在 MMLU 基准上，INT4 (GPTQ/AWQ) 相比 BF16 的平均准确率损失约为 0.5%-

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N134

## Claim

INT4 量化对 Qwen3-27B 质量损失的具体量化：在 MMLU 基准上，INT4 (GPTQ/AWQ) 相比 BF16 的平均准确率损失约为 0.5%-1.5% [待核验：需引用具体 Qwen3 技术报告或第三方评测]；若损失超过 2%，则需考虑 INT8 或 FP8 作为替代，但 INT8 会显著降低 Decode 吞吐（带宽减半），需重新计算 TCO 权衡。

## Corrected Claim

INT4 量化（如 GPTQ/AWQ）通常会导致大模型在 MMLU 等基准上出现轻微准确率下降（通常小于 2%），具体损失幅度取决于模型规模、量化算法及校准数据；若对精度敏感或损失超过可接受阈值，应考虑 INT8/FP8 等更高精度方案，但需权衡其对 Decode 吞吐及 TCO 的影响。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU准确率损失0.5%-1.5%）和特定模型（Qwen3-27B）的量化表现，属于经验事实。由于缺乏具体技术报告或第三方评测的直接引用，且不同量化算法（GPTQ vs AWQ）及校准数据集可能导致结果差异，该具体数值范围缺乏直接证据支持，存在口径混淆或数值偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值范围）

## Search Query

Qwen3-27B INT4 quantization quality loss MMLU benchmark
