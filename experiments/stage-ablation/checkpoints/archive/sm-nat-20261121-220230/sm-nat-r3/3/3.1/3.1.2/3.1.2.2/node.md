# N163: Bottom 50% 冷门对象失效概率 P_invalid = 0.0297 的精确计算：P_invalid = 1 - exp(-u * T_resident

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Bottom 50% 冷门对象失效概率 P_invalid = 0.0297 的精确计算：P_invalid = 1 - exp(-u * T_resident)，其中 u=0.01/天，T_resident=3.0 天，P_invalid = 1 - exp(-0.03) ≈ 0.02955，折减系数 (1 - P_invalid) ≈ 0.97045，该值对 T_resident 的敏感度 ∂P_invalid/∂T_resident = u * exp(-u * T_resident) ≈ 0.00970/天。

## Corrected Claim

Bottom 50% 冷门对象失效概率 P_invalid = 0.0297 的精确计算：P_invalid = 1 - exp(-u * T_resident)，其中 u=0.01/天，T_resident=3.0 天，P_invalid = 1 - exp(-0.03) ≈ 0.02955，折减系数 (1 - P_invalid) ≈ 0.97045，该值对 T_resident 的敏感度 ∂P_invalid/∂T_resident = u * exp(-u * T_resident) ≈ 0.00970/天。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1-exp(-0.03)≈0.02955 及导数 u*exp(-u*T)≈0.00970 均准确无误
