# N138: 95th Percentile 计费模式的成本计算：C_p95 = B_p95 * P_bw_p95_monthly，其中 B_p95 为月度内每 5 分钟采样

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

95th Percentile 计费模式的成本计算：C_p95 = B_p95 * P_bw_p95_monthly，其中 B_p95 为月度内每 5 分钟采样带宽的第 95 百分位值；若流量分布平滑，B_p95 ≈ B_avg * 1.2-1.5，成本介于峰值与流量计费之间，通常比纯峰值计费低 30-50%

## Corrected Claim

95th Percentile 计费模式的成本计算：C_p95 = B_p95 * P_bw_p95_monthly，其中 B_p95 为月度内每 5 分钟采样带宽的第 95 百分位值；若流量分布平滑，B_p95 ≈ B_avg * 1.2-1.5，成本介于峰值与流量计费之间，通常比纯峰值计费低 30-50%

## Evidence

先验知识/题面给定，逻辑校验通过
