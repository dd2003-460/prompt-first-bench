# N20: 混合策略的延迟特性：P99_hybrid = max(P99_self_core, P99_public_tail)，由于P99是全局99分位，需确保核心区域和

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

混合策略的延迟特性：P99_hybrid = max(P99_self_core, P99_public_tail)，由于P99是全局99分位，需确保核心区域和长尾区域的P99均低于T，否则整体P99由较差的一侧决定

## Corrected Claim

混合策略的延迟特性：P99_hybrid = max(P99_self_core, P99_public_tail)，由于P99是全局99分位，需确保核心区域和长尾区域的P99均低于T，否则整体P99由较差的一侧决定

## Evidence

先验知识/题面给定，逻辑校验通过：混合策略的整体延迟分布由核心与长尾两部分组成，P99作为全局分位数，确实受限于两部分中较差（较大）的那一侧，逻辑自洽。

## Search Query

hybrid CDN P99 latency max of core and tail regions
