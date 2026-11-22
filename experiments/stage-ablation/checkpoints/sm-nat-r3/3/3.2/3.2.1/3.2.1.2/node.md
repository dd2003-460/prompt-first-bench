# N179: 在 LRU 策略下，保留对象集合 S_LRU 的字节加权未命中损失项 L_LRU = Σ_{i∉S_LRU} p_i s_i 的计算，需基于最近访问时间窗口 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

在 LRU 策略下，保留对象集合 S_LRU 的字节加权未命中损失项 L_LRU = Σ_{i∉S_LRU} p_i s_i 的计算，需基于最近访问时间窗口 T_window 确定 S_LRU 边界，并量化因长尾突发访问导致的头部对象误驱逐比例。

## Corrected Claim

在 LRU 策略下，保留对象集合 S_LRU 的字节加权未命中损失项 L_LRU = Σ_{i∉S_LRU} p_i s_i 的计算，需基于最近访问时间窗口 T_window 确定 S_LRU 边界，并量化因长尾突发访问导致的头部对象误驱逐比例。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU策略确实基于最近访问时间窗口确定保留集合，且长尾突发访问确实会导致头部对象被误驱逐，公式定义符合缓存替换策略的基本原理。
