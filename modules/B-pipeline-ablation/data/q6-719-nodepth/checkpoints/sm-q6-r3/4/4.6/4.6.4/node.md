# N121: 公有云CDN L2 中间层节点缓存未命中率 Miss_rate_L2，通常为 1-5%，L2 节点容量更大且更接近源站，Miss 后需回源，影响最终回源延迟。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

公有云CDN L2 中间层节点缓存未命中率 Miss_rate_L2，通常为 1-5%，L2 节点容量更大且更接近源站，Miss 后需回源，影响最终回源延迟。

## Corrected Claim

公有云CDN L2 中间层节点缓存未命中率 Miss_rate_L2，通常为 1-5%，L2 节点容量更大且更接近源站，Miss 后需回源，影响最终回源延迟。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的，分别描述了L2的硬件属性（容量）、统计特性（命中率/流量关系）和工程结果（带宽需求）。但是，父节点明确定义了核心指标为'Miss_rate_L2'，而子节点1讨论的是'容量'，子节点3讨论的是'带宽'，只有子节点2直接关联了命中率。虽然容量和带宽与命中率紧密相关，但作为对'未命中率'这一特定指标的分解，缺少对影响Miss_rate_L2的关键因素（如缓存替换策略、请求分布长尾特性、TTL设置等）的直接分解，导致对父节点核心概念的解释不够完备。）

## Search Query

CDN L2 intermediate node cache hit ratio
