# N201: 在 LFU 策略下，缓存保留集合的边界由频率阈值 f_th 决定，其数值为 f_th = R_total / (N * C_norm)，即 50,000,000

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

在 LFU 策略下，缓存保留集合的边界由频率阈值 f_th 决定，其数值为 f_th = R_total / (N * C_norm)，即 50,000,000 / (100,000 * 0.119) ≈ 4201.7 次/天，该值代表 LFU 能保留对象的最低访问频率。

## Corrected Claim

在 LFU 策略下，缓存保留集合的边界由频率阈值 f_th 决定，其数值为 f_th = R_total / (N * C_norm)，即 50,000,000 / (100,000 * 0.119) ≈ 4201.7 次/天，该值代表 LFU 能保留对象的最低访问频率。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 50,000,000 / (100,000 * 0.119) ≈ 4201.68 与陈述一致，量纲（次/天）合理，符合 LFU 频率阈值定义。
