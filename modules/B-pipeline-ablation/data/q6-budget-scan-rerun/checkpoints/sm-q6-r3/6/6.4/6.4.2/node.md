# N363: 年总请求量的季节性波动修正：R_total_annual_seasonal = Σ_m (R_total_daily_m × days_m)，其中 m 为月份，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

年总请求量的季节性波动修正：R_total_annual_seasonal = Σ_m (R_total_daily_m × days_m)，其中 m 为月份，R_total_daily_m 随季节波动（如春节、双11 期间请求量可能激增 20-50%），若使用简单平均 365 天，会低估峰值月份的成本压力，导致 CDN 容量规划不足。

## Corrected Claim

年总请求量的季节性波动修正：R_total_annual_seasonal = Σ_m (R_total_daily_m × days_m)，其中 m 为月份，R_total_daily_m 随季节波动（如春节、双11 期间请求量可能激增 20-50%），若使用简单平均 365 天，会低估峰值月份的成本压力，导致 CDN 容量规划不足。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义正确，且基于CDN容量规划需覆盖峰值流量的工程常识，简单平均确实会低估峰值成本，逻辑自洽。
