# N11: 请求热度 Pareto(β=0.9) 的累积分布函数 CDF(r) = (r_min/r)^β，其中 r_min 是最小请求率，前 k 个最热门对象的请求占比 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

请求热度 Pareto(β=0.9) 的累积分布函数 CDF(r) = (r_min/r)^β，其中 r_min 是最小请求率，前 k 个最热门对象的请求占比 = 1 - (k/N)^β（近似，假设对象按热度排序）

## Corrected Claim

请求热度 Pareto(β=0.9) 的累积分布函数 CDF(r) = (r_min/r)^β，其中 r_min 是最小请求率，前 k 个最热门对象的请求占比 = 1 - (k/N)^β（近似，假设对象按热度排序）

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的CDF定义及前k项占比推导符合数学逻辑

## Search Query

Pareto distribution CDF request popularity cache
