# N544: K_peak 的高值风险：在大型直播或热点事件期间，K_peak 可瞬时飙升至 5.0-6.0 倍，若容量规划仅按 K_peak=3.5 设计，峰值期间将出现带

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N179

## Claim

K_peak 的高值风险：在大型直播或热点事件期间，K_peak 可瞬时飙升至 5.0-6.0 倍，若容量规划仅按 K_peak=3.5 设计，峰值期间将出现带宽拥塞导致 P99 延迟超标，需预留 30%-50% 的弹性带宽冗余或采用按量计费模式以应对突发流量。

## Corrected Claim

K_peak 的高值风险：在大型直播或热点事件期间，K_peak 可瞬时飙升至 5.0-6.0 倍，若容量规划仅按 K_peak=3.5 设计，峰值期间将出现带宽拥塞导致 P99 延迟超标，需预留 30%-50% 的弹性带宽冗余或采用按量计费模式以应对突发流量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN bandwidth surge during live streaming events
