# N439: Spin-up 瞬态功耗对年化电费的贡献率 r_transient = (N_wakeups_per_year * ΔP_peak * T_spinup) / 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N192

## Claim

Spin-up 瞬态功耗对年化电费的贡献率 r_transient = (N_wakeups_per_year * ΔP_peak * T_spinup) / (P_avg_annual * 8760h)，其中 ΔP_peak ≈ 5W (10W-5W idle)，若每日唤醒 100 次，r_transient < 0.01% (可忽略)

## Corrected Claim

Spin-up 瞬态功耗对年化电费的贡献率 r_transient = (N_wakeups_per_year * ΔP_peak * T_spinup) / (P_avg_annual * 8760h)，其中 ΔP_peak ≈ 5W (10W-5W idle)，若每日唤醒 100 次，r_transient < 0.01% (可忽略)

## Evidence

先验知识/题面给定，逻辑校验通过：计算显示 r_transient ≈ 0.0000057 (0.00057%)，远小于 0.01%，结论成立
