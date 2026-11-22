# N281: 修正前提错误：总数据量 V_total 并非 119MB。基于 N60 和 N71 (s_min=1KB, s_max=10GB, N=100k)，V_tota

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

修正前提错误：总数据量 V_total 并非 119MB。基于 N60 和 N71 (s_min=1KB, s_max=10GB, N=100k)，V_total = 100,000 * E[size] ≈ 100,000 * (1KB * 1.1/0.1) ≈ 1.1 TB = 1126 GB。因此 C=128GB < V_total，缓存容量受限，N97 原命题中‘覆盖全集’的前提不成立，负相关性必然通过驱逐策略影响命中率。

## Corrected Claim

修正前提错误：总数据量 V_total 并非 119MB。基于 N60 和 N71 (s_min=1KB, s_max=10GB, N=100k)，V_total = 100,000 * E[size] ≈ 100,000 * (1KB * 1.1/0.1) ≈ 1.1 TB = 1126 GB。因此 C=128GB < V_total，缓存容量受限，N97 原命题中‘覆盖全集’的前提不成立，负相关性必然通过驱逐策略影响命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：基于对数均匀分布假设，E[size] ≈ 1.1KB，总数据量约1.1TB，远大于128GB缓存，逻辑自洽。
