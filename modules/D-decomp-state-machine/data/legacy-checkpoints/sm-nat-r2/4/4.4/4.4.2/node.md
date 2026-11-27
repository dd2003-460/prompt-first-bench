# N75: 对于 LRU 队列尾部（k=N_cache-100..N_cache，对应缓存边界对象），由于 sum_{j>k} λ_j 趋近于最小访问速率 λ_min，W_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

对于 LRU 队列尾部（k=N_cache-100..N_cache，对应缓存边界对象），由于 sum_{j>k} λ_j 趋近于最小访问速率 λ_min，W_LRU(k) ≈ 1 / λ_min，若 λ_min 为日均 1 次请求，则 W_LRU(k) ≈ 24h，量化了缓存边界对象的高抖动风险和易被长尾驱逐的特性。

## Corrected Claim

对于 LRU 队列尾部（k=N_cache-100..N_cache，对应缓存边界对象），由于 sum_{j>k} λ_j 趋近于最小访问速率 λ_min，W_LRU(k) ≈ 1 / λ_min，若 λ_min 为日均 1 次请求，则 W_LRU(k) ≈ 24h，量化了缓存边界对象的高抖动风险和易被长尾驱逐的特性。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 驱逐时间近似为 1/访问频率，量纲与数值推导自洽
