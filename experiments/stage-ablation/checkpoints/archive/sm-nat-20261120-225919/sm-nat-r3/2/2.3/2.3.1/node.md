# N47: LRU 缓存中对象 i 的驻留时间 τ_res(i) 由最近一次访问间隔决定，在稳态下近似为 1/R_i（天），其中 R_i 为对象 i 的请求频率（次/天）。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

LRU 缓存中对象 i 的驻留时间 τ_res(i) 由最近一次访问间隔决定，在稳态下近似为 1/R_i（天），其中 R_i 为对象 i 的请求频率（次/天）。

## Corrected Claim

LRU 缓存中对象 i 的驻留时间 τ_res(i) 由最近一次访问间隔决定，在稳态下近似为 1/R_i（天），其中 R_i 为对象 i 的请求频率（次/天）。

## Evidence

先验知识/题面给定，逻辑校验通过：在稳态泊松到达假设下，LRU缓存中对象的驻留时间近似等于其平均请求间隔，即1/R_i，符合排队论与缓存替换算法的基本原理。
