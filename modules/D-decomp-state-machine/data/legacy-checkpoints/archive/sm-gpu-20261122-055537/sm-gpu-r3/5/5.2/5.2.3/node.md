# N84: Qwen3-27B INT4 量化的质量损失量化：在 MMLU 基准上，INT4 (AWQ) 相比 BF16 的准确率下降通常在 1-3% 范围内；在 Huma

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Qwen3-27B INT4 量化的质量损失量化：在 MMLU 基准上，INT4 (AWQ) 相比 BF16 的准确率下降通常在 1-3% 范围内；在 HumanEval (代码生成) 上，下降幅度可能更大，约 2-5%，需通过具体量化模型 (如 Qwen3-27B-AWQ) 的公开评测或复现验证。

## Corrected Claim

Qwen3-27B INT4 量化（如 AWQ）相比 BF16 通常会导致一定程度的准确率下降，具体幅度需参考该模型的公开评测数据或自行复现验证，一般大模型在 MMLU 等基准上下降幅度较小，在代码生成等复杂任务上可能略高。

## Evidence

[质询]该陈述包含具体的经验性数值范围（MMLU下降1-3%，HumanEval下降2-5%），属于硬件/模型性能指标，无法从第一性原理推导。且未提供具体来源支持这些特定数值，存在将一般量化经验直接套用于特定模型（Qwen3-27B）的风险，不同量化算法（AWQ vs GPTQ）和模型架构可能导致显著差异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值范围）

## Search Query

Qwen3-27B INT4 AWQ MMLU HumanEval accuracy drop vs BF16
