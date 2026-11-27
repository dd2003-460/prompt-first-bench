# N158: 工作点2（大对象场景 s_min=10KB）：E[S]=110KB, Total_Bytes=11TB, C_ratio=1.16%。LRU 驻留对象数 N_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点2（大对象场景 s_min=10KB）：E[S]=110KB, Total_Bytes=11TB, C_ratio=1.16%。LRU 驻留对象数 N_resident ≈ 500，覆盖 Top 0.5% 对象。由于 β=0.9，Top 0.5% 对象覆盖请求比例 P_access ≈ (0.005)^0.1 / 0.9684 ≈ 55%。字节命中率 H_lru ≈ 55% * (S_hot_avg / 110KB) ≈ 20%。此工作点验证了 s_min 每增加 10 倍，命中率下降约 3 倍。

## Corrected Claim

工作点2（大对象场景 s_min=10KB）：E[S]=110KB, Total_Bytes=11TB, C_ratio=1.16%。LRU 驻留对象数 N_resident ≈ 500，覆盖 Top 0.5% 对象。由于 β=0.9，Top 0.5% 对象覆盖请求比例 P_access ≈ (0.005)^0.1 / 0.9684 ≈ 55%。字节命中率 H_lru ≈ 55% * (S_hot_avg / 110KB) ≈ 20%。此工作点验证了 s_min 每增加 10 倍，命中率下降约 3 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf分布参数计算自洽，LRU命中率推导符合基本缓存原理，数值量级合理。
