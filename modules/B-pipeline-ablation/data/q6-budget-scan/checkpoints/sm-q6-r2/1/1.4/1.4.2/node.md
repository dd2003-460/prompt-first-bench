# N47: 针对短视频请求（s_video=5-10MB），在典型B_effective=100Mbps下，T_transmission计算值为 40-80ms，均大于RT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

针对短视频请求（s_video=5-10MB），在典型B_effective=100Mbps下，T_transmission计算值为 40-80ms，均大于RTT_base(10-50ms)，判定为带宽受限(bandwidth-bound)

## Corrected Claim

针对短视频请求（s_video=5-10MB），在典型B_effective=100Mbps下，T_transmission计算值为 40-80ms，均大于RTT_base(10-50ms)，判定为带宽受限(bandwidth-bound)

## Evidence

先验知识/题面给定，逻辑校验通过：5MB/100Mbps=40ms, 10MB/100Mbps=80ms，计算无误且大于RTT_base，符合带宽受限判定逻辑
