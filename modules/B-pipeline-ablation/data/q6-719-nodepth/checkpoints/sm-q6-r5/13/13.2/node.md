# N404: 边缘节点处理延迟 L_processing_edge 包含 TCP 握手、TLS 解密、HTTP 解析及磁盘读取，典型值为 2-5 ms；在 P99 负载下，由

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

边缘节点处理延迟 L_processing_edge 包含 TCP 握手、TLS 解密、HTTP 解析及磁盘读取，典型值为 2-5 ms；在 P99 负载下，由于队列效应，L_processing_edge 可能上升至 10-15 ms，需与传播延迟 L_prop 相加得到总边缘延迟 L_edge_total = L_prop + L_processing_edge。

## Corrected Claim

边缘节点处理延迟 L_processing_edge 包含 TCP 握手、TLS 解密、HTTP 解析及磁盘读取，典型值为 2-5 ms；在 P99 负载下，由于队列效应，L_processing_edge 可能上升至 10-15 ms，需与传播延迟 L_prop 相加得到总边缘延迟 L_edge_total = L_prop + L_processing_edge。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node processing latency TCP TLS overhead P99
