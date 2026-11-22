# N71: 卖家临界干预强度计算：当平台展示真实成交价导致卖家挂价下调 ΔP 时，卖家剩余变化 ΔSS_seller = -ΔP * Prob(Sale) - C_wait

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

卖家临界干预强度计算：当平台展示真实成交价导致卖家挂价下调 ΔP 时，卖家剩余变化 ΔSS_seller = -ΔP * Prob(Sale) - C_wait_reduction。设定 Threshold_seller = 5% 利润下降，则临界干预强度对应于使 ΔSS_seller / Initial_Profit = -0.05 的 ΔP 值，该值与当前平均溢价率 (20%) 和成交概率弹性相关。

## Corrected Claim

卖家临界干预强度计算：当平台展示真实成交价导致卖家挂价下调 ΔP 时，卖家剩余变化 ΔSS_seller = -ΔP * Prob(Sale) - C_wait_reduction。设定 Threshold_seller = 5% 利润下降，则临界干预强度对应于使 ΔSS_seller / Initial_Profit = -0.05 的 ΔP 值，该值与当前平均溢价率 (20%) 和成交概率弹性相关。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了基于利润下降阈值的临界干预强度计算模型，公式结构（剩余价值变化=价格损失*成交概率-等待成本减少）符合经济学直觉，量纲与逻辑自洽。

## Search Query

seller surplus loss threshold price transparency intervention 5 percent
