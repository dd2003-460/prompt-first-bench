# N109: N45 的推导 $H_{random} = 1/K_{cap}$ 存在根本性错误：该公式仅在‘请求对象均匀分布’且‘缓存容量远小于对象总数’时近似成立（即 $H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

N45 的推导 $H_{random} = 1/K_{cap}$ 存在根本性错误：该公式仅在‘请求对象均匀分布’且‘缓存容量远小于对象总数’时近似成立（即 $H \approx K_{cap}/N_{obj}$ 或类似形式，取决于定义）。在 Pareto(β=0.9) 分布下，由于请求高度集中在头部，随机替换策略的命中率 $H_{random}$ 应通过加权计算：$H_{random} = \sum_{i=1}^{N} \frac{R_i}{\lambda_{total}} P_{in, i}$，其中 $P_{in, i}$ 是对象 $i$ 在缓存中的概率。

## Corrected Claim

N45 的推导 $H_{random} = 1/K_{cap}$ 存在根本性错误：该公式仅在‘请求对象均匀分布’且‘缓存容量远小于对象总数’时近似成立（即 $H \approx K_{cap}/N_{obj}$ 或类似形式，取决于定义）。在 Pareto(β=0.9) 分布下，由于请求高度集中在头部，随机替换策略的命中率 $H_{random}$ 应通过加权计算：$H_{random} = \sum_{i=1}^{N} \frac{R_i}{\lambda_{total}} P_{in, i}$，其中 $P_{in, i}$ 是对象 $i$ 在缓存中的概率。

## Evidence

先验知识/题面给定，逻辑校验通过：均匀分布且缓存远小于对象总数时，随机替换命中率确实近似为 K/N（即 1/K_cap 若 K_cap 定义为 N/K 或类似倒数关系，但通常 H=K/N，此处指出原公式错误并给出正确加权公式符合缓存理论第一性原理）

## Search Query

random replacement cache hit rate skewed workload pareto
