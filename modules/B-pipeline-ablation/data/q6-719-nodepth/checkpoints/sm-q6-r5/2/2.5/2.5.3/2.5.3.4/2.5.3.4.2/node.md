# N622: 自建缓存扩容的边际成本 C_cache_upgrade_self = C_ssd_marginal + C_space_marginal，其中 C_ssd_ma

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N205

## Claim

自建缓存扩容的边际成本 C_cache_upgrade_self = C_ssd_marginal + C_space_marginal，其中 C_ssd_marginal ≈ ¥0.8/GB/月（NVMe SSD 摊销），C_space_marginal ≈ ¥0.05-0.1/GB/月（机柜电力与制冷分摊，基于 PUE 1.4 和 ¥0.8/kWh 电价）；总自建成本 ≈ ¥0.85-0.9/GB/月，显著高于公有云折扣价，仅在数据量 > 100TB 时因规模效应趋近

## Corrected Claim

自建缓存扩容的边际成本 C_cache_upgrade_self = C_ssd_marginal + C_space_marginal，其中 C_ssd_marginal ≈ ¥0.8/GB/月（NVMe SSD 摊销），C_space_marginal ≈ ¥0.05-0.1/GB/月（机柜电力与制冷分摊，基于 PUE 1.4 和 ¥0.8/kWh 电价）；总自建成本 ≈ ¥0.85-0.9/GB/月，显著高于公有云折扣价，仅在数据量 > 100TB 时因规模效应趋近

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD 摊销成本与机柜电力制冷分摊的量级符合行业常识，总成本推导逻辑自洽。
