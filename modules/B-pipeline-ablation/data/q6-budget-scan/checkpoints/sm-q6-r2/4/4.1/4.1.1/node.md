# N57: 自建POP点最优覆盖半径 R_opt 与熵 H_geo 的关系：R_opt = f(H_geo, N_pop)，其中 N_pop 为POP点数量（10），H_g

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

自建POP点最优覆盖半径 R_opt 与熵 H_geo 的关系：R_opt = f(H_geo, N_pop)，其中 N_pop 为POP点数量（10），H_geo 越高，R_opt 越大，需通过优化算法（如K-means）计算最小化平均回源距离的POP点位置。

## Corrected Claim

自建POP点最优覆盖半径 R_opt 与熵 H_geo 的关系：R_opt = f(H_geo, N_pop)，其中 N_pop 为POP点数量（10），H_geo 越高，R_opt 越大，需通过优化算法（如K-means）计算最小化平均回源距离的POP点位置。

## Evidence

先验知识/题面给定，逻辑校验通过：在地理覆盖优化中，熵值高代表分布分散，为覆盖相同区域或达到相同服务等级，单个POP点的平均覆盖半径确实需要增大；K-means是求解此类聚类覆盖问题的标准算法。

## Search Query

optimal POP point coverage radius entropy K-means
