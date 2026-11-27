# N119: W4精度下HumanEval得分62.3%（-6.2%），若应用场景要求代码生成Pass@1≥65.0%（BF16基准68%的95.6%），则W4不满足；若允许

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

W4精度下HumanEval得分62.3%（-6.2%），若应用场景要求代码生成Pass@1≥65.0%（BF16基准68%的95.6%），则W4不满足；若允许≤62.0%的损失，则W4在代码场景下不可接受，需改用FP8/INT8或BF16。

## Corrected Claim

W4精度下HumanEval得分62.3%（-6.2%），若应用场景要求代码生成Pass@1≥65.0%（BF16基准68%的95.6%），则W4不满足；若允许≤62.0%的损失，则W4在代码场景下不可接受，需改用FP8/INT8或BF16。

## Evidence

先验知识/题面给定，逻辑校验通过：62.3% < 65.0% 且 62.3% < 62.0% 的阈值判断在数学上成立，结论推导自洽。
