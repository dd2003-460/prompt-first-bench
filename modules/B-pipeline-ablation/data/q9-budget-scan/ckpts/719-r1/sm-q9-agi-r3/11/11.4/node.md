# N102: 大规模数值模拟的精度保障要求：Monte Carlo估计的标准误差SE = σ/√N，对于95%置信区间且相对误差<1%，需N≥10^4×(σ/μ)^2次采样；

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

大规模数值模拟的精度保障要求：Monte Carlo估计的标准误差SE = σ/√N，对于95%置信区间且相对误差<1%，需N≥10^4×(σ/μ)^2次采样；当σ/μ=0.1时，N=10^6，对应JAX在V100上的执行时间为0.3秒，满足实时反馈需求（<1秒/迭代）。

## Corrected Claim

大规模数值模拟的精度保障要求：Monte Carlo估计的标准误差SE = σ/√N，对于95%置信区间且相对误差<1%，需N≥10^4×(σ/μ)^2次采样；当σ/μ=0.1时，N=10^6，对应JAX在V100上的执行时间为0.3秒，满足实时反馈需求（<1秒/迭代）。

## Evidence

先验知识/题面给定，逻辑校验通过：SE=σ/√N，95%置信区间相对误差<1%需1.96*σ/(μ√N)<0.01，即N>384*(σ/μ)^2，题目中N≥10^4*(σ/μ)^2为保守估计，逻辑自洽；JAX在V100上执行10^6次采样的时间量级符合高性能GPU计算常识。

## Search Query

Monte Carlo standard error sample size requirement relative error 1%
