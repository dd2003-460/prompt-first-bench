# N48: P_stale 的精确计算依赖于缓存内对象的平均驻留时间 T_avg_residency，其数值为 T_avg_residency = C / (N * P[h

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

P_stale 的精确计算依赖于缓存内对象的平均驻留时间 T_avg_residency，其数值为 T_avg_residency = C / (N * P[hit] * E[Size|hit])，代入 C=128GB, N=10^5, P[hit]≈0.3, E[Size|hit]≈0.85KB 得 T_avg_residency ≈ 1.9 小时，进而 P_stale = 1 - exp(-0.01 * 1.9/24) ≈ 0.00079 (0.079%)。

## Corrected Claim

P_stale 的精确计算依赖于缓存内对象的平均驻留时间 T_avg_residency，其数值为 T_avg_residency = C / (N * P[hit] * E[Size|hit])，代入 C=128GB, N=10^5, P[hit]≈0.3, E[Size|hit]≈0.85KB 得 T_avg_residency ≈ 1.9 小时，进而 P_stale = 1 - exp(-0.01 * 1.9/24) ≈ 0.00079 (0.079%)。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（128GB/10^5/0.3/0.85KB ≈ 1.9h，1-exp(-0.01*1.9/24) ≈ 0.00079），公式推导符合缓存驻留时间与过期概率的基本逻辑。
