# N220: 在 128GB 缓存中，若 E[S] 修正为 1.03 KB (N104)，则可缓存对象数 N_cache = 128 * 1024^3 / (1.03 * 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

在 128GB 缓存中，若 E[S] 修正为 1.03 KB (N104)，则可缓存对象数 N_cache = 128 * 1024^3 / (1.03 * 1024^2) ≈ 128,155 个对象，由于 N_cache > 100,000 (总对象数)，缓存覆盖率 Coverage = min(1, N_cache / 100,000) = 1.0，确认全量缓存状态。

## Corrected Claim

在 128GB 缓存中，若 E[S] 修正为 1.03 KB (N104)，则可缓存对象数 N_cache = 128 * 1024^3 / (1.03 * 1024^2) ≈ 128,155 个对象，由于 N_cache > 100,000 (总对象数)，缓存覆盖率 Coverage = min(1, N_cache / 100,000) = 1.0，确认全量缓存状态。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB / 1.03KB ≈ 128,155，大于100,000，覆盖率计算正确
