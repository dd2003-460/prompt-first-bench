# N34: H_LRU 的稳态下界计算：在容量充足 (K>N) 且无更新时，LRU 稳态命中率下界为 100%；但考虑冷启动和访问间隔，H_LRU = 1 - P(miss

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

H_LRU 的稳态下界计算：在容量充足 (K>N) 且无更新时，LRU 稳态命中率下界为 100%；但考虑冷启动和访问间隔，H_LRU = 1 - P(miss)，其中 P(miss) 为对象在访问间隔内被驱逐的概率；由于 K>N，P(miss)=0（稳态），故 H_LRU = 100%，LFU 增益为 0，除非考虑更新或有限缓存。

## Corrected Claim

H_LRU 的稳态下界计算：在容量充足 (K>N) 且无更新时，LRU 稳态命中率下界为 100%；但考虑冷启动和访问间隔，H_LRU = 1 - P(miss)，其中 P(miss) 为对象在访问间隔内被驱逐的概率；由于 K>N，P(miss)=0（稳态），故 H_LRU = 100%，LFU 增益为 0，除非考虑更新或有限缓存。

## Evidence

先验知识/题面给定，逻辑校验通过：在缓存容量 K 大于对象总数 N 且无更新的情况下，LRU 算法在稳态下不会驱逐任何对象，因此命中率必然为 100%，LFU 无额外增益。

## Search Query

LRU cache hit rate steady state full capacity
