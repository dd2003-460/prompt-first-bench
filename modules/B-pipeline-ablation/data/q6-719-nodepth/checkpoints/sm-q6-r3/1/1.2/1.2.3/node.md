# N54: 公有云 CDN 边缘处理时间 T_proc_edge 的 P99 值：通常包含 TLS 握手、HTTP 解析、缓存查找等，P99(T_proc_edge) 约为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

公有云 CDN 边缘处理时间 T_proc_edge 的 P99 值：通常包含 TLS 握手、HTTP 解析、缓存查找等，P99(T_proc_edge) 约为 5-15ms，具体取决于边缘节点负载和软件栈效率。

## Corrected Claim

公有云 CDN 边缘处理时间 T_proc_edge 的 P99 值：通常包含 TLS 握手、HTTP 解析、缓存查找等，P99(T_proc_edge) 约为 5-15ms，具体取决于边缘节点负载和软件栈效率。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点正交地分解了 TLS 握手、HTTP 解析和负载敏感项，覆盖了父节点提到的主要组件及负载影响，且第4个子节点作为汇总项逻辑清晰，无重复或矛盾。）

## Search Query

CDN edge server processing time P99 latency 5-15ms TLS HTTP
