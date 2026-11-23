# N25: 缓存命中率差异 ΔH = H_edge - H_origin；命中率每提升 1%，P99 延迟降低约 5-10ms，带宽成本降低约 1%

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

缓存命中率差异 ΔH = H_edge - H_origin；命中率每提升 1%，P99 延迟降低约 5-10ms，带宽成本降低约 1%

## Corrected Claim

缓存命中率差异 ΔH = H_edge - H_origin；命中率提升通常能显著降低P99延迟和带宽成本，具体数值取决于业务场景（如对象大小、网络条件），一般经验上每提升1%命中率，P99延迟降低数毫秒至数十毫秒，带宽成本降低约1%。

## Evidence

[质询]数值量级缺乏普适性：P99延迟降低5-10ms与带宽成本降低1%是高度依赖具体业务场景（如对象大小、网络RTT、缓存策略）的经验估算值，并非物理定律或通用工程常数，存在将特定案例数据泛化为普遍规律的风险。 | source=knowledge，逻辑自洽（命中率提升确实降低回源延迟和带宽），但具体数值（5-10ms, 1%）属于经验事实，无外部来源支持且无法从第一性原理严格推导，故降级。

## Search Query

CDN cache hit rate impact on latency and cost
