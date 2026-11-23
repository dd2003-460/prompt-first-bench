# N169: 自建策略的 P99(t_cache | self) 由边缘节点本地延迟决定：t_cache_self = t_disk_read + t_processing 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

自建策略的 P99(t_cache | self) 由边缘节点本地延迟决定：t_cache_self = t_disk_read + t_processing + t_network_local，其中 t_disk_read ≈ 0.1-1ms（NVMe），t_processing ≈ 0.5-2ms，t_network_local ≈ 0.1-0.5ms（机房内），总计 P99 < 5ms

## Corrected Claim

自建策略的 P99(t_cache | self) 由边缘节点本地延迟决定：t_cache_self = t_disk_read + t_processing + t_network_local，其中 t_disk_read ≈ 0.1-1ms（NVMe），t_processing ≈ 0.5-2ms，t_network_local ≈ 0.1-0.5ms（机房内），总计 P99 < 5ms

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe随机读延迟（~0.1-1ms）、CPU处理延迟（~0.5-2ms）及机房内网络延迟（~0.1-0.5ms）的量级符合工程常识，总和P99<5ms在逻辑上自洽且合理。

## Search Query

edge node local cache latency NVMe SSD read time
