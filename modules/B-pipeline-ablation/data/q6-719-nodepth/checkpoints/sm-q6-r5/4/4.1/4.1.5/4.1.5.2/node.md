# N250: 峰值带宽需求对计费模式的影响：若采用按带宽峰值计费（95th percentile billing），需计算月内 95 百分位带宽值 B_95 = B_peak

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

峰值带宽需求对计费模式的影响：若采用按带宽峰值计费（95th percentile billing），需计算月内 95 百分位带宽值 B_95 = B_peak * (1 - 0.05 * T_peak / T_month)，其中 T_peak 为峰值持续时间；若峰值 69.3Gbps 持续 4 小时/天，则 B_95 ≈ 69.3 * (1 - 0.05 * (4*30)/720) ≈ 69.3 * 0.972 ≈ 67.4 Gbps，低于 83.16Gbps，故按 95 计费时合同带宽可低于按绝对峰值计费。

## Corrected Claim

峰值带宽需求对计费模式的影响：若采用按带宽峰值计费（95th percentile billing），需计算月内 95 百分位带宽值 B_95 = B_peak * (1 - 0.05 * T_peak / T_month)，其中 T_peak 为峰值持续时间；若峰值 69.3Gbps 持续 4 小时/天，则 B_95 ≈ 69.3 * (1 - 0.05 * (4*30)/720) ≈ 69.3 * 0.972 ≈ 67.4 Gbps，低于 83.16Gbps，故按 95 计费时合同带宽可低于按绝对峰值计费。

## Search Query

CDN 95th percentile bandwidth billing calculation formula peak duration
