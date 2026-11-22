# N184: LRU 错误缓存的‘中等热度’对象集合定义为：热度排名在 [k_hot, k_cold] 之间的对象，其中 k_hot 为 LFU 策略下保留的头部对象数（由频

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

LRU 错误缓存的‘中等热度’对象集合定义为：热度排名在 [k_hot, k_cold] 之间的对象，其中 k_hot 为 LFU 策略下保留的头部对象数（由频率阈值决定），k_cold 为 LRU 策略下因近期访问而驻留的尾部对象数。该集合的字节流量占比 P_byte_mid = Σ_{i=k_hot}^{k_cold} λ_i * S_i / R_byte。

## Corrected Claim

LRU 错误缓存的‘中等热度’对象集合定义为：热度排名在 [k_hot, k_cold] 之间的对象，其中 k_hot 为 LFU 策略下保留的头部对象数（由频率阈值决定），k_cold 为 LRU 策略下因近期访问而驻留的尾部对象数。该集合的字节流量占比 P_byte_mid = Σ_{i=k_hot}^{k_cold} λ_i * S_i / R_byte。

## Evidence

先验知识/题面给定，逻辑校验通过
