# N56: 功耗曲线建模：定义 P_avg = P_idle * (1 - U) + P_peak * U，其中 U 为利用率因子。针对 RTX 4090 (P_idle=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

功耗曲线建模：定义 P_avg = P_idle * (1 - U) + P_peak * U，其中 U 为利用率因子。针对 RTX 4090 (P_idle=30W, P_peak=450W)，计算 U=0.5 时的 P_avg = 240W

## Corrected Claim

功耗曲线建模：定义 P_avg = P_idle * (1 - U) + P_peak * U，其中 U 为利用率因子。针对 RTX 4090 (P_idle=30W, P_peak=450W)，计算 U=0.5 时的 P_avg = 240W

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_avg = 30*(1-0.5) + 450*0.5 = 15 + 225 = 240W，计算无误且符合线性插值模型定义。
