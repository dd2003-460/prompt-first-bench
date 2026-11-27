# N241: 工作点3（低溢价-高匹配）：P_ask_new = 1.05 * P_market，此时需 P_wtp > 1.05 * P_market 且 Q_matche

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

工作点3（低溢价-高匹配）：P_ask_new = 1.05 * P_market，此时需 P_wtp > 1.05 * P_market 且 Q_matched ≥ Q_base；该工作点下 ΔCS_buyer = (P_wtp - 1.05 * P_market) * Q_matched，买家剩余最大，但卖家利润空间被极度压缩，可能导致 Q_matched 因卖家退出而下降，需验证 Q_matched 的弹性约束。

## Corrected Claim

工作点3（低溢价-高匹配）：P_ask_new = 1.05 * P_market，此时需 P_wtp > 1.05 * P_market 且 Q_matched ≥ Q_base；该工作点下 ΔCS_buyer = (P_wtp - 1.05 * P_market) * Q_matched，买家剩余最大，但卖家利润空间被极度压缩，可能导致 Q_matched 因卖家退出而下降，需验证 Q_matched 的弹性约束。

## Evidence

先验知识/题面给定，逻辑校验通过：买家剩余公式符合定义，低溢价高匹配工作点的经济直觉（卖家利润压缩导致供给弹性风险）自洽。
