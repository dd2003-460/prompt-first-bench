# N157: FP8 与 W4 量化在 27B 模型上的 Perplexity 与 MMLU 损失差异需通过控制变量法对比：相同数据集、相同采样温度、相同 prompt 长度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

FP8 与 W4 量化在 27B 模型上的 Perplexity 与 MMLU 损失差异需通过控制变量法对比：相同数据集、相同采样温度、相同 prompt 长度下计算 ΔPPL 和 ΔMMLU 的绝对差值，以量化'无损'与'有损'的边界，该差异值直接决定精度选择的性价比拐点 [待核验]

## Corrected Claim

FP8 与 W4 量化在 27B 模型上的 Perplexity 与 MMLU 损失差异需通过控制变量法对比：相同数据集、相同采样温度、相同 prompt 长度下计算 ΔPPL 和 ΔMMLU 的绝对差值，以量化'无损'与'有损'的边界，该差异值直接决定精度选择的性价比拐点 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：控制变量法是评估量化精度损失的标准科学方法，ΔPPL和ΔMMLU是衡量模型性能退化的合理指标，逻辑自洽且符合机器学习评估常识。
