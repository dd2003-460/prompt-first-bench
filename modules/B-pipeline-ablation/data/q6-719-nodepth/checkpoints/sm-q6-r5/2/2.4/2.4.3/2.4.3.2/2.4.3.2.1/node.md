# N585: 工作点 A（高吞吐/低延迟优化）：通过启用 HTTP/2 多路复用及内核级 TCP 优化，将单核平均服务时间 E[S] 压缩至 0.5 ms（含内存缓存命中路径

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N192

## Claim

工作点 A（高吞吐/低延迟优化）：通过启用 HTTP/2 多路复用及内核级 TCP 优化，将单核平均服务时间 E[S] 压缩至 0.5 ms（含内存缓存命中路径），此时单核服务率 μ_core = 1 / 0.0005s = 2,000 req/s，16 核节点总服务率 μ_node = 32,000 req/s。

## Corrected Claim

工作点 A（高吞吐/低延迟优化）：通过启用 HTTP/2 多路复用及内核级 TCP 优化，将单核平均服务时间 E[S] 压缩至 0.5 ms（含内存缓存命中路径），此时单核服务率 μ_core = 1 / 0.0005s = 2,000 req/s，16 核节点总服务率 μ_node = 32,000 req/s。

## Evidence

先验知识/题面给定，逻辑校验通过：1/0.0005s=2000 req/s，2000*16=32000 req/s，数值量级与计算均正确。

## Search Query

HTTP/2 multiplexing impact on per-request processing time server side
