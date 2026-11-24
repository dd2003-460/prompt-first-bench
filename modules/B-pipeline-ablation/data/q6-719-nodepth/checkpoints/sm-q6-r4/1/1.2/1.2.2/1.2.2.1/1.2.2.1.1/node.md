# N464: CDN 边缘节点 RTT 对数正态分布参数 μ 的估算：μ = ln(Geometric_Mean_RTT)，若实测 P50 RTT 为 20ms，则 μ ≈ 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

CDN 边缘节点 RTT 对数正态分布参数 μ 的估算：μ = ln(Geometric_Mean_RTT)，若实测 P50 RTT 为 20ms，则 μ ≈ ln(20) ≈ 2.996，该值直接决定 P99 延迟的基准水平。

## Corrected Claim

CDN 边缘节点 RTT 对数正态分布参数 μ 的估算：μ = ln(Geometric_Mean_RTT)，若实测 P50 RTT 为 20ms，则 μ ≈ ln(20) ≈ 2.996，该值直接决定 P99 延迟的基准水平。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布中位数等于 exp(μ)，故 μ=ln(P50)；ln(20)≈2.996 计算正确；μ 确实决定分布中心位置，进而影响 P99 基准。
