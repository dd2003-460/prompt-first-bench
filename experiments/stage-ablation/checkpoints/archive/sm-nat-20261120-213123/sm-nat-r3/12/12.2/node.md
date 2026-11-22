# N185: LRU 驱逐的‘高频头部’对象集合定义为：热度排名在 [1, k_hot] 之间，但因 LRU 的时间局部性偏差（如突发流量干扰）而在稳态下未驻留的对象。该集合

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

LRU 驱逐的‘高频头部’对象集合定义为：热度排名在 [1, k_hot] 之间，但因 LRU 的时间局部性偏差（如突发流量干扰）而在稳态下未驻留的对象。该集合的字节流量占比 P_byte_lost = Σ_{i=1}^{k_hot} λ_i * S_i * P_evict(i) / R_byte，其中 P_evict(i) 为对象 i 在 LRU 下被驱逐的概率，需结合 T_LRU 和对象访问间隔分布计算。

## Corrected Claim

LRU 驱逐的‘高频头部’对象集合定义为：热度排名在 [1, k_hot] 之间，但因 LRU 的时间局部性偏差（如突发流量干扰）而在稳态下未驻留的对象。该集合的字节流量占比 P_byte_lost = Σ_{i=1}^{k_hot} λ_i * S_i * P_evict(i) / R_byte，其中 P_evict(i) 为对象 i 在 LRU 下被驱逐的概率，需结合 T_LRU 和对象访问间隔分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过
