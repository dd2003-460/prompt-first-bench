# N61: 选址优化目标函数：Minimize Weighted_Avg_RTT = Σ_i (p_i * min_j D[i][j])，约束条件为每个 POP 点 j 的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12, N13, N14

## Claim

选址优化目标函数：Minimize Weighted_Avg_RTT = Σ_i (p_i * min_j D[i][j])，约束条件为每个 POP 点 j 的服务半径内用户占比 ≥ 5%，且总覆盖用户比例 ≥ 95%。

## Corrected Claim

选址优化目标函数：Minimize Weighted_Avg_RTT = Σ_i (p_i * min_j D[i][j])，约束条件为每个 POP 点 j 的服务半径内用户占比 ≥ 5%，且总覆盖用户比例 ≥ 95%。

## Evidence

先验知识/题面给定，逻辑校验通过
