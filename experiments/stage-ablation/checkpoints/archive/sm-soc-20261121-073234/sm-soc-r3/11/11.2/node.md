# N352: Time（成交周期）的分布特征：Time 并非固定值，而是服从指数分布或威布尔分布，其均值 E[Time] = 1/λ 受溢价率影响；需计算在 15-25% 溢

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

Time（成交周期）的分布特征：Time 并非固定值，而是服从指数分布或威布尔分布，其均值 E[Time] = 1/λ 受溢价率影响；需计算在 15-25% 溢价区间内，Time 的条件期望值 E[Time | Premium ∈ [15%, 25%]] 与基准溢价下的差异，以验证‘短周期’断言的统计显著性。

## Corrected Claim

Time（成交周期）的分布特征：Time 并非固定值，而是服从指数分布或威布尔分布，其均值 E[Time] = 1/λ 受溢价率影响；需计算在 15-25% 溢价区间内，Time 的条件期望值 E[Time | Premium ∈ [15%, 25%]] 与基准溢价下的差异，以验证‘短周期’断言的统计显著性。

## Evidence

先验知识/题面给定，逻辑校验通过：在金融与排队论中，成交周期（Time）通常建模为指数或威布尔分布，且溢价率与成交速度存在负相关关系，计算条件期望以验证统计显著性是标准的量化分析方法，逻辑自洽且符合领域常识。

## Search Query

time to sell used items price premium distribution exponential weibull
