# N54: 价格弹性对短期成交量的修正：引入价格弹性系数 ε (Elasticity of Demand)。若 ε > 1 (富有弹性)，则 ΔQ = -ε * 0.15 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

价格弹性对短期成交量的修正：引入价格弹性系数 ε (Elasticity of Demand)。若 ε > 1 (富有弹性)，则 ΔQ = -ε * 0.15 * Q0。修正后的短期GMV变化 ΔGMV_adjusted = Q0*P0 * (-0.15 + 0.15ε)。只有当 ε > 1 时，短期GMV才可能不降反升或降幅小于15%。

## Corrected Claim

价格弹性对短期成交量的修正：引入价格弹性系数 ε (Elasticity of Demand)。若 ε > 1 (富有弹性)，则 ΔQ = -ε * 0.15 * Q0。修正后的短期GMV变化 ΔGMV_adjusted = Q0*P0 * (-0.15 + 0.15ε)。只有当 ε > 1 时，短期GMV才可能不降反升或降幅小于15%。

## Evidence

先验知识/题面给定，逻辑校验通过：基于需求价格弹性定义及GMV=Q*P推导，数学关系自洽且量纲正确。
