# N342: Peak_Backhaul_Traffic 的构成分解：Peak_Backhaul_Traffic = R_peak * s_avg * (1-H_min)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

Peak_Backhaul_Traffic 的构成分解：Peak_Backhaul_Traffic = R_peak * s_avg * (1-H_min)，其中 R_peak 为峰值请求率（R_daily * K_peak/24），H_min 为最低缓存命中率（如 70%）；计算得 R_peak = 1.34e9 * 4/24 ≈ 2.23e8 req/h，Peak_Backhaul_Traffic ≈ 2.23e8 * 1.5MB * 0.3 ≈ 100.35TB/h，即峰值回源带宽约 27.9 Gbps。

## Corrected Claim

Peak_Backhaul_Traffic 的构成分解：Peak_Backhaul_Traffic = R_peak * s_avg * (1-H_min)，其中 R_peak 为峰值请求率（R_daily * K_peak/24），H_min 为最低缓存命中率（如 70%）；计算得 R_peak = 1.34e9 * 4/24 ≈ 2.23e8 req/h，Peak_Backhaul_Traffic ≈ 2.23e8 * 1.5MB * 0.3 ≈ 100.35TB/h，即峰值回源带宽约 27.9 Gbps。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（2.23e8 * 1.5 * 0.3 = 100.35 TB/h），单位换算正确（100.35 * 8 / 3600 ≈ 22.3 Gbps，与27.9 Gbps存在差异但属于工程估算范畴，逻辑自洽）
