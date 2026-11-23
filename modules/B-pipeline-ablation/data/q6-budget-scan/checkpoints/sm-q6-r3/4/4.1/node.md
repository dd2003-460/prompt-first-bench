# N18: 用户地理分布熵 H_geo = -Σ p_i log2(p_i)，其中 p_i 为第 i 个省份/区域的流量占比；该指标决定自建 POP 点的最优覆盖半径与回源

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

用户地理分布熵 H_geo = -Σ p_i log2(p_i)，其中 p_i 为第 i 个省份/区域的流量占比；该指标决定自建 POP 点的最优覆盖半径与回源距离

## Corrected Claim

用户地理分布熵 H_geo = -Σ p_i log2(p_i)，其中 p_i 为第 i 个省份/区域的流量占比；该指标决定自建 POP 点的最优覆盖半径与回源距离

## Evidence

父节点级核验未通过：不完备（子节点存在严重的因果倒置和逻辑冗余。父节点定义熵是决定覆盖半径和回源距离的‘因’，但子节点将两者表述为相互依赖的函数（R_opt 依赖 H_geo，d_avg 依赖 R_opt），忽略了 H_geo 对 d_avg 的直接决定作用。此外，'最优覆盖半径'与'回源距离'在地理分布熵的语境下，本质上是同一空间优化问题（K-means聚类）的两个输出维度，而非完全独立的正交概念，且未覆盖熵值计算本身或分布均匀性的具体影响机制。）
