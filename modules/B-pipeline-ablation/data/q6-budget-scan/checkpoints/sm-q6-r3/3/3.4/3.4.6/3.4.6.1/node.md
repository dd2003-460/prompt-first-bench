# N302: K-means聚类算法在POP点选址中的目标函数：最小化加权距离总和 Min Σ(w_i * d_i)，其中w_i为用户密度权重，d_i为用户到最近POP点的距

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

K-means聚类算法在POP点选址中的目标函数：最小化加权距离总和 Min Σ(w_i * d_i)，其中w_i为用户密度权重，d_i为用户到最近POP点的距离；约束条件为每个POP点覆盖半径≤50km，且总覆盖用户比例≥80%。

## Corrected Claim

K-means聚类算法在POP点选址中的目标函数：最小化加权距离总和 Min Σ(w_i * d_i)，其中w_i为用户密度权重，d_i为用户到最近POP点的距离；约束条件为每个POP点覆盖半径≤50km，且总覆盖用户比例≥80%。

## Evidence

先验知识/题面给定，逻辑校验通过
