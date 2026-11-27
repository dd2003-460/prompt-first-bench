# N202: 共享随机源：买家成交估值噪声 ε_deal，其分布假设为 ε_deal ~ N(0, σ_deal^2)，其中 σ_deal 为成交决策的噪声标准差，通常 σ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

共享随机源：买家成交估值噪声 ε_deal，其分布假设为 ε_deal ~ N(0, σ_deal^2)，其中 σ_deal 为成交决策的噪声标准差，通常 σ_deal > σ_click，因为成交是高成本承诺行为。

## Corrected Claim

共享随机源：买家成交估值噪声 ε_deal，其分布假设为 ε_deal ~ N(0, σ_deal^2)，其中 σ_deal 为成交决策的噪声标准差，通常 σ_deal > σ_click，因为成交是高成本承诺行为。

## Evidence

先验知识/题面给定，逻辑校验通过：成交行为涉及更高的决策成本和不确定性，其噪声标准差通常大于点击行为，符合经济学直觉。
