# N82: 边缘缓存命中率 H_edge 的理论上限由工作集大小决定：H_edge_max = 1 - (N_unique_active / Cache_Capacity_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

边缘缓存命中率 H_edge 的理论上限由工作集大小决定：H_edge_max = 1 - (N_unique_active / Cache_Capacity_Objects)，其中 N_unique_active 为 TTL 窗口内活跃唯一对象数，Cache_Capacity_Objects = 单节点总存储 / s_avg

## Corrected Claim

边缘缓存命中率 H_edge 的理论上限由工作集大小决定：H_edge_max = 1 - (N_unique_active / Cache_Capacity_Objects)，其中 N_unique_active 为 TTL 窗口内活跃唯一对象数，Cache_Capacity_Objects = 单节点总存储 / s_avg

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了父节点公式中的两个核心变量（N_unique_active 和 Cache_Capacity_Objects）以及边界条件（容量不足时的降级策略），三者逻辑独立且互补，共同构成了对理论上限完整且无冲突的解释。）
