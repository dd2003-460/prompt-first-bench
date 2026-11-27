# N178: 专业推理任务（代码生成/数学）的精度可接受性阈值：定义为 HumanEval Pass@1 或 GSM8K 准确率下降 < 2%。在此严格阈值下，INT4 量化

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38, N39, N40

## Claim

专业推理任务（代码生成/数学）的精度可接受性阈值：定义为 HumanEval Pass@1 或 GSM8K 准确率下降 < 2%。在此严格阈值下，INT4 量化通常因逻辑推理能力受损而被判定为“不可接受”，必须使用 INT8 或 FP8 精度，从而强制要求更大的显存或更贵的硬件。

## Corrected Claim

专业推理任务（代码生成/数学）的精度可接受性阈值：定义为 HumanEval Pass@1 或 GSM8K 准确率下降 < 2%。在此严格阈值下，INT4 量化通常因逻辑推理能力受损而被判定为“不可接受”，必须使用 INT8 或 FP8 精度，从而强制要求更大的显存或更贵的硬件。

## Evidence

先验知识/题面给定，逻辑校验通过
