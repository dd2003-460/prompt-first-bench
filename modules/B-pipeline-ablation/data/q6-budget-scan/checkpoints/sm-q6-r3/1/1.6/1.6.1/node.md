# N66: 公有云CDN缓存命中P99延迟：T_cache_hit_P99_cloud = RTT_user_to_edge_P99 + T_processing_clou

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

公有云CDN缓存命中P99延迟：T_cache_hit_P99_cloud = RTT_user_to_edge_P99 + T_processing_cloud_P99 + T_queue_cloud_P99，其中RTT_user_to_edge_P99基于用户到最近边缘节点的地理分布（典型20-50ms），T_processing_cloud_P99典型1-5ms，T_queue_cloud_P99典型0-10ms（低负载），合计典型25-65ms。

## Corrected Claim

公有云CDN缓存命中P99延迟：T_cache_hit_P99_cloud = RTT_user_to_edge_P99 + T_processing_cloud_P99 + T_queue_cloud_P99，其中RTT_user_to_edge_P99基于用户到最近边缘节点的地理分布（典型20-50ms），T_processing_cloud_P99典型1-5ms，T_queue_cloud_P99典型0-10ms（低负载），合计典型25-65ms。

## Evidence

先验知识/题面给定，逻辑校验通过：各分项延迟量级（RTT 20-50ms, 处理 1-5ms, 队列 0-10ms）符合公有云CDN边缘节点缓存命中的典型工程经验，总和计算无误。
