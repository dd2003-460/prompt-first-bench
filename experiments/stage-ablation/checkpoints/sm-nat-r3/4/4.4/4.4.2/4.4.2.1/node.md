# N213: LRU 队列尾部对象（k=N_cache-100..N_cache）的驻留时间 W_LRU_tail = 1 / λ_min，其中 λ_min 为最小访问速率；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

LRU 队列尾部对象（k=N_cache-100..N_cache）的驻留时间 W_LRU_tail = 1 / λ_min，其中 λ_min 为最小访问速率；若 λ_min = 1 次/天，则 W_LRU_tail = 24h；若 λ_min = 0.1 次/天，则 W_LRU_tail = 240h。

## Corrected Claim

LRU 队列尾部对象（k=N_cache-100..N_cache）的驻留时间 W_LRU_tail = 1 / λ_min，其中 λ_min 为最小访问速率；若 λ_min = 1 次/天，则 W_LRU_tail = 24h；若 λ_min = 0.1 次/天，则 W_LRU_tail = 240h。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU尾部对象驻留时间由最小访问速率决定，W=1/λ_min，数值换算正确（1次/天=24h，0.1次/天=240h）
