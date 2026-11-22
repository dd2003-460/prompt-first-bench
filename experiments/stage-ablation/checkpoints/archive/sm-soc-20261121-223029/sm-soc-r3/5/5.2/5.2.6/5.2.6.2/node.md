# N315: 曝光弹性 E 的对数-对数回归模型：ln(Exposure) = α + E * ln(F_update) + β_ctrl * ln(Price) + γ_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

曝光弹性 E 的对数-对数回归模型：ln(Exposure) = α + E * ln(F_update) + β_ctrl * ln(Price) + γ_ctrl * ln(Seller_Rating) + ε，其中 E 为待估弹性系数，需控制价格水平及卖家评分以隔离更新频率的独立影响。

## Corrected Claim

曝光弹性 E 的对数-对数回归模型：ln(Exposure) = α + E * ln(F_update) + β_ctrl * ln(Price) + γ_ctrl * ln(Seller_Rating) + ε，其中 E 为待估弹性系数，需控制价格水平及卖家评分以隔离更新频率的独立影响。

## Evidence

先验知识/题面给定，逻辑校验通过
