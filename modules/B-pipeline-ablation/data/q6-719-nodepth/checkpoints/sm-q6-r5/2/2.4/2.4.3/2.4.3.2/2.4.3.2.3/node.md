# N587: 工作点 C（保守估计/高安全边际）：在 P99 尾部负载下，考虑上下文切换及锁竞争开销，单请求服务时间 E[S] 上升至 2.0 ms，单核服务率 μ_core

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N192

## Claim

工作点 C（保守估计/高安全边际）：在 P99 尾部负载下，考虑上下文切换及锁竞争开销，单请求服务时间 E[S] 上升至 2.0 ms，单核服务率 μ_core = 500 req/s，16 核节点总服务率 μ_node = 8,000 req/s；此值用于计算最坏情况下的队列深度。

## Corrected Claim

工作点 C（保守估计/高安全边际）：在 P99 尾部负载下，考虑上下文切换及锁竞争开销，单请求服务时间 E[S] 上升至 2.0 ms，单核服务率 μ_core = 500 req/s，16 核节点总服务率 μ_node = 8,000 req/s；此值用于计算最坏情况下的队列深度。

## Evidence

先验知识/题面给定，逻辑校验通过：1/2.0ms = 500 req/s，500 * 16 = 8000 req/s，数值推导自洽且量级合理。

## Search Query

server context switching overhead high load per-request latency increase
