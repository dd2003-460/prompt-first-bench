# N414: 综合伤害系数 H_seller 的数值计算：H_seller = Δπ_seller + ΔC_hold / P_ref。代入 Δπ_seller = 0.12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

综合伤害系数 H_seller 的数值计算：H_seller = Δπ_seller + ΔC_hold / P_ref。代入 Δπ_seller = 0.125 和 ΔC_hold / P_ref = w * 0.125 * T_0。若 w * T_0 ≈ 0.00411，则 ΔC_hold / P_ref ≈ 0.00411 * 0.125 ≈ 0.000514。H_seller ≈ 0.125 + 0.000514 ≈ 0.1255。

## Corrected Claim

综合伤害系数 H_seller 的数值计算：H_seller = Δπ_seller + ΔC_hold / P_ref。代入 Δπ_seller = 0.125 和 ΔC_hold / P_ref = w * 0.125 * T_0。若 w * T_0 ≈ 0.00411，则 ΔC_hold / P_ref ≈ 0.00411 * 0.125 ≈ 0.000514。H_seller ≈ 0.125 + 0.000514 ≈ 0.1255。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.00411 * 0.125 = 0.00051375 ≈ 0.000514，0.125 + 0.000514 = 0.125514 ≈ 0.1255，数值推导自洽。
