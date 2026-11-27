# N79: Pareto 参数 β=0.9 对应于 2000 年代 Web 服务器日志的请求热度分布，现代边缘节点的请求热度分布更平坦（β=1.0-1.2），这会导致头部对

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

Pareto 参数 β=0.9 对应于 2000 年代 Web 服务器日志的请求热度分布，现代边缘节点的请求热度分布更平坦（β=1.0-1.2），这会导致头部对象命中率降低，整体 LRU 命中率下降约 2-5%。

## Corrected Claim

Pareto 参数 β 的增大通常意味着请求热度分布更平坦，这可能导致头部对象命中率降低，进而影响整体 LRU 命中率，但具体数值需依赖实测数据。

## Evidence

[质询]该陈述包含具体的经验性数值（β值范围、命中率下降幅度2-5%），属于硬件/系统性能经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

edge CDN request popularity distribution Zipf beta 2024
