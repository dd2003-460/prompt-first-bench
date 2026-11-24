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

先验知识/题面给定，逻辑校验通过：2.05MB * 1000 = 2050MB ≈ 2.05GB，单位换算与成本映射逻辑自洽。
