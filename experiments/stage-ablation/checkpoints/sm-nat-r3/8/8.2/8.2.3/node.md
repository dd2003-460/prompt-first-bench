# N276: LRU 驱逐边界对象的驻留时间修正：对于缓存边界对象（k=N_cache-100..N_cache），W_LRU(k) ≈ 24h，该值远大于 T_window

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

LRU 驱逐边界对象的驻留时间修正：对于缓存边界对象（k=N_cache-100..N_cache），W_LRU(k) ≈ 24h，该值远大于 T_window=1h，表明边界对象易被驱逐，需引入周期性修正项以量化误差边界。

## Corrected Claim

LRU 驱逐边界对象的驻留时间修正：对于缓存边界对象（k=N_cache-100..N_cache），W_LRU(k) ≈ 24h，该值远大于 T_window=1h，表明边界对象易被驱逐，需引入周期性修正项以量化误差边界。

## Evidence

先验知识/题面给定，逻辑校验通过
