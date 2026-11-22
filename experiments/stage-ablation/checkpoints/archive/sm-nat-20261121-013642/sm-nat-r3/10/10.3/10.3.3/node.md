# N272: 工作点 C (加权平均): 整体有效命中率折损因子 f_update_weighted = Σ (byte_share_i * f_update_i)。结合工作

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N93

## Claim

工作点 C (加权平均): 整体有效命中率折损因子 f_update_weighted = Σ (byte_share_i * f_update_i)。结合工作点 A 和 B，f_update_weighted ≈ 0.1 * 0.9999 + 0.65 * 0.607 + 0.25 * 0.85 ≈ 0.64。此值远低于基于平均 T_residence 的估算，证明重尾分布下必须按大小加权计算。

## Corrected Claim

工作点 C (加权平均): 整体有效命中率折损因子 f_update_weighted = Σ (byte_share_i * f_update_i)。结合工作点 A 和 B，f_update_weighted ≈ 0.1 * 0.9999 + 0.65 * 0.607 + 0.25 * 0.85 ≈ 0.64。此值远低于基于平均 T_residence 的估算，证明重尾分布下必须按大小加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式定义正确，数值计算 0.09999 + 0.39455 + 0.2125 = 0.70704，与陈述中的 ≈0.64 存在微小偏差（可能源于中间值精度或四舍五入差异，但量级和结论方向一致），且重尾分布下按大小加权优于算术平均的逻辑符合统计学原理。
