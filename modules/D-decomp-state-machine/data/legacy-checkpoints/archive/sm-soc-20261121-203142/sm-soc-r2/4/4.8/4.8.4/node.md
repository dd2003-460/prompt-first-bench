# N86: 干预后买家效用变化 ΔU_buyer 的计算：ΔU_buyer = (V - P_deal_new) * Q_new - (V - P_deal_old) * 

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：公式符合消费者剩余（效用）定义，即（价值-价格）*数量，且差分逻辑自洽。
