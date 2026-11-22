# N80: 买家旧均衡效用基准：U_buyer(old) = V(Good) - P_paid_old - S_cost_old，其中 P_paid_old 为实际成交均价

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

买家旧均衡效用基准：U_buyer(old) = V(Good) - P_paid_old - S_cost_old，其中 P_paid_old 为实际成交均价，S_cost_old 为搜索成本（含时间成本 λ*Time 和认知成本），V(Good) 为买家对商品的估值。

## Corrected Claim

买家旧均衡效用基准：U_buyer(old) = V(Good) - P_paid_old - S_cost_old，其中 P_paid_old 为实际成交均价，S_cost_old 为搜索成本（含时间成本 λ*Time 和认知成本），V(Good) 为买家对商品的估值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个独立变量：V(Good)、P_paid_old 和 S_cost_old。其中 S_cost_old 被进一步分解为时间分量（S_time_old）和认知分量（S_cog_old），这两个分量在定义上是互补且不重叠的（一个基于时间/机会成本，一个基于心理资源/比较次数）。所有关键组成部分均已覆盖，且不存在将同一参数拆分为不同取值导致的冗余。）
