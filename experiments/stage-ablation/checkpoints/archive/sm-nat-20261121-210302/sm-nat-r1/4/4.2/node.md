# N10: Pareto 分布下对象大小总和与头部对象占比的解析解：总字节数 E[S] = α/(α-1) * X_min (当 α>1)，前 k% 对象占总字节数的比例为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Pareto 分布下对象大小总和与头部对象占比的解析解：总字节数 E[S] = α/(α-1) * X_min (当 α>1)，前 k% 对象占总字节数的比例为 1 - (0.01)^((α-1)/α)，用于确定缓存需覆盖的最小对象集

## Corrected Claim

Pareto 分布下对象大小总和与头部对象占比的解析解：总字节数 E[S] = α/(α-1) * X_min (当 α>1)，前 k% 对象占总字节数的比例为 1 - (0.01)^((α-1)/α)，用于确定缓存需覆盖的最小对象集

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布（α>1）的期望公式 E[S]=α/(α-1)*X_min 及前k%对象占比公式 1-(0.01)^((α-1)/α) 均符合数学推导，量纲与逻辑自洽。

## Search Query

Pareto distribution cumulative byte fraction head objects formula
