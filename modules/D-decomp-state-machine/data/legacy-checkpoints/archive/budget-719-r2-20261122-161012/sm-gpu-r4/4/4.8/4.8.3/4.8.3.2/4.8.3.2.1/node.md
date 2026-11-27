# N636: Qwen3-27B 在 BF16 精度下的 HumanEval Pass@1 基线值 (HE_BF16) 需从 Qwen3 官方代码生成基准获取，作为计算 IN

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N263

## Claim

Qwen3-27B 在 BF16 精度下的 HumanEval Pass@1 基线值 (HE_BF16) 需从 Qwen3 官方代码生成基准获取，作为计算 INT4 量化后代码生成能力下降幅度的绝对参照，若官方未公布，参考同级别模型 (如 CodeLlama-34B) 的 Pass@1 (约 70-75%) 进行校准。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 HumanEval Pass@1 基线值需从官方基准获取；若未公布，可参考同级别代码模型（如 CodeLlama 系列）的公开基准数据进行定性校准，具体数值需查阅最新技术报告。

## Evidence

[质询]该陈述包含具体的经验性数值范围（CodeLlama-34B Pass@1 约 70-75%）和特定模型（Qwen3-27B）的基准假设，属于经验事实，无法从第一性原理推导，且缺乏来源支持以确认具体数值或模型是否存在。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证 Qwen3-27B 具体基准及 CodeLlama-34B 的精确 Pass@1 数值范围）。

## Search Query

Qwen3-27B HumanEval Pass@1 BF16 baseline
