# N395: 骨干网拥塞导致的排队延迟 T_queue_L1_L2 (ms) 的 P99 估计：在非高峰期为 0-2ms，在晚高峰（19:00-22:00）由于带宽利用率超过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

骨干网拥塞导致的排队延迟 T_queue_L1_L2 (ms) 的 P99 估计：在非高峰期为 0-2ms，在晚高峰（19:00-22:00）由于带宽利用率超过 80%，P99 排队延迟可达 5-15ms，取决于 QoS 策略和链路负载率。

## Corrected Claim

骨干网拥塞导致的排队延迟 T_queue_L1_L2 (ms) 的 P99 估计：在非高峰期为 0-2ms，在晚高峰（19:00-22:00）由于带宽利用率超过 80%，P99 排队延迟可达 5-15ms，取决于 QoS 策略和链路负载率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

backbone network queueing delay P99 during peak hours
