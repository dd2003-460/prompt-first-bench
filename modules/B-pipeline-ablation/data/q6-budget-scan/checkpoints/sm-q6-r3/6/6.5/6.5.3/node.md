# N285: 跨境链路延迟对 P99 的影响量化：跨境回源或边缘节点位于海外时，RTT 增加 Δt_cross ≈ 80-150ms（取决于距离，如中美 RTT ~150ms

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

跨境链路延迟对 P99 的影响量化：跨境回源或边缘节点位于海外时，RTT 增加 Δt_cross ≈ 80-150ms（取决于距离，如中美 RTT ~150ms，中日 ~30ms）；若 P99 目标 T < 200ms，则跨境用户请求必须命中海外边缘缓存，否则 P99 超标概率趋近于 1，导致策略不可行或需额外支付 QoS 加速费

## Corrected Claim

跨境链路延迟对 P99 的影响量化：跨境回源或边缘节点位于海外时，RTT 增加 Δt_cross ≈ 80-150ms（取决于距离，如中美 RTT ~150ms，中日 ~30ms）；若 P99 目标 T < 200ms，则跨境用户请求必须命中海外边缘缓存，否则 P99 超标概率趋近于 1，导致策略不可行或需额外支付 QoS 加速费

## Evidence

先验知识/题面给定，逻辑校验通过：中美RTT~150ms、中日~30ms符合物理常识；若P99<200ms且RTT已占150ms，剩余预算仅50ms，未命中缓存导致回源必然超时，推导自洽。

## Search Query

cross border CDN latency RTT impact on P99 SLO
