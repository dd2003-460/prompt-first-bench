# N119: 公有云CDN边缘节点的处理时间 T_proc_edge P99，主要包含 TLS 握手开销（若未复用连接）和 HTTP 响应头生成，典型值为 1-5ms，取决于

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

公有云CDN边缘节点的处理时间 T_proc_edge P99，主要包含 TLS 握手开销（若未复用连接）和 HTTP 响应头生成，典型值为 1-5ms，取决于节点 CPU 负载和并发连接数。

## Corrected Claim

公有云CDN边缘节点的处理时间 T_proc_edge P99，主要包含 TLS 握手开销（若未复用连接）和 HTTP 响应头生成，典型值为 1-5ms，取决于节点 CPU 负载和并发连接数。

## Evidence

父节点级核验未通过：不完备（子节点在功能模块上是正交的（TLS、CPU/内存查找、磁盘I/O），但存在严重的逻辑矛盾和完备性缺失。1. 矛盾：父节点定义典型值为 1-5ms，但子节点1指出未复用连接时TLS开销为 10-30ms，这直接导致 T_proc_edge 远超父节点定义的上限，父子节点数值逻辑不自洽。2. 不完备：父节点明确提到'取决于节点CPU负载'，但子节点仅提到了'并发连接数'导致的上下文切换，未涵盖CPU计算密集型任务（如动态内容生成、复杂正则匹配、加密解密计算）对 P99 的影响，导致对 CPU 负载这一关键因子的覆盖不全。）

## Search Query

CDN edge node processing time P99 latency benchmark
