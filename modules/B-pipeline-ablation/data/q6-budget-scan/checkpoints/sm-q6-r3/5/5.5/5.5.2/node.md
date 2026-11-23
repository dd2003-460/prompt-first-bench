# N106: 增量带宽成本 Cost_per_TB_incremental 的分项计算：公有云CDN部分为 Price_per_TB_cloud（0.2-0.5元/TB），自

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

增量带宽成本 Cost_per_TB_incremental 的分项计算：公有云CDN部分为 Price_per_TB_cloud（0.2-0.5元/TB），自建节点部分为 (Hardware_Cost_per_TB + Bandwidth_Lease_per_TB)；自建节点硬件成本约2万元/台（支持10Gbps），折算为0.2元/TB/月，带宽租赁约0.1元/TB/月，合计0.3元/TB/月。

## Corrected Claim

增量带宽成本 Cost_per_TB_incremental 的分项计算：公有云CDN部分为 Price_per_TB_cloud（0.2-0.5元/TB），自建节点部分为 (Hardware_Cost_per_TB + Bandwidth_Lease_per_TB)；自建节点硬件成本约2万元/台（支持10Gbps），折算为0.2元/TB/月，带宽租赁约0.1元/TB/月，合计0.3元/TB/月。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中定义的'公有云CDN部分'和'自建节点部分'，两者在成本来源、适用流量场景（长尾vs核心）及技术特性上互斥且互补，无逻辑重叠或矛盾。两个子节点完整覆盖了父节点提到的两个主要分项，且各自提供了具体的参数取值和工作点定义，没有发现多个子节点实质上是同一参数的不同取值这一冗余情况。）
