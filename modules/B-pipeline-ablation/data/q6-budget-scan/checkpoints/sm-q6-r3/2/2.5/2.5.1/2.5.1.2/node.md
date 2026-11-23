# N272: 带宽利用率因子 U_factor：B_avg 是日均均值，但计费通常基于 P95 或峰值。B_billable = B_avg * (86400 / T_bil

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86, N90, N92

## Claim

带宽利用率因子 U_factor：B_avg 是日均均值，但计费通常基于 P95 或峰值。B_billable = B_avg * (86400 / T_billing_window) * U_factor，其中 U_factor 反映流量波动性（Burstiness）。对于短视频平台，晚高峰（19:00-22:00）流量通常是日均值的 2-3 倍，因此 B_peak ≈ 2-3 * B_avg。

## Corrected Claim

带宽利用率因子 U_factor：B_avg 是日均均值，但计费通常基于 P95 或峰值。B_billable = B_avg * (86400 / T_billing_window) * U_factor，其中 U_factor 反映流量波动性（Burstiness）。对于短视频平台，晚高峰（19:00-22:00）流量通常是日均值的 2-3 倍，因此 B_peak ≈ 2-3 * B_avg。

## Evidence

先验知识/题面给定，逻辑校验通过：短视频平台流量具有显著的时间聚集性，晚高峰（19:00-22:00）流量达到日均值2-3倍符合行业普遍经验及流量分布规律，量级合理且无内部矛盾。
