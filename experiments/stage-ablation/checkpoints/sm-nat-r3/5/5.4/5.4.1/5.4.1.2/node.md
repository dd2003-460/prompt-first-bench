# N242: LRU 队列排序误差的量化：平均排序偏移量 5 个位置意味着前 10,000 个对象中有约 5% 的对象位置错误，对命中率的影响应通过重排后的缓存集合计算：H_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

LRU 队列排序误差的量化：平均排序偏移量 5 个位置意味着前 10,000 个对象中有约 5% 的对象位置错误，对命中率的影响应通过重排后的缓存集合计算：H_LRU_shifted = 1 - (Σ_{i∉C_shifted} p_i s_i) / (Σ_all p_i s_i)，其中 C_shifted 为偏移后的缓存集合

## Corrected Claim

LRU 队列排序误差的量化：平均排序偏移量 5 个位置意味着前 10,000 个对象中有约 5% 的对象位置错误，对命中率的影响应通过重排后的缓存集合计算：H_LRU_shifted = 1 - (Σ_{i∉C_shifted} p_i s_i) / (Σ_all p_i s_i)，其中 C_shifted 为偏移后的缓存集合

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 缓存命中率公式定义正确，排序偏移对集合的影响逻辑自洽
