# N654: 公有云出网流量 Traffic_out_cloud 的峰值修正：在高峰时段（K_peak=3），实际出网流量 Traffic_out_peak = 200GB/

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

公有云出网流量 Traffic_out_cloud 的峰值修正：在高峰时段（K_peak=3），实际出网流量 Traffic_out_peak = 200GB/day * 3 * (1 - H_peak)，其中 H_peak 为高峰命中率（通常低于日均 5-10%，因突发热点未预热），导致峰值带宽需求需按 1.5-2 倍冗余预留，影响带宽租赁模式选择。

## Corrected Claim

公有云出网流量 Traffic_out_cloud 的峰值修正：在高峰时段（K_peak=3），实际出网流量 Traffic_out_peak = 200GB/day * 3 * (1 - H_peak)，其中 H_peak 为高峰命中率（通常低于日均 5-10%，因突发热点未预热），导致峰值带宽需求需按 1.5-2 倍冗余预留，影响带宽租赁模式选择。

## Evidence

先验知识/题面给定，逻辑校验通过
