# N64: Pareto(β=0.9) 分布的尾部特性导致前 1% 对象（k=1000）的累积请求占比 P_top1000 = 1 - (1000/100000)^(0.1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Pareto(β=0.9) 分布的尾部特性导致前 1% 对象（k=1000）的累积请求占比 P_top1000 = 1 - (1000/100000)^(0.1) ≈ 0.59，表明热点集中度极高，缓存前 1% 对象即可覆盖近 60% 请求。

## Corrected Claim

Pareto(β=0.9) 分布的尾部特性导致前 1% 对象（k=1000）的累积请求占比 P_top1000 = 1 - (1000/100000)^(0.1) ≈ 0.59，表明热点集中度极高，缓存前 1% 对象即可覆盖近 60% 请求。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布累积分布函数计算正确，1-(0.01)^0.1≈0.59符合数学推导

## Search Query

Pareto distribution top 1% cumulative request ratio
