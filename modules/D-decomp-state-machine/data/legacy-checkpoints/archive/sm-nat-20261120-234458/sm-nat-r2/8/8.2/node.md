# N66: 更新概率 P_update_within_residence 的精确计算：P = 1 - exp(-λ_update * T_residence)，代入 λ_u

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

更新概率 P_update_within_residence 的精确计算：P = 1 - exp(-λ_update * T_residence)，代入 λ_update = 0.01/day 和 T_residence = 1/500 day，P ≈ 1 - exp(-0.00002) ≈ 0.00002，折减因子 ≈ 0.99998

## Corrected Claim

更新概率 P_update_within_residence 的精确计算：P = 1 - exp(-λ_update * T_residence)，代入 λ_update = 0.01/day 和 T_residence = 1/500 day，P ≈ 1 - exp(-0.00002) ≈ 0.00002，折减因子 ≈ 0.99998

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程更新概率公式 P=1-exp(-λt) 应用正确，数值计算 1-exp(-0.00002) ≈ 0.00002 符合泰勒展开近似，折减因子 1-P ≈ 0.99998 逻辑自洽。
