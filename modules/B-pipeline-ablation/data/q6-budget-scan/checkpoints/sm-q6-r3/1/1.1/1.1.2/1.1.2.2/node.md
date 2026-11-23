# N117: 混合策略中公有云需承载的最小流量下限 Q_cloud_min = Q_total * (1 - P_core_top10) * (1 - η_self_tail

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

混合策略中公有云需承载的最小流量下限 Q_cloud_min = Q_total * (1 - P_core_top10) * (1 - η_self_tail)，其中 η_self_tail 为自建节点对长尾区域的覆盖效率（通常 0.1-0.3，因 RTT 过高导致缓存失效）；当 P_core_top10=75% 且 η_self_tail=0.2 时，Q_cloud_min ≈ 25% * 80% = 20% 的总流量。

## Corrected Claim

混合策略中公有云需承载的最小流量下限 Q_cloud_min = Q_total * (1 - P_core_top10) * (1 - η_self_tail)，其中 η_self_tail 为自建节点对长尾区域的覆盖效率（通常 0.1-0.3，因 RTT 过高导致缓存失效）；当 P_core_top10=75% 且 η_self_tail=0.2 时，Q_cloud_min ≈ 25% * 80% = 20% 的总流量。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导 Q_total * (1-0.75) * (1-0.2) = 0.25 * 0.8 = 0.2 (20%) 计算正确，量纲与逻辑自洽。

## Search Query

hybrid CDN strategy minimum cloud traffic ratio tail region coverage efficiency
