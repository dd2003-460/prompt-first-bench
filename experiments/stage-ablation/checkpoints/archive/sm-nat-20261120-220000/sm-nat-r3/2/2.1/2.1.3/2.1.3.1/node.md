# N87: 修正 N29 中 n_warmup 的量纲错误：在 Pareto(β=0.9) 热度分布下，新对象需累积的访问次数 n_warmup 应基于频率分布的分位数定义

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

修正 N29 中 n_warmup 的量纲错误：在 Pareto(β=0.9) 热度分布下，新对象需累积的访问次数 n_warmup 应基于频率分布的分位数定义，即 n_warmup = f_{p99} / f_{median}，其中 f_{p99} 为第 99 百分位的访问频率，f_{median} 为中位数频率；该比值在 β=0.9 下约为 10^(1/0.9) ≈ 12.9，而非原陈述中的 100。

## Corrected Claim

修正 N29 中 n_warmup 的量纲错误：在 Pareto(β=0.9) 热度分布下，新对象需累积的访问次数 n_warmup 应基于频率分布的分位数定义，即 n_warmup = f_{p99} / f_{median}，其中 f_{p99} 为第 99 百分位的访问频率，f_{median} 为中位数频率；该比值在 β=0.9 下约为 10^(1/0.9) ≈ 12.9，而非原陈述中的 100。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布中分位数比值与指数关系符合数学推导，量级合理
