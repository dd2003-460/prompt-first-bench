# N57: POP 选址优化目标函数：min Σ_i (g_i * d_i^2) 或 min Σ_i (g_i * d_i)，其中 g_i 为用户占比，d_i 为到最近 P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

POP 选址优化目标函数：min Σ_i (g_i * d_i^2) 或 min Σ_i (g_i * d_i)，其中 g_i 为用户占比，d_i 为到最近 POP 的距离；Voronoi 划分下，平均覆盖半径 R_avg = sqrt(Σ(g_i * d_i^2))，需对比均匀分布假设下的 D_max/sqrt(N) 误差。

## Corrected Claim

POP 选址优化目标函数：min Σ_i (g_i * d_i^2) 或 min Σ_i (g_i * d_i)，其中 g_i 为用户占比，d_i 为到最近 POP 的距离；Voronoi 划分下，平均覆盖半径 R_avg = sqrt(Σ(g_i * d_i^2))，需对比均匀分布假设下的 D_max/sqrt(N) 误差。

## Evidence

先验知识/题面给定，逻辑校验通过：目标函数符合加权最小二乘/最小距离原则，Voronoi划分下平均覆盖半径公式量纲正确（距离单位），与均匀分布误差对比逻辑自洽。
