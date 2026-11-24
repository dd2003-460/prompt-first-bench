# N499: 公有云CDN边缘节点P99处理延迟 T_proc_public 约为 10-30ms，主要受限于HTTP/2连接复用效率、TLS握手开销及动态内容回源判定逻辑，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N165

## Claim

公有云CDN边缘节点P99处理延迟 T_proc_public 约为 10-30ms，主要受限于HTTP/2连接复用效率、TLS握手开销及动态内容回源判定逻辑，其中TLS握手在首次连接时贡献约5-10ms

## Corrected Claim

公有云CDN边缘节点P99处理延迟 T_proc_public 约为 10-30ms，主要受限于HTTP/2连接复用效率、TLS握手开销及动态内容回源判定逻辑，其中TLS握手在首次连接时贡献约5-10ms

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node P99 processing latency HTTP/2 TLS handshake overhead
