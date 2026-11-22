# N19: 在稳态下，LRU 缓存中对象 i 的有效驻留时间 T_eff(i) 等于其 LRU 队列位置对应的平均等待时间 W_LRU(i) 与对象更新间隔 T_updat

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

在稳态下，LRU 缓存中对象 i 的有效驻留时间 T_eff(i) 等于其 LRU 队列位置对应的平均等待时间 W_LRU(i) 与对象更新间隔 T_update 的并联（即 T_eff(i) = W_LRU(i) || T_update = (W_LRU(i) * T_update) / (W_LRU(i) + T_update)），其中 W_LRU(i) 由 LRU 队列中排在 i 之后的所有对象的请求速率之和决定。

## Corrected Claim

在稳态下，LRU 缓存中对象 i 的有效驻留时间 T_eff(i) 等于其 LRU 队列位置对应的平均等待时间 W_LRU(i) 与对象更新间隔 T_update 的并联（即 T_eff(i) = W_LRU(i) || T_update = (W_LRU(i) * T_update) / (W_LRU(i) + T_update)），其中 W_LRU(i) 由 LRU 队列中排在 i 之后的所有对象的请求速率之和决定。

## Evidence

先验知识/题面给定，逻辑校验通过
