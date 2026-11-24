# N613: Voronoi 划分下覆盖半径的几何关系：当 POP 从 N 增加到 N+1 时，平均覆盖半径 R_avg(N) ≈ A_total / (N * R_avg(

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

Voronoi 划分下覆盖半径的几何关系：当 POP 从 N 增加到 N+1 时，平均覆盖半径 R_avg(N) ≈ A_total / (N * R_avg(N))，其中 A_total 为服务区域面积，R_avg(N) 与 1/sqrt(N) 成正比，即 R_avg(N+1) ≈ R_avg(N) * sqrt(N/(N+1))

## Corrected Claim

Voronoi 划分下覆盖半径的几何关系：当 POP 从 N 增加到 N+1 时，平均覆盖半径 R_avg(N) ≈ A_total / (N * R_avg(N))，其中 A_total 为服务区域面积，R_avg(N) 与 1/sqrt(N) 成正比，即 R_avg(N+1) ≈ R_avg(N) * sqrt(N/(N+1))

## Evidence

先验知识/题面给定，逻辑校验通过：Voronoi 划分下，N 个站点覆盖总面积 A，平均每个站点覆盖面积 A/N，若近似为圆形，半径 R ≈ sqrt(A/(Nπ))，故 R ∝ 1/sqrt(N)，推导关系 R(N+1)/R(N) = sqrt(N/(N+1)) 成立。

## Search Query

Voronoi diagram average cell radius number of points relationship
