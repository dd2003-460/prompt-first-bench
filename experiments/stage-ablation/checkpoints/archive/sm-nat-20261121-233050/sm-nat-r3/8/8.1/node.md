# N64: LRU缓存中对象i的平均驻留时间 T_res_i 的解析下界公式：T_res_i ≈ 1 / (λ_i + λ_evict_i)，其中 λ_i 是对象i的访问到

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LRU缓存中对象i的平均驻留时间 T_res_i 的解析下界公式：T_res_i ≈ 1 / (λ_i + λ_evict_i)，其中 λ_i 是对象i的访问到达率（次/秒），λ_evict_i 是由其他对象访问引起的驱逐速率，需通过缓存占用比例和竞争对象的频率分布计算。

## Corrected Claim

LRU缓存中对象i的平均驻留时间 T_res_i 的解析下界公式：T_res_i ≈ 1 / (λ_i + λ_evict_i)，其中 λ_i 是对象i的访问到达率（次/秒），λ_evict_i 是由其他对象访问引起的驱逐速率，需通过缓存占用比例和竞争对象的频率分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过
