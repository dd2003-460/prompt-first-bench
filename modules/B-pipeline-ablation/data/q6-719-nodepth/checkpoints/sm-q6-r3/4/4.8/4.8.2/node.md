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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式（P99_tail ≈ f(d_tail, H_miss_tail)）在不同参数取值下的实例化，属于典型的参数扫描而非正交分解；此外，父节点强调'基于 N30 的计算结果'，但子节点未体现 N30 这一关键前提或约束，导致完备性不足。）

## Search Query

hybrid CDN strategy tail region P99 latency
