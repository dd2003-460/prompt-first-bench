# N294: 置信区间计算方法：使用 Bootstrap 法而非正态近似，因为 Pareto(α=1.1) 的样本均值分布非正态；需对每次仿真的命中率序列进行 1000 次重

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

置信区间计算方法：使用 Bootstrap 法而非正态近似，因为 Pareto(α=1.1) 的样本均值分布非正态；需对每次仿真的命中率序列进行 1000 次重抽样，计算 95% 分位数区间。

## Corrected Claim

置信区间计算方法：使用 Bootstrap 法而非正态近似，因为 Pareto(α=1.1) 的样本均值分布非正态；需对每次仿真的命中率序列进行 1000 次重抽样，计算 95% 分位数区间。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 分布尾部极重，样本均值收敛极慢且非正态，使用 Bootstrap 法计算置信区间在统计学上是合理且必要的选择。
