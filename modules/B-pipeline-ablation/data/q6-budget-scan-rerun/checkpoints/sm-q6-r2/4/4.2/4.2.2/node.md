# N78: 单POP点容量 C_pop 的确定逻辑：C_pop 需满足 C_pop >= B_peak_pop / U_target，其中 U_target 为目标利用率（

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

单POP点容量 C_pop 的确定逻辑：C_pop 需满足 C_pop >= B_peak_pop / U_target，其中 U_target 为目标利用率（40%-60%）。若取 U_target=50% 且 B_peak_pop=7.92 Mbps（均匀分布），则 C_pop >= 15.84 Mbps。考虑到硬件规格标准化，实际选型通常向上取整至标准带宽套餐（如 20 Mbps 或 50 Mbps），导致实际利用率 U_actual = B_peak_pop / C_selected 低于理论值。

## Corrected Claim

单POP点容量 C_pop 的确定逻辑：C_pop 需满足 C_pop >= B_peak_pop / U_target，其中 U_target 为目标利用率（40%-60%）。若取 U_target=50% 且 B_peak_pop=7.92 Mbps（均匀分布），则 C_pop >= 15.84 Mbps。考虑到硬件规格标准化，实际选型通常向上取整至标准带宽套餐（如 20 Mbps 或 50 Mbps），导致实际利用率 U_actual = B_peak_pop / C_selected 低于理论值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C >= B/U 符合容量规划基本定义，数值计算 7.92/0.5=15.84 正确，向上取整至标准套餐符合工程惯例。

## Search Query

network capacity planning utilization target 50%
