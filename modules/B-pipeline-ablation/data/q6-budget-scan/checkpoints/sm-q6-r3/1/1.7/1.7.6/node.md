# N41: 节点处理延迟 T_proc 包括TLS握手、HTTP解析、缓存查找及数据包组装，对于缓存命中请求通常为 1-5ms；对于缓存未命中请求，由于需等待回源数据流，T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

节点处理延迟 T_proc 包括TLS握手、HTTP解析、缓存查找及数据包组装，对于缓存命中请求通常为 1-5ms；对于缓存未命中请求，由于需等待回源数据流，T_proc 可忽略不计（被回源延迟掩盖）。

## Corrected Claim

节点处理延迟 T_proc 包括TLS握手、HTTP解析、缓存查找及数据包组装，对于缓存命中请求通常为 1-5ms；对于缓存未命中请求，由于需等待回源数据流，T_proc 可忽略不计（被回源延迟掩盖）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点准确分解了父节点定义的三个核心组件（TLS、解析/缓存、组装/发送），彼此之间无逻辑重叠且无矛盾。虽然父节点指出缓存未命中时 T_proc 可忽略，但子节点详细列出各组件延迟是合理的，因为这是构成 T_proc 的基础参数，且父节点已说明了在特定场景下的宏观表现，子节点提供的是微观构成，二者互补而非冲突。）

## Search Query

CDN edge node processing latency TLS HTTP parsing
