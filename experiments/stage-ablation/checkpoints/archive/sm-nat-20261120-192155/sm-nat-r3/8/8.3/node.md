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

父节点级核验通过：正交+完备+无冗余（三个子节点分别从'主要损失来源（中尾部）'、'边界条件验证（头部）'和'整体加权耦合效应（全局）'三个正交维度对父节点公式进行了分解。它们分别对应了积分域的不同部分（i=k附近 vs i=1）以及最终的聚合逻辑，逻辑上互补且无重复。）

## Search Query

cache hit rate degradation due to object updates LRU
