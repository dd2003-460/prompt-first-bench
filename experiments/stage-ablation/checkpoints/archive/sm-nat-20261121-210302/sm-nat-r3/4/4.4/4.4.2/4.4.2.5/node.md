# N150: 截断Pareto(β=0.9, P_min, P_max)的二阶矩 E[P^2] 解析公式：E[P^2] = (β*P_min^2 / (β-2)) * (1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

截断Pareto(β=0.9, P_min, P_max)的二阶矩 E[P^2] 解析公式：E[P^2] = (β*P_min^2 / (β-2)) * (1 - (P_min/P_max)^(β-2)) / (1 - (P_min/P_max)^β)，注意 β=0.9<2 时 α-2 为负数，需验证积分收敛性

## Corrected Claim

截断Pareto(β=0.9, P_min, P_max)的二阶矩 E[P^2] 解析公式：E[P^2] = (β*P_min^2 / (β-2)) * (1 - (P_min/P_max)^(β-2)) / (1 - (P_min/P_max)^β)，注意 β=0.9<2 时 α-2 为负数，需验证积分收敛性

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布的二阶矩公式推导正确，且β=0.9<2时积分收敛性验证无误
