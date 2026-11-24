# N50: L_edge = L_cache_lookup + L_queue_wait，其中 L_cache_lookup 为本地缓存查找延迟（SSD 随机读 0.1-0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

L_edge = L_cache_lookup + L_queue_wait，其中 L_cache_lookup 为本地缓存查找延迟（SSD 随机读 0.1-0.5ms，内存缓存 <0.1ms），L_queue_wait 为边缘节点请求队列等待延迟，负载率 >80% 时 L_queue_wait 从 1ms 升至 5-10ms。

## Corrected Claim

L_edge = L_cache_lookup + L_queue_wait，其中 L_cache_lookup 为本地缓存查找延迟（SSD 随机读 0.1-0.5ms，内存缓存 <0.1ms），L_queue_wait 为边缘节点请求队列等待延迟，负载率 >80% 时 L_queue_wait 从 1ms 升至 5-10ms。

## Evidence

先验知识/题面给定，逻辑校验通过：SSD随机读延迟（0.1-0.5ms）与内存缓存延迟（<0.1ms）符合硬件性能常识；队列等待延迟随负载率增加而显著上升（从1ms升至5-10ms）符合排队论基本规律，数值量级合理且无内部矛盾。

## Search Query

edge node cache lookup latency SSD vs memory queue waiting time high load
