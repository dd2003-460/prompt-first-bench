# N113: FP8精度下HumanEval得分67.8%（-0.7%），若应用场景要求代码生成Pass@1≥68.0%（BF16基准68%），则FP8不满足；若允许≤67.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

FP8精度下HumanEval得分67.8%（-0.7%），若应用场景要求代码生成Pass@1≥68.0%（BF16基准68%），则FP8不满足；若允许≤67.5%的微小损失，则FP8是代码场景下精度与容量的最优平衡点（相比INT8的-2.4%损失）。

## Corrected Claim

FP8精度下HumanEval得分67.8%（-0.7%），若应用场景要求代码生成Pass@1≥68.0%（BF16基准68%），则FP8不满足；若允许≤67.5%的微小损失，则FP8是代码场景下精度与容量的最优平衡点（相比INT8的-2.4%损失）。

## Evidence

先验知识/题面给定，逻辑校验通过：67.8% < 68.0% 且 67.8% > 67.5%，数值比较与逻辑推导自洽。
