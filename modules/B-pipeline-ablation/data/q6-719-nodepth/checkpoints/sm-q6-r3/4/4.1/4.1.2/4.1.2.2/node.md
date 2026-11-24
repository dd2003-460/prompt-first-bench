# N324: D_user_edge_p99 的几何计算需基于用户分布密度 ρ(u) 与 POP 位置集合 {P_i}，计算第 99 百分位的欧氏距离或路由距离 d_99 =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

D_user_edge_p99 的几何计算需基于用户分布密度 ρ(u) 与 POP 位置集合 {P_i}，计算第 99 百分位的欧氏距离或路由距离 d_99 = min_i(dist(u, P_i))，而非简单平均。

## Corrected Claim

D_user_edge_p99 的几何计算需基于用户分布密度 ρ(u) 与 POP 位置集合 {P_i}，计算第 99 百分位的欧氏距离或路由距离 d_99 = min_i(dist(u, P_i))，而非简单平均。

## Evidence

先验知识/题面给定，逻辑校验通过：基于用户分布密度和POP位置计算第99百分位距离是标准的网络覆盖/延迟建模方法，逻辑自洽且符合工程直觉。
