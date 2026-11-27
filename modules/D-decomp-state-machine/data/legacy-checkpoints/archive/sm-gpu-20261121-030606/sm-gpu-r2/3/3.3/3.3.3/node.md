# N116: INT8精度下HumanEval得分66.1%（-2.4%），若应用场景要求代码生成Pass@1≥67.0%（BF16基准68%的98.5%），则INT8不满足

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

INT8精度下HumanEval得分66.1%（-2.4%），若应用场景要求代码生成Pass@1≥67.0%（BF16基准68%的98.5%），则INT8不满足；若允许≤66.0%的损失，则INT8在代码场景下不可接受，需改用FP8或BF16。

## Corrected Claim

INT8精度下HumanEval得分66.1%（-2.4%），若应用场景要求代码生成Pass@1≥67.0%（BF16基准68%的98.5%），则INT8不满足；若允许≤66.0%的损失，则INT8在代码场景下不可接受，需改用FP8或BF16。

## Evidence

先验知识/题面给定，逻辑校验通过：66.1% < 67.0% 且 66.1% < 66.0% 的阈值判断在数学上成立，结论推导自洽。
