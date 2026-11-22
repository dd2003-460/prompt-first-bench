# N160: Top 10% 热门对象失效概率 P_invalid = 0.005 的精确计算：P_invalid = 1 - exp(-u * T_resident)，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

Top 10% 热门对象失效概率 P_invalid = 0.005 的精确计算：P_invalid = 1 - exp(-u * T_resident)，其中 u=0.01/天，T_resident=0.5 天，P_invalid = 1 - exp(-0.005) ≈ 0.00499，折减系数 (1 - P_invalid) ≈ 0.99501，该值对 T_resident 的敏感度 ∂P_invalid/∂T_resident = u * exp(-u * T_resident) ≈ 0.00995/天。

## Corrected Claim

Top 10% 热门对象失效概率 P_invalid = 0.005 的精确计算：P_invalid = 1 - exp(-u * T_resident)，其中 u=0.01/天，T_resident=0.5 天，P_invalid = 1 - exp(-0.005) ≈ 0.00499，折减系数 (1 - P_invalid) ≈ 0.99501，该值对 T_resident 的敏感度 ∂P_invalid/∂T_resident = u * exp(-u * T_resident) ≈ 0.00995/天。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P=1-exp(-uT) 代入 u=0.01, T=0.5 得 1-exp(-0.005)≈0.0049875，与 0.00499 一致；导数 dP/dT = u*exp(-uT) ≈ 0.01*0.995 ≈ 0.00995，计算无误。
