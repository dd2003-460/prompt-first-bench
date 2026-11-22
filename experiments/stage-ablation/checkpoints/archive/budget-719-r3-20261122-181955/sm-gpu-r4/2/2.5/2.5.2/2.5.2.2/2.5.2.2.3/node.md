# N758: FP8 量化相对于 BF16 的 HumanEval 准确率下降百分比 (ΔHumanEval) 计算公式为：((65.1 - 64.3) / 65.1) * 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N269

## Claim

FP8 量化相对于 BF16 的 HumanEval 准确率下降百分比 (ΔHumanEval) 计算公式为：((65.1 - 64.3) / 65.1) * 100% ≈ 1.23%。若实测 FP8 为 64.8%，则 ΔHumanEval ≈ 0.46%。该损失幅度在代码生成任务中处于可接受边缘，需结合具体应用场景判断。

## Corrected Claim

FP8 量化相对于 BF16 的 HumanEval 准确率下降百分比 (ΔHumanEval) 计算公式为：((65.1 - 64.3) / 65.1) * 100% ≈ 1.23%。若实测 FP8 为 64.8%，则 ΔHumanEval ≈ 0.46%。该损失幅度在代码生成任务中处于可接受边缘，需结合具体应用场景判断。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (65.1-64.3)/65.1≈1.23% 和 (65.1-64.8)/65.1≈0.46% 均正确，量纲与逻辑自洽。
