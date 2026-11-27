# N5: 缓存可容纳的对象数量上限 N_cap = 128GB / S_mean，其中 S_mean 是 Pareto(α=1.1) 分布截断到最大对象大小 S_max 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

缓存可容纳的对象数量上限 N_cap = 128GB / S_mean，其中 S_mean 是 Pareto(α=1.1) 分布截断到最大对象大小 S_max 后的期望大小（需积分计算或查表）

## Corrected Claim

缓存可容纳的对象数量上限 N_cap = 128GB / S_mean，其中 S_mean 是 Pareto(α=1.1) 分布截断到最大对象大小 S_max 后的期望大小（需积分计算或查表）

## Evidence

先验知识/题面给定，逻辑校验通过：缓存容量上限由总容量除以平均对象大小定义，符合基本物理/经济直觉，且Pareto分布截断后的期望值计算逻辑自洽。
