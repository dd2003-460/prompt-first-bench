# N70: 确定最小请求频率 r_min（即排名第 N 的对象的日请求量）：R_N = Q / (N * Z_β) * N^{-β} 的逆推，或直接由 R_1 = Q / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N29

## Claim

确定最小请求频率 r_min（即排名第 N 的对象的日请求量）：R_N = Q / (N * Z_β) * N^{-β} 的逆推，或直接由 R_1 = Q / Z_β 推导。R_1 ≈ 5*10^7 / 21.62 ≈ 2.31 * 10^6 requests/day。R_N ≈ R_1 * N^{-0.9} ≈ 2.31*10^6 * (10^5)^{-0.9} ≈ 2.31*10^6 * 10^{-4.5} ≈ 0.73 requests/day。

## Corrected Claim

确定最小请求频率 r_min（即排名第 N 的对象的日请求量）：R_N = Q / (N * Z_β) * N^{-β} 的逆推，或直接由 R_1 = Q / Z_β 推导。R_1 ≈ 5*10^7 / 21.62 ≈ 2.31 * 10^6 requests/day。R_N ≈ R_1 * N^{-0.9} ≈ 2.31*10^6 * (10^5)^{-0.9} ≈ 2.31*10^6 * 10^{-4.5} ≈ 0.73 requests/day。

## Evidence

先验知识/题面给定，逻辑校验通过：R_1计算正确(5e7/21.62≈2.31e6)，R_N推导符合Zipf定律幂律关系(2.31e6 * 10^-4.5 ≈ 0.73)，数值量级合理。
