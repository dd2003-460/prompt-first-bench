# N83: 月总流量 V_total 的精确计算需考虑缓存命中率 H_cache，实际出网流量 V_out = V_total * (1 - H_cache) + V_to

- **status**: pending
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

父节点级核验未通过：不完备（子节点分别描述了公有云CDN和自建节点两种不同场景下的计费逻辑，彼此正交且无冗余。但父节点的核心在于'精确计算需考虑缓存命中率'以及'实际成本应基于回源流量计算（除非计费规则明确包含命中流量）'，而子节点仅解释了两种特定场景下的计费口径，未覆盖'回源流量V_origin'作为通用成本计算基础这一关键逻辑，也未提及'计费规则是否包含命中流量'这一条件分支，因此不完备。）

## Search Query

CDN billing model cache hit vs miss traffic cost calculation
