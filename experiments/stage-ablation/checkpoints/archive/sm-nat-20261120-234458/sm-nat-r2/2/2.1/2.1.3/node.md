# N35: LFU 增益上限的修正：在容量充足 (K>N) 且无更新时，LRU 和 LFU 的稳态命中率均为 100%，增益为 0；增益仅在容量受限 (K<N) 或存在更新

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LFU 增益上限的修正：在容量充足 (K>N) 且无更新时，LRU 和 LFU 的稳态命中率均为 100%，增益为 0；增益仅在容量受限 (K<N) 或存在更新时出现；对于 K=N 的情况，LFU 增益上限为 0，原 5-15% 的估计基于容量受限假设，需重新定义 K 值。

## Corrected Claim

LFU 增益上限的修正：在容量充足 (K>N) 且无更新时，LRU 和 LFU 的稳态命中率均为 100%，增益为 0；增益仅在容量受限 (K<N) 或存在更新时出现；对于 K=N 的情况，LFU 增益上限为 0，原 5-15% 的估计基于容量受限假设，需重新定义 K 值。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量 K 大于等于请求序列中不同对象总数 N 时，LRU 和 LFU 均可容纳所有对象，稳态命中率均为 100%，故增益为 0；该结论符合缓存算法基本逻辑。

## Search Query

LFU vs LRU gain full cache capacity
