# N184: 卖家期望边际收益 E[Margin_t] 的动态计算：E[Margin_t] = Margin_avg * P_success(t)，其中 Margin_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

卖家期望边际收益 E[Margin_t] 的动态计算：E[Margin_t] = Margin_avg * P_success(t)，其中 Margin_avg 为干预后的平均利润率（10-15%），P_success(t) 为 t 期内的成交概率，随时间 t 增加呈指数衰减 e^(-λt)。

## Corrected Claim

卖家期望边际收益 E[Margin_t] 的动态计算：E[Margin_t] = Margin_avg * P_success(t)，其中 Margin_avg 为干预后的平均利润率（10-15%），P_success(t) 为 t 期内的成交概率，随时间 t 增加呈指数衰减 e^(-λt)。

## Evidence

先验知识/题面给定，逻辑校验通过：期望收益等于平均收益乘以成功概率，且成交概率随时间指数衰减符合经典排队论/搜索模型直觉，数值量级（10-15%利润率）合理。

## Search Query

seller expected margin dynamic success probability decay
