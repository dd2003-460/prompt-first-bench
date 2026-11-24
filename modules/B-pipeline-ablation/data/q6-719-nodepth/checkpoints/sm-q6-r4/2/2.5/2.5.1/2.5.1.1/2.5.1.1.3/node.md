# N596: T_img_cost_sensitive（高成本低性工作点）：设定 P99 图片延迟阈值为 200ms，基于 LCP < 2.5s 的宽松解释，允许更稀疏的 P

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N195, N196, N197

## Claim

T_img_cost_sensitive（高成本低性工作点）：设定 P99 图片延迟阈值为 200ms，基于 LCP < 2.5s 的宽松解释，允许更稀疏的 POP 部署或更低的缓存命中率（H<80%），以显著降低带宽和基础设施成本，适用于对延迟不极度敏感的长尾流量。

## Corrected Claim

T_img_cost_sensitive（高成本低性工作点）：设定 P99 图片延迟阈值为 200ms，基于 LCP < 2.5s 的宽松解释，允许更稀疏的 POP 部署或更低的缓存命中率（H<80%），以显著降低带宽和基础设施成本，适用于对延迟不极度敏感的长尾流量。

## Evidence

先验知识/题面给定，逻辑校验通过：P99 200ms 与 LCP 2.5s 在技术上是兼容的（LCP 包含网络延迟+渲染时间，200ms 网络延迟留有充足余量）；降低缓存命中率（H<80%）确实会增加回源带宽成本但降低存储/计算基础设施成本，符合‘高成本低性工作点’中通过牺牲部分性能指标（如更稀疏部署）来优化整体成本结构的工程权衡逻辑。

## Search Query

CDN cost optimization P99 latency 200ms trade-off sparse POP deployment
