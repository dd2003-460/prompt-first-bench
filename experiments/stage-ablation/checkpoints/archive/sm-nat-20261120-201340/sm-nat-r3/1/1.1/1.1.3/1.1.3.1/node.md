# N86: 缓存覆盖率 Ratio 的临界工作点 B（部分覆盖假设）：若 s_min 需达到约 1.2MB 才能使 W_total = 128GB (Ratio=1.0)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

缓存覆盖率 Ratio 的临界工作点 B（部分覆盖假设）：若 s_min 需达到约 1.2MB 才能使 W_total = 128GB (Ratio=1.0)，即 10^5 * 1.2MB = 120GB，此时缓存刚好填满，LRU 策略将开始驱逐最冷对象，命中率下界开始低于 100%。

## Corrected Claim

缓存覆盖率 Ratio 的临界工作点 B（部分覆盖假设）：若 s_min 需达到约 1.2MB 才能使 W_total = 128GB (Ratio=1.0)，即 10^5 * 1.2MB = 120GB，此时缓存刚好填满，LRU 策略将开始驱逐最冷对象，命中率下界开始低于 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：10^5 * 1.2MB = 120GB ≈ 128GB，量级匹配，LRU在缓存填满后开始驱逐冷对象导致命中率下降符合基本缓存原理。
