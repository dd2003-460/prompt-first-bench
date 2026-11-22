# N160: 平台净收益 ΔRev 的估算公式：ΔRev = ΔGMV * r - ΔC_total，其中 ΔGMV 为干预后GMV增量（基于 Q_short 和 P_new

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

平台净收益 ΔRev 的估算公式：ΔRev = ΔGMV * r - ΔC_total，其中 ΔGMV 为干预后GMV增量（基于 Q_short 和 P_new 计算），r=0.05，ΔC_total = C_display + C_data_processing * T_horizon；若 T_horizon=365天，ΔC_total ≈ 50000 + 280*365 = 152,200元，需 ΔRev > 152,200元 才能盈利。

## Corrected Claim

平台净收益 ΔRev 的估算公式：ΔRev = ΔGMV * r - ΔC_total，其中 ΔGMV 为干预后GMV增量（基于 Q_short 和 P_new 计算），r=0.05，ΔC_total = C_display + C_data_processing * T_horizon；若 T_horizon=365天，ΔC_total ≈ 50000 + 280*365 = 152,200元，需 ΔRev > 152,200元 才能盈利。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合基本经济逻辑（收益=增量GMV*变现率-总成本），数值计算 50000 + 280*365 = 50000 + 102200 = 152200 准确无误，量纲一致。
