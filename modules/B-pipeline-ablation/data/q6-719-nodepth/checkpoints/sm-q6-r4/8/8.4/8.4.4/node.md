# N384: 激进自建（低冗余/高弹性惩罚工作点，如仅5个POP无跨域备份）：Elasticity_Penalty = 5 × (0.1 × 0.5 × 500k) = 12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

激进自建（低冗余/高弹性惩罚工作点，如仅5个POP无跨域备份）：Elasticity_Penalty = 5 × (0.1 × 0.5 × 500k) = 125k元/月（假设单POP故障影响50%流量，无冗余降级），Geo_Policy_Premium = 5 × 5k = 25k元/月，总 Risk_Premium = 150k元/月，展示降低冗余导致的风险成本非线性上升。

## Corrected Claim

激进自建（低冗余/高弹性惩罚工作点，如仅5个POP无跨域备份）：Elasticity_Penalty = 5 × (0.1 × 0.5 × 500k) = 125k元/月（假设单POP故障影响50%流量，无冗余降级），Geo_Policy_Premium = 5 × 5k = 25k元/月，总 Risk_Premium = 150k元/月，展示降低冗余导致的风险成本非线性上升。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（5*0.1*0.5*500k=125k, 5*5k=25k, 总和150k），且符合低冗余架构风险成本上升的逻辑直觉。

## Search Query

CDN single point of failure risk cost model
