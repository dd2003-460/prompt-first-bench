# N7: 公有云 CDN（阿里云/Cloudflare）的全球 P99 延迟基准值约为 150ms（基于全球边缘节点覆盖密度及 Anycast 路由优化，假设用户均匀分布

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

公有云 CDN（阿里云/Cloudflare）的全球 P99 延迟基准值约为 150ms（基于全球边缘节点覆盖密度及 Anycast 路由优化，假设用户均匀分布或集中于一二线城市）

## Corrected Claim

公有云 CDN（阿里云/Cloudflare）的全球 P99 延迟基准值约为 150ms（基于全球边缘节点覆盖密度及 Anycast 路由优化，假设用户均匀分布或集中于一二线城市）

## Evidence

父节点级核验未通过：不完备（子节点1拆解了延迟的构成要素（物理层/网络层），子节点2提供了关键变量（缓存命中率 CHR）的基准值，两者维度不同且互补，无重复或矛盾，正交性合格。但完备性不足：父节点声称基于'全球边缘节点覆盖密度'和'用户分布假设'，然而子节点仅关注了技术延迟拆解和命中率，完全缺失了'用户地理分布'、'边缘节点拓扑/覆盖密度'以及'Anycast 路由具体开销'等对 P99 延迟有显著影响的关键前置条件或约束参数。此外，子节点1中 T_last_mile 50-80ms 的取值对于全球 P99 而言偏乐观（通常 P99 需考虑更差的长尾网络），且未说明该拆解是加权平均还是 P99 直接相加（P99 延迟通常不是各部分 P99 的简单线性相加，存在相关性），这导致逻辑上不够严谨。）

## Search Query

Alibaba Cloud CDN global P99 latency benchmark 150ms Cloudflare P99 latency report
