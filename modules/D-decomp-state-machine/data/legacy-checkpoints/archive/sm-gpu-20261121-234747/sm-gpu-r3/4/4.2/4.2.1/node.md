# N105: 定义'多源一致'的具体判定标准：需至少2个独立权威来源（如NVIDIA官方Spec Sheet与AnandTech/ServerServing评测）数值偏差<5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18, N19, N20

## Claim

定义'多源一致'的具体判定标准：需至少2个独立权威来源（如NVIDIA官方Spec Sheet与AnandTech/ServerServing评测）数值偏差<5%，且发布时间均在最近12个月内；若偏差>5%或来源单一，置信度降为'中'

## Corrected Claim

定义'多源一致'的具体判定标准：需至少2个独立权威来源（如NVIDIA官方Spec Sheet与AnandTech/ServerServing评测）数值偏差<5%，且发布时间均在最近12个月内；若偏差>5%或来源单一，置信度降为'中'

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1严格复现了父节点中关于技术规格（如Spec Sheet）的判定逻辑（5%偏差、12个月时效），而子节点2针对父节点未明确覆盖但逻辑上必然存在的‘例外情况’（如价格波动性大的参数）进行了补充，两者在适用对象上互斥且互补，无重复或矛盾。）
