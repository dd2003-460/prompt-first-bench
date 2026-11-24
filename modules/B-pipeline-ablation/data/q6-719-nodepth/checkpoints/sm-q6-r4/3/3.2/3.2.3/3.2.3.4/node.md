# N230: 自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbps) = 3.5%；极低利用率导致固定成本分摊后单位成本高昂，需提高缓存命中率 H 或增加 POP 数量以降低单位带宽成本，或转向公有云 CDN 以利用其规模效应。

## Corrected Claim

自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbps) = 3.5%；极低利用率导致固定成本分摊后单位成本高昂，需提高缓存命中率 H 或增加 POP 数量以降低单位带宽成本，或转向公有云 CDN 以利用其规模效应。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别从静态经济临界点、架构混合策略优化、以及时间维度敏感性三个正交维度深入分析了父节点提出的带宽利用率低及成本高昂问题，覆盖了主要优化路径且无逻辑矛盾或重复。）
