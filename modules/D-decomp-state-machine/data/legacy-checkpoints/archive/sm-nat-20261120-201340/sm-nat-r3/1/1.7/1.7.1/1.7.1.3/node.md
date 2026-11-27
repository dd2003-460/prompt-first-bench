# N114: 修正缓存覆盖率 Ratio = C / W_total_corrected，其中 W_total_corrected = N * E[S|S≤s_max] = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

修正缓存覆盖率 Ratio = C / W_total_corrected，其中 W_total_corrected = N * E[S|S≤s_max] = 10^5 * 66 KB = 6.6 GB，Ratio = 128 GB / 6.6 GB ≈ 19.4，确认缓存容量远超工作集，支持 N74 中 H_LRU_lower = 1.0 的结论，但需考虑更新损耗。

## Corrected Claim

修正缓存覆盖率 Ratio = C / W_total_corrected，其中 W_total_corrected = N * E[S|S≤s_max] = 10^5 * 66 KB = 6.6 GB，Ratio = 128 GB / 6.6 GB ≈ 19.4，确认缓存容量远超工作集，支持 N74 中 H_LRU_lower = 1.0 的结论，但需考虑更新损耗。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 10^5 * 66 KB = 6.6 GB 正确，128 GB / 6.6 GB ≈ 19.4 正确，缓存容量远大于工作集支持高命中率结论。
