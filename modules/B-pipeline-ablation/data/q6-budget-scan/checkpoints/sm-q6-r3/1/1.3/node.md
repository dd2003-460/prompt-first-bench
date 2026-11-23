# N9: 缓存命中路径的P99延迟：T_cache_hit_P99 = RTT_P99 + T_processing_P99 + T_queue_P99，其中T_proc

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存命中路径的P99延迟：T_cache_hit_P99 = RTT_P99 + T_processing_P99 + T_queue_P99，其中T_processing为边缘节点CPU处理时间（通常<5ms），T_queue为队列等待时间（与负载相关）

## Corrected Claim

缓存命中路径的P99延迟：T_cache_hit_P99 = RTT_P99 + T_processing_P99 + T_queue_P99，其中T_processing为边缘节点CPU处理时间（通常<5ms），T_queue为队列等待时间（与负载相关）

## Evidence

父节点级核验未通过：不完备（子节点未覆盖父节点公式中的核心组成部分。父节点明确定义为 RTT + Processing + Queue，但子节点讨论的是 TLS 握手（连接建立阶段，通常不计入稳态 RTT）和 TCP 慢启动（传输阶段，未包含在父节点公式中）。缺失了对 RTT、CPU 处理和队列等待这三个关键变量的分解。）

## Search Query

CDN edge server processing latency P99
