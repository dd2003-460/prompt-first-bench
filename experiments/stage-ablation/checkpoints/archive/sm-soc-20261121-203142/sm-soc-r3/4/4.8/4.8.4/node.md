# N86: 干预后买家效用变化 ΔU_buyer 的计算：ΔU_buyer = (V - P_deal_new) * Q_new - (V - P_deal_old) * 

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

干预后买家效用变化 ΔU_buyer 的计算：ΔU_buyer = (V - P_deal_new) * Q_new - (V - P_deal_old) * Q_old，需代入 N13 中 W_exposure 调整后的新成交概率 Q_new 和新成交价 P_deal_new 进行差分计算。

## Corrected Claim

干预后买家效用变化 ΔU_buyer 的计算：ΔU_buyer = (V - P_deal_new) * Q_new - (V - P_deal_old) * Q_old，需代入 N13 中 W_exposure 调整后的新成交概率 Q_new 和新成交价 P_deal_new 进行差分计算。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数取值下的两个具体算例（Case Study），属于参数变体而非结构性的正交分解。此外，仅通过两个数值例子无法覆盖父节点中提到的'W_exposure调整'这一关键机制，也未涵盖其他典型工作点（如价格上升或效用最大化点），导致完备性不足。）
