# N49: 对象更新率 U=0.01/day 导致的有效命中率折扣因子 D = 1 - E[p_evict | i∈C] * (s_i / S_total_cached)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

对象更新率 U=0.01/day 导致的有效命中率折扣因子 D = 1 - E[p_evict | i∈C] * (s_i / S_total_cached)，其中 E[p_evict | i∈C] 是缓存内对象被更新驱逐的期望概率，S_total_cached 是缓存总字节数；由于热门对象访问频率高，其 T_res_i 短，p_evict_i 高，但热门对象大小 s_i 小（负相关），需加权计算。

## Corrected Claim

对象更新率 U=0.01/day 导致的有效命中率折扣因子 D = 1 - E[p_evict | i∈C] * (s_i / S_total_cached)，其中 E[p_evict | i∈C] 是缓存内对象被更新驱逐的期望概率，S_total_cached 是缓存总字节数；由于热门对象访问频率高，其 T_res_i 短，p_evict_i 高，但热门对象大小 s_i 小（负相关），需加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache hit rate degradation due to object updates LRU
