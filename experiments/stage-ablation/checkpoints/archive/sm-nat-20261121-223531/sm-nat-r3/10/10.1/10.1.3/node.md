# N229: 热门对象（h > 10/天）对 D 的边际贡献量化：由于 P_stale(h) ≈ 0.001 且其字节占比约 40%，该部分对 E[P_stale] 的贡献 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

热门对象（h > 10/天）对 D 的边际贡献量化：由于 P_stale(h) ≈ 0.001 且其字节占比约 40%，该部分对 E[P_stale] 的贡献 < 0.0004，可忽略，主要衰减来自中冷对象（h ∈ [0.1, 10]）。

## Corrected Claim

热门对象（h > 10/天）对 D 的边际贡献量化：由于 P_stale(h) ≈ 0.001 且其字节占比约 40%，该部分对 E[P_stale] 的贡献 < 0.0004，可忽略，主要衰减来自中冷对象（h ∈ [0.1, 10]）。

## Evidence

先验知识/题面给定，逻辑校验通过：0.001 * 0.4 = 0.0004，数学推导自洽，符合缓存热度分布规律
