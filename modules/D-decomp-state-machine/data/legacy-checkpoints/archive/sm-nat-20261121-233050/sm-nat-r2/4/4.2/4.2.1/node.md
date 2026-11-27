# N45: 在 M/C = 1.0 的极限工作点下，LRU 队列中所有对象的驻留时间 T_res → ∞（因为无驱逐发生），导致 T_LRU_avg 趋于无穷大。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

在 M/C = 1.0 的极限工作点下，LRU 队列中所有对象的驻留时间 T_res → ∞（因为无驱逐发生），导致 T_LRU_avg 趋于无穷大。

## Corrected Claim

在 M/C = 1.0 的极限工作点下，LRU 队列中所有对象的驻留时间 T_res → ∞（因为无驱逐发生），导致 T_LRU_avg 趋于无穷大。

## Evidence

先验知识/题面给定，逻辑校验通过：M/C=1.0 意味着缓存容量等于工作集大小，LRU 策略下无对象被驱逐，驻留时间趋于无穷大，平均驻留时间亦趋于无穷大。
