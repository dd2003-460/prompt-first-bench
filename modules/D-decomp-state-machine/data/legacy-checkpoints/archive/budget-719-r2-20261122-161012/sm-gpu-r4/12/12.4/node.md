# N313: 量化质量损失的可接受性阈值公式定义：Acceptable_Quantization = (PPL_FP8 - PPL_BF16 < 0.1) AND (MMLU

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N135

## Claim

量化质量损失的可接受性阈值公式定义：Acceptable_Quantization = (PPL_FP8 - PPL_BF16 < 0.1) AND (MMLU_FP8 - MMLU_BF16 < 0.5%)；若 FP8 不满足此条件，则必须升级为 BF16 或寻找更高精度的 INT8 方案；该阈值直接决定 N137 中 Quality_Factor 的取值范围 (FP8 对应 0.98-0.99, INT4 对应 0.95-0.97)。

## Corrected Claim

量化质量损失的可接受性阈值公式定义：Acceptable_Quantization = (PPL_FP8 - PPL_BF16 < 0.1) AND (MMLU_FP8 - MMLU_BF16 < 0.5%)；若 FP8 不满足此条件，则必须升级为 BF16 或寻找更高精度的 INT8 方案；该阈值直接决定 N137 中 Quality_Factor 的取值范围 (FP8 对应 0.98-0.99, INT4 对应 0.95-0.97)。

## Evidence

先验知识/题面给定，逻辑校验通过
