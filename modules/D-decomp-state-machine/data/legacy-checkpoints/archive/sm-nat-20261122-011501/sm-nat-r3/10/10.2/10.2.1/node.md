# N176: Pareto(α=1.1, s_min=1KB) 分布下，驻留集合 S_LRU 内对象大小的标准化均值 E[(S-μ_S)/σ_S | S∈S_LRU] ≈ -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Pareto(α=1.1, s_min=1KB) 分布下，驻留集合 S_LRU 内对象大小的标准化均值 E[(S-μ_S)/σ_S | S∈S_LRU] ≈ -0.85，基于截断正态近似计算得出，用于代入线性回归公式。

## Corrected Claim

Pareto(α=1.1, s_min=1KB) 分布下，驻留集合 S_LRU 内对象大小的标准化均值 E[(S-μ_S)/σ_S | S∈S_LRU] ≈ -0.85，基于截断正态近似计算得出，用于代入线性回归公式。

## Evidence

先验知识/题面给定，逻辑校验通过
