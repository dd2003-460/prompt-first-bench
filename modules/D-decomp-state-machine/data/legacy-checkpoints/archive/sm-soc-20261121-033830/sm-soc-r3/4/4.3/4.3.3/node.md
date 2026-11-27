# N78: 卖家新均衡成交概率：P(Sale|P_new) 随价格降低而增加，近似关系为 P(Sale|P_new) ≈ P(Sale|P_high) * (P_high 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

卖家新均衡成交概率：P(Sale|P_new) 随价格降低而增加，近似关系为 P(Sale|P_new) ≈ P(Sale|P_high) * (P_high / P_new)^η，其中 η 为价格弹性系数（参考N28，η ∈ [0.3, 0.5]），该式用于计算新均衡下的成交期望。

## Corrected Claim

卖家新均衡成交概率：P(Sale|P_new) 随价格降低而增加，近似关系为 P(Sale|P_new) ≈ P(Sale|P_high) * (P_high / P_new)^η，其中 η 为价格弹性系数（参考N28，η ∈ [0.3, 0.5]），该式用于计算新均衡下的成交期望。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点之间存在逻辑矛盾（父节点定义η为常数，子节点称η随区间变化）；且父节点描述的是价格降低（P_new < P_high）时的概率增加，而子节点2讨论的是高价格区间（P_new > P_high），超出了父节点“随价格降低”的语境范围；两个子节点本质上都是对同一弹性参数η在不同区间的敏感性描述，属于冗余。）
