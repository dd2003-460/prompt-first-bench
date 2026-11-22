# N9: LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Paret

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Pareto(β=0.9) 下，LFU 对头部 10% 对象（占 90% 请求）的缓存保留率更高，增益上限 ≈ 5-15 个百分点 [待核验]

## Corrected Claim

LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Pareto(β=0.9) 下，LFU 对头部 10% 对象（占 90% 请求）的缓存保留率更高，增益上限 ≈ 5-15 个百分点 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU hit rate Pareto distribution edge case
