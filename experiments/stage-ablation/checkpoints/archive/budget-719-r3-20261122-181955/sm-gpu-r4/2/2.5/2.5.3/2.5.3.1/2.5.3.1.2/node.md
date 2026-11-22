# N760: INT4 (AWQ) 量化相对于 BF16 的 MMLU 准确率下降百分比 (ΔMMLU_INT4) 计算公式为：((78.2 - 76.4) / 78.2) 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N271

## Claim

INT4 (AWQ) 量化相对于 BF16 的 MMLU 准确率下降百分比 (ΔMMLU_INT4) 计算公式为：((78.2 - 76.4) / 78.2) * 100% ≈ 2.30%。该值显著高于 FP8 的损失（~0.9%），表明 INT4 在知识密集型任务上存在更明显的质量退化，需权衡显存节省与精度损失。

## Corrected Claim

INT4 (AWQ) 量化相对于 BF16 的 MMLU 准确率下降百分比 (ΔMMLU_INT4) 计算公式为：((78.2 - 76.4) / 78.2) * 100% ≈ 2.30%。该值显著高于 FP8 的损失（~0.9%），表明 INT4 在知识密集型任务上存在更明显的质量退化，需权衡显存节省与精度损失。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (78.2-76.4)/78.2 ≈ 2.30% 正确，且 INT4 量化损失通常高于 FP8 符合工程常识。
