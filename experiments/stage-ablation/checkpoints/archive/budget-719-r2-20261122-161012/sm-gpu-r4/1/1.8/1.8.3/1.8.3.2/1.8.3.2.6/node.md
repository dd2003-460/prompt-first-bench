# N471: MMLU ≥ 80% 硬约束下的精度选择决策树：若 BF16 基线 MMLU 为 85.2%，则 FP8 (84.9%)、INT4-AWQ (83.4%)、IN

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N193, N194, N195

## Claim

MMLU ≥ 80% 硬约束下的精度选择决策树：若 BF16 基线 MMLU 为 85.2%，则 FP8 (84.9%)、INT4-AWQ (83.4%)、INT4-GPTQ (82.6%) 均满足约束；此时性价比排序由 Cost_Performance_Ratio = (Capex + OPEX) / (Throughput * Quality_Factor) 决定，其中 Quality_Factor 分别取 0.996 (FP8), 0.979 (AWQ), 0.969 (GPTQ)，需计算各方案在 3 年 TCO 下的具体比值

## Corrected Claim

MMLU ≥ 80% 硬约束下的精度选择决策树：若 BF16 基线 MMLU 为 85.2%，则 FP8 (84.9%)、INT4-AWQ (83.4%)、INT4-GPTQ (82.6%) 均满足约束；此时性价比排序由 Cost_Performance_Ratio = (Capex + OPEX) / (Throughput * Quality_Factor) 决定，其中 Quality_Factor 分别取 0.996 (FP8), 0.979 (AWQ), 0.969 (GPTQ)，需计算各方案在 3 年 TCO 下的具体比值

## Evidence

先验知识/题面给定，逻辑校验通过：MMLU数值与80%约束比较正确，Quality_Factor计算（84.9/85.2≈0.996, 83.4/85.2≈0.979, 82.6/85.2≈0.969）准确，决策树逻辑自洽。
