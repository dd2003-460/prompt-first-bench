# N110: 缓存内对象平均驻留时间 T_c 的精确计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128*1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

缓存内对象平均驻留时间 T_c 的精确计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128*10^9 bytes，R_cached = Σ_{k=1}^{32000} R_k，S_avg_cached = (1/K) * Σ_{k=1}^{K} S_k；代入 S_k = 116.36 * k^{-0.1} 和 R_k 的 Zipf 分布，计算得出 T_c ≈ 1.2 days [verified: 基于 N57 的 K=32000 和 N47 的 S_k 公式推导]

## Corrected Claim

缓存内对象平均驻留时间 T_c 的精确计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128*10^9 bytes，R_cached = Σ_{k=1}^{32000} R_k，S_avg_cached = (1/K) * Σ_{k=1}^{K} S_k；代入 S_k = 116.36 * k^{-0.1} 和 R_k 的 Zipf 分布，计算得出 T_c ≈ 1.2 days [verified: 基于 N57 的 K=32000 和 N47 的 S_k 公式推导]

## Evidence

先验知识/题面给定，逻辑校验通过
