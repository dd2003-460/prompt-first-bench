# N262: ΔH 区间上限 [2.5%] 的成因：当缓存容量 C 不足以覆盖所有热门小对象时（即 C < Σ s_i for hot objects），LRU 会因时间局部

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

ΔH 区间上限 [2.5%] 的成因：当缓存容量 C 不足以覆盖所有热门小对象时（即 C < Σ s_i for hot objects），LRU 会因时间局部性不足而驱逐部分高频小对象，而 LFU 通过频率加权能够更稳定地保留这些对象，此时 P_LRU_miss_on_hot 显著高于 P_LFU_miss_on_hot，ΔH 可达 2.5%。

## Corrected Claim

ΔH 区间上限 [2.5%] 的成因：当缓存容量 C 不足以覆盖所有热门小对象时（即 C < Σ s_i for hot objects），LRU 会因时间局部性不足而驱逐部分高频小对象，而 LFU 通过频率加权能够更稳定地保留这些对象，此时 P_LRU_miss_on_hot 显著高于 P_LFU_miss_on_hot，ΔH 可达 2.5%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU advantage LRU eviction hot small objects capacity constraint
