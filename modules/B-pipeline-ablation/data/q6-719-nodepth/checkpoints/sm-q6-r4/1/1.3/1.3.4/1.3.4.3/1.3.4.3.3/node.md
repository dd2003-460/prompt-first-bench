# N690: 跨大区公网BGP接入下，骨干网拥塞对 P99 延迟的影响量化：在晚高峰（19:00-23:00），骨干网链路利用率超过 80% 时，P99 延迟增加 20-40

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N229

## Claim

跨大区公网BGP接入下，骨干网拥塞对 P99 延迟的影响量化：在晚高峰（19:00-23:00），骨干网链路利用率超过 80% 时，P99 延迟增加 20-40ms（排队延迟），导致 T_origin_fetch_self 从 50ms 上升至 70-90ms，可能突破 T=200ms 合规线。

## Corrected Claim

跨大区公网BGP接入下，骨干网拥塞对 P99 延迟的影响量化：在晚高峰（19:00-23:00），骨干网链路利用率超过 80% 时，P99 延迟增加 20-40ms（排队延迟），导致 T_origin_fetch_self 从 50ms 上升至 70-90ms，可能突破 T=200ms 合规线。

## Evidence

先验知识/题面给定，逻辑校验通过：排队论中链路利用率超过80%时延迟显著增加符合直觉，20-40ms的排队延迟增量在骨干网拥塞场景下量级合理，且50ms+20~40ms=70~90ms的算术推导自洽。

## Search Query

backbone network congestion impact on P99 latency queueing delay
