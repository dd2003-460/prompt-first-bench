# N157: 工作点1（基准场景 s_min=1KB）：E[S]=11KB, Total_Bytes=1.1TB, C_ratio=11.6%。LRU 驻留对象数 N_res

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点1（基准场景 s_min=1KB）：E[S]=11KB, Total_Bytes=1.1TB, C_ratio=11.6%。LRU 驻留对象数 N_resident ≈ 5000（基于 N34 修正），覆盖 Top 5% 对象，请求覆盖率 P_access ≈ 75%（基于 N29 修正，因 β=0.9 时 Top 5% 覆盖约 75%），字节命中率 H_lru ≈ 75% * (S_hot_avg / 11KB) ≈ 60%。

## Corrected Claim

工作点1（基准场景 s_min=1KB）：E[S]=11KB, Total_Bytes=1.1TB, C_ratio=11.6%。LRU 驻留对象数 N_resident ≈ 5000（基于 N34 修正），覆盖 Top 5% 对象，请求覆盖率 P_access ≈ 75%（基于 N29 修正，因 β=0.9 时 Top 5% 覆盖约 75%），字节命中率 H_lru ≈ 75% * (S_hot_avg / 11KB) ≈ 60%。

## Evidence

先验知识/题面给定，逻辑校验通过
