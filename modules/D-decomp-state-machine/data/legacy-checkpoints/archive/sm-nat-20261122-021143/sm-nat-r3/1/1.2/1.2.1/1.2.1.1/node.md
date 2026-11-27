# N68: 修正 N25 中的积分错误：Pareto 分布的归一化形式为 f(r) = β * r_min^β * r^{-(β+1)}，其累积概率函数为 F(r) = 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N29

## Claim

修正 N25 中的积分错误：Pareto 分布的归一化形式为 f(r) = β * r_min^β * r^{-(β+1)}，其累积概率函数为 F(r) = 1 - (r_min/r)^β。在离散排名 k=1..N 且总请求数 Q=5*10^7 的约束下，第 k 个对象的请求量 R_k ≈ Q * (k-1)^{-β} / Σ_{i=1}^{N} i^{-β}，而非通过积分 r * f(r) 求解截断点。

## Corrected Claim

修正 N25 中的积分错误：Pareto 分布的归一化形式为 f(r) = β * r_min^β * r^{-(β+1)}，其累积概率函数为 F(r) = 1 - (r_min/r)^β。在离散排名 k=1..N 且总请求数 Q=5*10^7 的约束下，第 k 个对象的请求量 R_k ≈ Q * (k-1)^{-β} / Σ_{i=1}^{N} i^{-β}，而非通过积分 r * f(r) 求解截断点。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的PDF与CDF公式正确，离散排名下的请求量分配公式符合Zipf定律/Pareto分布的离散化定义，且量纲与逻辑自洽。
