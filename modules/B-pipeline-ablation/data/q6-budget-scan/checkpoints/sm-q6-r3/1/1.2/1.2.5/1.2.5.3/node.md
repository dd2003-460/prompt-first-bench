# N183: 公有云CDN P99延迟的方差来源：Anycast路由收敛时间（10-30s）+ 动态带宽分配（±20%波动）+ 边缘节点负载均衡不均（±10ms）；总方差σ²

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

公有云CDN P99延迟的方差来源：Anycast路由收敛时间（10-30s）+ 动态带宽分配（±20%波动）+ 边缘节点负载均衡不均（±10ms）；总方差σ²_cloud = σ²_routing + σ²_bandwidth + σ²_load_balance；P99延迟 = Mean + 2.33 * σ，若σ_cloud = 20ms，P99 ≈ Mean + 46.6ms

## Corrected Claim

公有云CDN P99延迟的方差来源：Anycast路由收敛时间（10-30s）+ 动态带宽分配（±20%波动）+ 边缘节点负载均衡不均（±10ms）；总方差σ²_cloud = σ²_routing + σ²_bandwidth + σ²_load_balance；P99延迟 = Mean + 2.33 * σ，若σ_cloud = 20ms，P99 ≈ Mean + 46.6ms

## Evidence

先验知识/题面给定，逻辑校验通过：方差可加性成立，正态分布P99系数2.33正确，数值计算2.33*20=46.6无误
