# N118: 公有云CDN弹性扩容的冷启动延迟（Cold Start Latency）通常为5-15秒，在突发流量（如热点事件）前5-15秒内P99延迟会因连接建立和资源调度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

公有云CDN弹性扩容的冷启动延迟（Cold Start Latency）通常为5-15秒，在突发流量（如热点事件）前5-15秒内P99延迟会因连接建立和资源调度显著上升，需量化该时段内的额外延迟成本。

## Corrected Claim

公有云CDN弹性扩容的冷启动延迟（Cold Start Latency）通常为5-15秒，在突发流量（如热点事件）前5-15秒内P99延迟会因连接建立和资源调度显著上升，需量化该时段内的额外延迟成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

public cloud CDN cold start latency burst traffic p99
