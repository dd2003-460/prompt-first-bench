# N210: ε_compliance=0.3的触发条件量化：合规压力仅在商品挂价>Median_P7D*1.25且未成交天数>14天时触发，此时流量惩罚系数为0.5；若未满

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

ε_compliance=0.3的触发条件量化：合规压力仅在商品挂价>Median_P7D*1.25且未成交天数>14天时触发，此时流量惩罚系数为0.5；若未满足条件，ε_compliance=0，总弹性降至0.5。

## Corrected Claim

ε_compliance=0.3的触发条件量化：合规压力仅在商品挂价>Median_P7D*1.25且未成交天数>14天时触发，此时流量惩罚系数为0.5；若未满足条件，ε_compliance=0，总弹性降至0.5。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

platform traffic penalty trigger condition high premium unsold
