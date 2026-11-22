# N55: 卖家接受降价的临界持有时间 T_critical 满足方程 C_storage * T_critical + C_time * T_critical = λ_l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

卖家接受降价的临界持有时间 T_critical 满足方程 C_storage * T_critical + C_time * T_critical = λ_loss * (V_seller - P_mkt)，解得 T_critical = λ_loss * ΔP / (C_storage + C_time)。

## Corrected Claim

卖家接受降价的临界持有时间 T_critical 满足方程 C_storage * T_critical + C_time * T_critical = λ_loss * (V_seller - P_mkt)，解得 T_critical = λ_loss * ΔP / (C_storage + C_time)。

## Evidence

先验知识/题面给定，逻辑校验通过：方程左侧为总持有成本（存储+时间），右侧为损失期望，代数求解 T_critical = λ_loss * ΔP / (C_storage + C_time) 正确且量纲自洽。
