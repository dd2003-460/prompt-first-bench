# N53: 三种计费模式的成本比较需引入利用率因子 U_util = B_avg / B_peak，其中 B_avg 为月度平均带宽；按量计费成本 C_volume = B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13, N14, N15

## Claim

三种计费模式的成本比较需引入利用率因子 U_util = B_avg / B_peak，其中 B_avg 为月度平均带宽；按量计费成本 C_volume = B_avg * P_per_GB，包月成本 C_monthly = B_peak * P_per_GB_monthly，95 峰值成本 C_95 = B_95 * P_per_GB_95；最优计费模式取决于 U_util 和 B_95/B_peak 比值。

## Corrected Claim

三种计费模式的成本比较需引入利用率因子 U_util = B_avg / B_peak，其中 B_avg 为月度平均带宽；按量计费成本 C_volume = B_avg * P_per_GB，包月成本 C_monthly = B_peak * P_per_GB_monthly，95 峰值成本 C_95 = B_95 * P_per_GB_95；最优计费模式取决于 U_util 和 B_95/B_peak 比值。

## Evidence

先验知识/题面给定，逻辑校验通过
