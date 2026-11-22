# N339: 经验置信区间 [CI_lower, CI_upper] 的计算基于 10,000 次模拟结果 I^(k) 的排序统计量：CI_lower 为第 2.5 百分位数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N108

## Claim

经验置信区间 [CI_lower, CI_upper] 的计算基于 10,000 次模拟结果 I^(k) 的排序统计量：CI_lower 为第 2.5 百分位数，CI_upper 为第 97.5 百分位数；若 CI 宽度 > 0.2，则表明结论对参数不确定性高度敏感，需增加模拟次数或细化先验分布。

## Corrected Claim

经验置信区间 [CI_lower, CI_upper] 的计算基于 10,000 次模拟结果 I^(k) 的排序统计量：CI_lower 为第 2.5 百分位数，CI_upper 为第 97.5 百分位数；若 CI 宽度 > 0.2，则表明结论对参数不确定性高度敏感，需增加模拟次数或细化先验分布。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Monte Carlo empirical confidence interval calculation order statistics sensitivity width
