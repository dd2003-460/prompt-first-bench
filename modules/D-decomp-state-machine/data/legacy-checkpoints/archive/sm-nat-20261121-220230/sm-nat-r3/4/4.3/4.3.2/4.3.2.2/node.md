# N202: 在 LRU 策略下，缓存保留集合的边界由时间窗口 T_window 决定，其数值近似为 T_window ≈ C_norm * N / λ_avg = 0.11

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

在 LRU 策略下，缓存保留集合的边界由时间窗口 T_window 决定，其数值近似为 T_window ≈ C_norm * N / λ_avg = 0.119 * 100,000 / 500 = 23.8 天，该值代表 LRU 能保留对象的平均驻留时间上限。

## Corrected Claim

在 LRU 策略下，缓存保留集合的边界由时间窗口 T_window 决定，其数值近似为 T_window ≈ C_norm * N / λ_avg = 0.119 * 100,000 / 500 = 23.8 天，该值代表 LRU 能保留对象的平均驻留时间上限。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 缓存中对象平均驻留时间近似等于缓存容量除以平均到达率（Little's Law 变体），数值计算 0.119 * 100,000 / 500 = 23.8 正确，量纲合理。
