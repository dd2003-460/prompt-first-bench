# N31: 负相关性对字节命中率的影响量化：在 ρ=-0.3 下，高频率对象倾向于较小尺寸，导致 LRU（按时间）可能缓存了近期访问的中频大对象，而 LFU（按频率）缓存了

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

负相关性对字节命中率的影响量化：在 ρ=-0.3 下，高频率对象倾向于较小尺寸，导致 LRU（按时间）可能缓存了近期访问的中频大对象，而 LFU（按频率）缓存了高频小对象；计算两种策略在 Top K 对象上的字节覆盖差异 ΔBytes = |Sum_{LRU} S_i F_i - Sum_{LFU} S_i F_i|。

## Corrected Claim

负相关性对字节命中率的影响量化：在 ρ=-0.3 下，高频率对象倾向于较小尺寸，导致 LRU（按时间）可能缓存了近期访问的中频大对象，而 LFU（按频率）缓存了高频小对象；计算两种策略在 Top K 对象上的字节覆盖差异 ΔBytes = |Sum_{LRU} S_i F_i - Sum_{LFU} S_i F_i|。

## Evidence

先验知识/题面给定，逻辑校验通过
