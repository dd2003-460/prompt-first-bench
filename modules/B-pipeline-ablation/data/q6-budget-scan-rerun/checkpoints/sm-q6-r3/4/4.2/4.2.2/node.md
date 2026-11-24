# N78: 单POP点容量 C_pop 的确定逻辑：C_pop 需满足 C_pop >= B_peak_pop / U_target，其中 U_target 为目标利用率（

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一决策变量（C_selected）的两个不同取值实例，而非正交的逻辑分支；且未覆盖父节点中明确提到的‘硬件规格标准化/向上取整’这一核心约束逻辑，仅展示了结果。）

## Search Query

network capacity planning utilization target 50%
