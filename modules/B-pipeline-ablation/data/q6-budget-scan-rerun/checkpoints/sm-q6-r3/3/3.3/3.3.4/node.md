# N72: 对象大小分布对每千请求带宽成本的线性映射：Cost_bandwidth_per_1k = (s_avg × 1000 × 8 bits/byte) / 8640

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

对象大小分布对每千请求带宽成本的线性映射：Cost_bandwidth_per_1k = (s_avg × 1000 × 8 bits/byte) / 86400s / 1000 × unit_cost_Mbps_day。基于 s_avg = 2.05MB，计算每千请求的带宽消耗量为 2.05GB，对应带宽成本 = 2.05GB × unit_cost_per_GB。需量化 unit_cost_per_GB 在公有云（0.2元/GB）和自建（0.1元/GB）下的具体成本值。

## Corrected Claim

对象大小分布对每千请求带宽成本的线性映射：Cost_bandwidth_per_1k = (s_avg × 1000 × 8 bits/byte) / 86400s / 1000 × unit_cost_Mbps_day。基于 s_avg = 2.05MB，计算每千请求的带宽消耗量为 2.05GB，对应带宽成本 = 2.05GB × unit_cost_per_GB。需量化 unit_cost_per_GB 在公有云（0.2元/GB）和自建（0.1元/GB）下的具体成本值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公有云、自建、混合三种独立的基础设施场景，逻辑上互斥且正交；覆盖了父节点要求的公有云和自建具体成本量化，并额外提供了混合策略以体现线性映射的灵活性；虽然公有云和自建部分存在计算结构相似性，但输入参数（计费模式、单价、容量模型）完全不同，属于不同场景下的具体实例化，不构成冗余。）
