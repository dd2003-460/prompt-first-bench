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

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node processing latency TLS HTTP parsing
