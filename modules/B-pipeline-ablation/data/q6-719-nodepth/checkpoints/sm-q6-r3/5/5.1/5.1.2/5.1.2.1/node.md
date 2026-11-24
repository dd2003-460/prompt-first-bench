# N301: 自动扩容触发阈值 ΔThreshold 通常为当前预置容量的 80%-90%，当实时流量超过该阈值时触发扩容，该阈值决定了扩容响应窗口 T_scaling 内的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

自动扩容触发阈值 ΔThreshold 通常为当前预置容量的 80%-90%，当实时流量超过该阈值时触发扩容，该阈值决定了扩容响应窗口 T_scaling 内的流量溢出比例，进而影响队列等待时间。

## Corrected Claim

自动扩容触发阈值 ΔThreshold 通常为当前预置容量的 80%-90%，当实时流量超过该阈值时触发扩容，该阈值决定了扩容响应窗口 T_scaling 内的流量溢出比例，进而影响队列等待时间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud CDN auto scaling trigger threshold percentage capacity
