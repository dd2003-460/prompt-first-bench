# N55: R_back_sensitivity = dR_back / dH_effective × (dH_effective / dTTL)，其中 dH_effect

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

R_back_sensitivity = dR_back / dH_effective × (dH_effective / dTTL)，其中 dH_effective / dTTL 为 TTL 对命中率的边际影响，TTL 从 1h 增至 24h 时，H_effective 提升 5-15%，R_back 下降 5-15%；需权衡新鲜度要求与回源成本。

## Corrected Claim

R_back_sensitivity = dR_back / dH_effective × (dH_effective / dTTL)，其中 dH_effective / dTTL 为 TTL 对命中率的边际影响，TTL 从 1h 增至 24h 时，H_effective 提升 5-15%，R_back 下降 5-15%；需权衡新鲜度要求与回源成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache TTL sensitivity backhaul rate reduction freshness tradeoff CDN
