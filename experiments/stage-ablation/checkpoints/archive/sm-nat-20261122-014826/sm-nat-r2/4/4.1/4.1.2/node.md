# N46: Stale Fraction P_stale 的边界条件修正：当更新率 u 与驻留时间 T_avg_residency 的乘积 u*T_avg_residenc

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Stale Fraction P_stale 的边界条件修正：当更新率 u 与驻留时间 T_avg_residency 的乘积 u*T_avg_residency < 0.1 时，P_stale ≈ u * T_avg_residency（线性近似）；在 u=0.01/天 和 T_avg_residency=1 小时（1/24 天）时，u*T_avg_residency = 0.0004，P_stale ≈ 0.04%，远低于 0.5%-1.5% 的估算值，表明在短驻留时间下缓存污染比例极低。

## Corrected Claim

Stale Fraction P_stale 的边界条件修正：当更新率 u 与驻留时间 T_avg_residency 的乘积 u*T_avg_residency < 0.1 时，P_stale ≈ u * T_avg_residency（线性近似）；在 u=0.01/天 和 T_avg_residency=1 小时（1/24 天）时，u*T_avg_residency = 0.0004，P_stale ≈ 0.04%，远低于 0.5%-1.5% 的估算值，表明在短驻留时间下缓存污染比例极低。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.01 * (1/24) ≈ 0.000417 正确，线性近似条件 u*T < 0.1 满足，结论符合缓存理论直觉。
