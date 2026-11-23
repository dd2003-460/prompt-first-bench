# N392: 经验系数 1.5 的物理意义是峰值延迟放大因子，用于将平均 RTT 转换为 P99 延迟，若平均 RTT 为 20ms，则 P99 延迟估算为 $1.5 \ti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

经验系数 1.5 的物理意义是峰值延迟放大因子，用于将平均 RTT 转换为 P99 延迟，若平均 RTT 为 20ms，则 P99 延迟估算为 $1.5 \times 20 = 30$ms，该系数需根据实际流量分布和缓存命中率调整

## Corrected Claim

经验系数 1.5 的物理意义是峰值延迟放大因子，用于将平均 RTT 转换为 P99 延迟，若平均 RTT 为 20ms，则 P99 延迟估算为 $1.5 \times 20 = 30$ms，该系数需根据实际流量分布和缓存命中率调整

## Evidence

先验知识/题面给定，逻辑校验通过
