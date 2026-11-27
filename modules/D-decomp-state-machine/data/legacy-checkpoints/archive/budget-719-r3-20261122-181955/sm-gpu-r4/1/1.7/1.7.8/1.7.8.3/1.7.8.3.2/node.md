# N685: INT4 (AWQ) 量化对 Qwen3-27B 的精度损失评估：相比 BF16，INT4 AWQ 在 MMLU 上的性能下降通常在 1-3% 范围内，具体数值

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N244

## Claim

INT4 (AWQ) 量化对 Qwen3-27B 的精度损失评估：相比 BF16，INT4 AWQ 在 MMLU 上的性能下降通常在 1-3% 范围内，具体数值需参考 AWQ 论文或 Qwen3 官方量化模型的评测数据；若损失 > 2%，需评估是否可通过校准数据集优化降低至可接受范围。

## Corrected Claim

INT4 (AWQ) 量化对 Qwen3-27B 的精度损失评估：相比 BF16，INT4 AWQ 在 MMLU 上通常会有轻微性能下降，具体数值需参考 AWQ 论文或 Qwen3 官方量化模型的评测数据；若损失显著，需评估是否可通过校准数据集优化降低至可接受范围。

## Evidence

[质询]该陈述包含具体的经验性数值范围（MMLU下降1-3%）和特定模型（Qwen3-27B）的量化表现，属于经验事实。由于缺乏检索来源支持，无法验证该具体数值范围是否准确，且不同校准数据集可能导致结果波动，1-3%并非绝对固定的物理/数学常数。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源），无法排除具体数值偏差的可能性，故降级。

## Search Query

AWQ INT4 quantization Qwen3-27B accuracy drop MMLU benchmark
