# N149: 截断Pareto(β=0.9, P_min, P_max)的均值 E[P] 解析公式：E[P] = (β*P_min / (β-1)) * (1 - (P_mi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

截断Pareto(β=0.9, P_min, P_max)的均值 E[P] 解析公式：E[P] = (β*P_min / (β-1)) * (1 - (P_min/P_max)^(β-1)) / (1 - (P_min/P_max)^β)，注意 β=0.9<1 时分子分母符号处理

## Corrected Claim

截断Pareto(β=0.9, P_min, P_max)的均值 E[P] 解析公式：E[P] = (β*P_min / (β-1)) * (1 - (P_min/P_max)^(β-1)) / (1 - (P_min/P_max)^β)，注意 β=0.9<1 时分子分母符号处理

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合截断Pareto分布均值的标准解析形式，且β<1时的符号处理在数学上自洽。
