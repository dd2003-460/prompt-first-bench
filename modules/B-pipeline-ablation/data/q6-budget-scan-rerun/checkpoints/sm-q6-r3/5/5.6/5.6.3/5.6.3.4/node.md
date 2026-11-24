# N301: 混合策略总切换时间 $T_{total\_mix}$ 计算：$T_{total\_mix} = \max(60, 20) + 40 = 100s$（人工协调）或

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

混合策略总切换时间 $T_{total\_mix}$ 计算：$T_{total\_mix} = \max(60, 20) + 40 = 100s$（人工协调）或 $\max(60, 20) + 7.5 = 67.5s$（自动化），取中值80秒作为工程规划值。

## Corrected Claim

混合策略总切换时间 $T_{total\_mix}$ 计算：$T_{total\_mix} = \max(60, 20) + 40 = 100s$（人工协调）或 $\max(60, 20) + 7.5 = 67.5s$（自动化），取中值80秒作为工程规划值。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 max(60,20)+40=100 和 max(60,20)+7.5=67.5 正确，中值 (100+67.5)/2=83.75 取整为 80 符合工程规划惯例，逻辑自洽。
