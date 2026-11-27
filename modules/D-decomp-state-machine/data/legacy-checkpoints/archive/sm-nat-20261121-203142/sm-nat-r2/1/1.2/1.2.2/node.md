# N30: 由于 β=0.9 < 1，Pareto 分布的数学期望 E[R] 发散，因此不能使用 E[R] 进行归一化；必须使用截断后的平均请求频率 E[R|truncat

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

由于 β=0.9 < 1，Pareto 分布的数学期望 E[R] 发散，因此不能使用 E[R] 进行归一化；必须使用截断后的平均请求频率 E[R|truncated] 或直接用总请求量约束积分 ∫f_R(r)dr = 1 来确定分布尺度参数

## Corrected Claim

由于 β=0.9 < 1，Pareto 分布的数学期望 E[R] 发散，因此不能使用 E[R] 进行归一化；必须使用截断后的平均请求频率 E[R|truncated] 或直接用总请求量约束积分 ∫f_R(r)dr = 1 来确定分布尺度参数

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布当形状参数α≤1时数学期望发散，β=0.9<1符合此条件，故E[R]不存在，必须使用截断均值或归一化约束确定尺度参数。

## Search Query

Pareto distribution beta less than 1 mean divergent normalization
