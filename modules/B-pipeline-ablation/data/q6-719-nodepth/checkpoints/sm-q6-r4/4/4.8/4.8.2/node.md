# N131: 混合策略中长尾区域（公有云 CDN）的 P99 延迟 P99_tail，基于 N30 的计算结果，通常为 50-200ms，取决于长尾区域用户到最近公有云 CD

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

混合策略中长尾区域（公有云 CDN）的 P99 延迟 P99_tail，基于 N30 的计算结果，通常为 50-200ms，取决于长尾区域用户到最近公有云 CDN 节点的距离和缓存命中率。

## Corrected Claim

混合策略中长尾区域（公有云 CDN）的 P99 延迟 P99_tail，基于 N30 的计算结果，通常为 50-200ms，取决于长尾区域用户到最近公有云 CDN 节点的距离和缓存命中率。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一数学模型（P99_tail = f(d, H_miss)）在不同参数下的具体实例，存在严重的结构性冗余；同时，父节点强调'基于N30'和'距离与命中率决定延迟'，子节点仅展示了离散工作点，未涵盖参数空间的一般性关系或边界条件（如极端距离或缓存失效情况），导致完备性不足。）

## Search Query

hybrid CDN strategy tail region P99 latency
