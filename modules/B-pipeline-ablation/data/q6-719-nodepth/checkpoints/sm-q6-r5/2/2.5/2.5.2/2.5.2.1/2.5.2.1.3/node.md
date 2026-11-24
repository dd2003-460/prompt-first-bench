# N605: 单POP带宽峰值 B_pop_peak 的推导公式：B_pop_peak = (R_daily_pop * s_avg * K_peak * (1 - H_po

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N198, N199, N200

## Claim

单POP带宽峰值 B_pop_peak 的推导公式：B_pop_peak = (R_daily_pop * s_avg * K_peak * (1 - H_pop)) / T_peak_window，其中 R_daily_pop = R_daily / 10，K_peak = 3-5（引用N25），H_pop = 0.8（自建命中率），T_peak_window = 1小时，计算得 B_pop_peak ≈ 5-10 Gbps。

## Corrected Claim

单POP带宽峰值 B_pop_peak 的推导公式：B_pop_peak = (R_daily_pop * s_avg * K_peak * (1 - H_pop)) / T_peak_window，其中 R_daily_pop = R_daily / 10，K_peak = 3-5（引用N25），H_pop = 0.8（自建命中率），T_peak_window = 1小时，计算得 B_pop_peak ≈ 5-10 Gbps。

## Evidence

先验知识/题面给定，逻辑校验通过
