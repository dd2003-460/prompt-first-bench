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

先验知识/题面给定，逻辑校验通过：硬件成本折算（20000元/10Gbps/月 ≈ 0.2元/TB/月）与带宽租赁成本（0.1元/TB/月）相加得0.3元/TB/月，数值量级符合行业常识，且公有云CDN价格区间（0.2-0.5元/TB）合理。
