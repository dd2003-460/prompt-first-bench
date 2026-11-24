# N627: 公有云 CDN 边缘节点 P99(T_proc_edge) 的 7.5ms 基准值分解：TLS 握手（若复用连接则为 0，否则 1-3ms）、HTTP/2 解析

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

公有云 CDN 边缘节点 P99(T_proc_edge) 的 7.5ms 基准值分解：TLS 握手（若复用连接则为 0，否则 1-3ms）、HTTP/2 解析与头部压缩（0.5-1ms）、本地 SSD 缓存查找（0.1-0.5ms）、内核协议栈处理（1-2ms）、应用层鉴权与限流（1-2ms），各项 P99 叠加后取 7.5ms 为保守估计。

## Corrected Claim

公有云 CDN 边缘节点 P99(T_proc_edge) 的 7.5ms 基准值分解：TLS 握手（若复用连接则为 0，否则 1-3ms）、HTTP/2 解析与头部压缩（0.5-1ms）、本地 SSD 缓存查找（0.1-0.5ms）、内核协议栈处理（1-2ms）、应用层鉴权与限流（1-2ms），各项 P99 叠加后取 7.5ms 为保守估计。

## Evidence

[质询]各项P99延迟直接相加在统计学上并不严谨（P99之和通常大于总和的P99），且具体数值（如TLS握手1-3ms）可能因网络环境和具体实现略有波动，但作为工程估算的保守上限，其量级和逻辑是合理的。 | 先验知识/题面给定，逻辑校验通过。各项组件延迟量级符合CDN边缘节点处理的一般工程经验，7.5ms作为P99保守估计在逻辑上自洽。
