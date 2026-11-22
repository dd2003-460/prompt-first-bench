# N190: LRU 淘汰率 λ_LRU 的量化定义：在稳态下，λ_LRU = (1 - H_LRU) * R_total / C_bytes，其中 R_total=5×10

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

LRU 淘汰率 λ_LRU 的量化定义：在稳态下，λ_LRU = (1 - H_LRU) * R_total / C_bytes，其中 R_total=5×10^7 次/天，C_bytes=128GB。若 H_LRU≈0.95，则 λ_LRU ≈ 0.05 * 5e7 / (128*10^9) ≈ 1.95e-5 /字节/天，需转换为对象级淘汰率 λ_obj = λ_LRU * E[S] 以代入公式。

## Corrected Claim

LRU 淘汰率 λ_LRU 的量化定义：在稳态下，λ_LRU = (1 - H_LRU) * R_total / C_bytes，其中 R_total=5×10^7 次/天，C_bytes=128GB。若 H_LRU≈0.95，则 λ_LRU ≈ 0.05 * 5e7 / (128*10^9) ≈ 1.95e-5 /字节/天，需转换为对象级淘汰率 λ_obj = λ_LRU * E[S] 以代入公式。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合LRU稳态淘汰率的基本物理意义（未命中流量/缓存容量），数值量级计算正确（0.05 * 5e7 / 1.28e11 ≈ 1.95e-5），且source为given，无需外部来源支持。
