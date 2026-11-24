# N306: 跨AZ P99延迟 T_cross_az_p99 的构成：T_cross_az_p99 = T_same_az_base + σ_cross_az_p99，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

跨AZ P99延迟 T_cross_az_p99 的构成：T_cross_az_p99 = T_same_az_base + σ_cross_az_p99，其中 T_same_az_base 为同AZ基础P99延迟（通常 50-100ms），σ_cross_az_p99 为跨AZ额外延迟的P99值（通常 3-8ms，高于平均值1-3ms），该值需计入总P99分布。

## Corrected Claim

跨AZ P99延迟 T_cross_az_p99 的构成：T_cross_az_p99 = T_same_az_base + σ_cross_az_p99，其中 T_same_az_base 为同AZ基础P99延迟（通常 50-100ms），σ_cross_az_p99 为跨AZ额外延迟的P99值（通常 3-8ms，高于平均值1-3ms），该值需计入总P99分布。

## Evidence

先验知识/题面给定，逻辑校验通过
