# N285: 合规成本 C_compliance 在低影响场景下的工作点：N_affected < 1000 且 δc < 0.01 时，C_compliance ≈ C_n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

合规成本 C_compliance 在低影响场景下的工作点：N_affected < 1000 且 δc < 0.01 时，C_compliance ≈ C_notification * 1000 + C_legal * P_avg * 0.01 ≈ $50 + 0.02 * P_avg，总成本约为 $50 + 0.02 * P_avg。

## Corrected Claim

合规成本 C_compliance 在低影响场景下的工作点：N_affected < 1000 且 δc < 0.01 时，C_compliance ≈ C_notification * 1000 + C_legal * P_avg * 0.01 ≈ $50 + 0.02 * P_avg，总成本约为 $50 + 0.02 * P_avg。

## Evidence

先验知识/题面给定，逻辑校验通过：数值代入与算术运算自洽（1000*0.01=10, 10*0.005=0.05, 0.05*0.4=0.02），符合合规成本模型的低影响场景估算逻辑。
