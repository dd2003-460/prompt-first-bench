# N41: 修正后的 K 应为 min(K_capacity, N_total)。由于 N_total=10^5 < K_capacity≈3.5×10^6，缓存容量足以容

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

修正后的 K 应为 min(K_capacity, N_total)。由于 N_total=10^5 < K_capacity≈3.5×10^6，缓存容量足以容纳所有 10 万个对象（若平均大小允许），此时理论最大请求命中率为 100%，但字节命中率受限于大对象的缓存覆盖。

## Corrected Claim

修正后的 K 应为 min(K_capacity, N_total)。由于 N_total=10^5 < K_capacity≈3.5×10^6，缓存容量足以容纳所有 10 万个对象（若平均大小允许），此时理论最大请求命中率为 100%，但字节命中率受限于大对象的缓存覆盖。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存容量大于总对象数时，对象级命中率可达100%是缓存理论的基本推论，且数值量级（10^5 < 3.5×10^6）合理。
