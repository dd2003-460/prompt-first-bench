# N177: 最优覆盖半径 R_opt 与平均距离 d_avg 的近似关系：R_opt ≈ 1.5 * d_avg，其中 d_avg 为 K-means 聚类后的平均用户到最

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

最优覆盖半径 R_opt 与平均距离 d_avg 的近似关系：R_opt ≈ 1.5 * d_avg，其中 d_avg 为 K-means 聚类后的平均用户到最近 POP 点距离；若 d_avg = 200km，则 R_opt ≈ 300km，需验证该半径内 95% 的用户可被覆盖

## Corrected Claim

最优覆盖半径 R_opt 与平均距离 d_avg 的近似关系：R_opt ≈ 1.5 * d_avg，其中 d_avg 为 K-means 聚类后的平均用户到最近 POP 点距离；若 d_avg = 200km，则 R_opt ≈ 300km，需验证该半径内 95% 的用户可被覆盖

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

optimal coverage radius K-means cluster distance approximation
