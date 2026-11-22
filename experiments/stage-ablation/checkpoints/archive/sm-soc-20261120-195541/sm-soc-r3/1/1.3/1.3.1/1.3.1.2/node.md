# N87: 季节性波动期间 α = 0.02/day 的触发条件：当节假日前后 7 天内，买家搜索量下降超过 20% 或卖家供给量上升超过 30% 时，α 翻倍；该阈值需通

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

季节性波动期间 α = 0.02/day 的触发条件：当节假日前后 7 天内，买家搜索量下降超过 20% 或卖家供给量上升超过 30% 时，α 翻倍；该阈值需通过时间序列分解（STL）识别季节性分量对成交周期的影响系数。

## Corrected Claim

季节性波动期间 α = 0.02/day 的触发条件：当节假日前后 7 天内，买家搜索量下降超过 20% 或卖家供给量上升超过 30% 时，α 翻倍；该阈值需通过时间序列分解（STL）识别季节性分量对成交周期的影响系数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seasonal impact on time discount rate used goods market holidays
