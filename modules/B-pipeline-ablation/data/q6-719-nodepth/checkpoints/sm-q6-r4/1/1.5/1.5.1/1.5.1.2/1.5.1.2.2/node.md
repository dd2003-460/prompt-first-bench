# N546: 若源站出口带宽缩减至 B_origin=300Mbps 以降低成本，未命中流量峰值需求 222Mbps 导致链路利用率 U = 222/300 = 74%，接近

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N185

## Claim

若源站出口带宽缩减至 B_origin=300Mbps 以降低成本，未命中流量峰值需求 222Mbps 导致链路利用率 U = 222/300 = 74%，接近饱和阈值，排队延迟显著上升，属于高成本敏感/高风险工作点。

## Corrected Claim

若源站出口带宽缩减至 B_origin=300Mbps 以降低成本，未命中流量峰值需求 222Mbps 导致链路利用率 U = 222/300 = 74%，接近饱和阈值，排队延迟显著上升，属于高成本敏感/高风险工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：222/300=0.74计算正确，且74%利用率在排队论中确实对应显著延迟上升的高风险区间。
