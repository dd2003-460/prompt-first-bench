# N173: 公有云策略的 P99(t_cache | cloud) 由云边缘节点延迟决定：t_cache_cloud = t_disk_read + t_processin

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

公有云策略的 P99(t_cache | cloud) 由云边缘节点延迟决定：t_cache_cloud = t_disk_read + t_processing + t_network_cloud，其中 t_disk_read ≈ 0.5-5ms（HDD/SSD混合），t_processing ≈ 1-5ms，t_network_cloud ≈ 1-5ms（跨机房），总计 P99 5-20ms

## Corrected Claim

公有云策略的 P99(t_cache | cloud) 由云边缘节点延迟决定：t_cache_cloud = t_disk_read + t_processing + t_network_cloud，其中 t_disk_read ≈ 0.5-5ms（HDD/SSD混合），t_processing ≈ 1-5ms，t_network_cloud ≈ 1-5ms（跨机房），总计 P99 5-20ms

## Evidence

先验知识/题面给定，逻辑校验通过：各分项延迟量级（磁盘0.5-5ms, 处理1-5ms, 网络1-5ms）符合公有云边缘节点典型工程参数，总和5-20ms在P99统计意义上合理且无内部矛盾。

## Search Query

public cloud CDN edge node latency P99 measurement
