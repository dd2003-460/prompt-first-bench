# N83: 月总流量 V_total 的精确计算需考虑缓存命中率 H_cache，实际出网流量 V_out = V_total * (1 - H_cache) + V_to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

月总流量 V_total 的精确计算需考虑缓存命中率 H_cache，实际出网流量 V_out = V_total * (1 - H_cache) + V_total * H_cache * p_cache_hit，其中 p_cache_hit 为命中时的内部带宽成本系数（通常接近 0 或极低），因此按流量计费的实际成本应基于回源流量 V_origin = V_total * (1 - H_cache) 计算，而非全量 V_total，除非计费规则明确包含命中流量。

## Corrected Claim

月总流量 V_total 的精确计算需考虑缓存命中率 H_cache，实际出网流量 V_out = V_total * (1 - H_cache) + V_total * H_cache * p_cache_hit，其中 p_cache_hit 为命中时的内部带宽成本系数（通常接近 0 或极低），因此按流量计费的实际成本应基于回源流量 V_origin = V_total * (1 - H_cache) 计算，而非全量 V_total，除非计费规则明确包含命中流量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN billing model cache hit vs miss traffic cost calculation
