# N68: 带宽成本对峰谷比的敏感度 dCost/dR_pg：Cost_bandwidth_peak = (B_avg × R_pg × unit_cost) / 年请求量

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

带宽成本对峰谷比的敏感度 dCost/dR_pg：Cost_bandwidth_peak = (B_avg × R_pg × unit_cost) / 年请求量 × 1000。当 R_pg 从 3 增至 5 时，带宽成本增加 (5-3)/3 = 66.7%。需计算在 R_pg ∈ [3, 5] 范围内，每增加 0.1 的 R_pg，每千请求成本增加 ΔC = (0.1 × B_avg × unit_cost) / 年请求量 × 1000。

## Corrected Claim

带宽成本对峰谷比的敏感度 dCost/dR_pg：Cost_bandwidth_peak = (B_avg × R_pg × unit_cost) / 年请求量 × 1000。当 R_pg 从 3 增至 5 时，带宽成本增加 (5-3)/3 = 66.7%。需计算在 R_pg ∈ [3, 5] 范围内，每增加 0.1 的 R_pg，每千请求成本增加 ΔC = (0.1 × B_avg × unit_cost) / 年请求量 × 1000。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Cost = (B_avg * R_pg * unit_cost) / Q * 1000 中，Cost 与 R_pg 呈线性正比关系。当 R_pg 从 3 增至 5 时，变化率为 (5-3)/3 = 2/3 ≈ 66.7%，推导正确；微分敏感度 dCost/dR_pg 即为系数 (B_avg * unit_cost) / Q * 1000，每增加 0.1 的 R_pg，增量 ΔC = 0.1 * 系数，逻辑自洽且量纲合理。
