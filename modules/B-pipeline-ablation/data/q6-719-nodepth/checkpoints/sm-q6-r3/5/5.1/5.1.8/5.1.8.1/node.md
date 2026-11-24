# N320: T_cloud_fallback 的量化估算：假设核心 POP 到公有云源站的 RTT_to_cloud 为 20ms（同省/邻近区域），T_cloud_pro

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

T_cloud_fallback 的量化估算：假设核心 POP 到公有云源站的 RTT_to_cloud 为 20ms（同省/邻近区域），T_cloud_processing 为 50ms（含缓存未命中时的回源处理），则 T_cloud_fallback = 70ms。若本地缓存 T_cache 为 10ms，则 ΔP99_hybrid = 0.2 × (70 - 10) = 12ms。

## Corrected Claim

T_cloud_fallback 的量化估算：假设核心 POP 到公有云源站的 RTT_to_cloud 为 20ms（同省/邻近区域），T_cloud_processing 为 50ms（含缓存未命中时的回源处理），则 T_cloud_fallback = 70ms。若本地缓存 T_cache 为 10ms，则 ΔP99_hybrid = 0.2 × (70 - 10) = 12ms。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.2 * (70 - 10) = 12 正确，且 20ms RTT 与 50ms 处理时间在邻近区域场景下量级合理。
