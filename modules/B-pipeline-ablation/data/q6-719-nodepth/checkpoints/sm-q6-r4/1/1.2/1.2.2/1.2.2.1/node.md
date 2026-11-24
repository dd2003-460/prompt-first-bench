# N156: 对数正态分布下 P99 延迟的精确计算：若 RTT 服从对数正态分布 LogNormal(μ, σ²)，则 P99 = exp(μ + 2.326σ)，其中 μ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

对数正态分布下 P99 延迟的精确计算：若 RTT 服从对数正态分布 LogNormal(μ, σ²)，则 P99 = exp(μ + 2.326σ)，其中 μ 和 σ 由实测 RTT 数据的几何均值和标准差决定。

## Corrected Claim

对数正态分布下 P99 延迟的精确计算：若 RTT 服从对数正态分布 LogNormal(μ, σ²)，则 P99 = exp(μ + 2.326σ)，其中 μ 和 σ 由实测 RTT 数据的几何均值和标准差决定。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布的定义及分位数公式推导正确，2.326为99%分位点的标准正态分布临界值，量纲与逻辑自洽。

## Search Query

lognormal distribution 99th percentile formula network latency
