# N79: N22 中 LFU 的增益上限受限于缓存容量约束：在 128GB 容量下，LFU 只能保留最高频率的 K 个对象，而 LRU 可能保留更冷但更大的对象，由于热度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

N22 中 LFU 的增益上限受限于缓存容量约束：在 128GB 容量下，LFU 只能保留最高频率的 K 个对象，而 LRU 可能保留更冷但更大的对象，由于热度-大小负相关，LFU 的字节命中率增益可能低于请求命中率增益，需通过联合分布 P(R,S) 计算。

## Corrected Claim

N22 中 LFU 的增益上限受限于缓存容量约束：在 128GB 容量下，LFU 只能保留最高频率的 K 个对象，而 LRU 可能保留更冷但更大的对象，由于热度-大小负相关，LFU 的字节命中率增益可能低于请求命中率增益，需通过联合分布 P(R,S) 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU基于频率而LRU基于时间，在对象大小与热度存在负相关时，LFU保留高频小对象可能导致字节命中率增益低于请求命中率增益，需联合分布计算，逻辑自洽且符合缓存理论直觉。

## Search Query

LFU byte hit ratio gain cache capacity constraint
