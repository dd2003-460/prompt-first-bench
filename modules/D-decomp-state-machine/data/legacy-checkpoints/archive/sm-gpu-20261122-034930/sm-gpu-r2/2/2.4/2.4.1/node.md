# N79: BF16精度下Qwen3-27B在MMLU基准测试上的准确率与FP32相比差异为<0.1%，因为BF16是Qwen3系列模型的主要训练精度之一，FP32仅为高精

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

BF16精度下Qwen3-27B在MMLU基准测试上的准确率与FP32相比差异为<0.1%，因为BF16是Qwen3系列模型的主要训练精度之一，FP32仅为高精度参考基准，实际推理中BF16即为原生精度

## Corrected Claim

BF16精度下Qwen3-27B在MMLU基准测试上的准确率与FP32相比差异极小（通常可忽略不计），因为BF16是Qwen3系列模型的主要训练精度之一，FP32仅为高精度参考基准，实际推理中BF16即为原生精度。

## Evidence

[质询]具体数值差异（<0.1%）属于经验事实，缺乏直接来源支持，且不同模型/数据集上BF16与FP32的精度损失可能波动，断言绝对小于0.1%过于绝对。 | 经验事实，逻辑自洽但缺来源支持；BF16作为训练/推理原生精度在逻辑上合理，但具体误差数值需实证数据支撑。
