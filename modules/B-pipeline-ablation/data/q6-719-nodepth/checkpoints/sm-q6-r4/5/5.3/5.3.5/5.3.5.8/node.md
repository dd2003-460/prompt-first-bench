# N309: K_base(t) 的峰值时段识别：通过 K_base(t) > 2.5 的时段定义峰值窗口 T_peak_hours，计算峰值窗口占全天比例 P_peak =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

K_base(t) 的峰值时段识别：通过 K_base(t) > 2.5 的时段定义峰值窗口 T_peak_hours，计算峰值窗口占全天比例 P_peak = T_peak_hours / 24；该比例用于修正带宽计费模式（峰值计费 vs 流量计费）的成本差异，关联 N106 的成本放大系数 C_amp。

## Corrected Claim

K_base(t) 的峰值时段识别：通过 K_base(t) > 2.5 的时段定义峰值窗口 T_peak_hours，计算峰值窗口占全天比例 P_peak = T_peak_hours / 24；该比例用于修正带宽计费模式（峰值计费 vs 流量计费）的成本差异，关联 N106 的成本放大系数 C_amp。

## Evidence

先验知识/题面给定，逻辑校验通过
