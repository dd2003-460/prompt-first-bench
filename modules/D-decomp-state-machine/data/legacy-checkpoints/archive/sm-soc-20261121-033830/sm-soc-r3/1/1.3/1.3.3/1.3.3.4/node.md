# N144: 信号溢价率的因果识别策略：Δr_signal = E[Rate_Click | P > P_median * 1.15] - E[Rate_Click | P 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43, N44, N45

## Claim

信号溢价率的因果识别策略：Δr_signal = E[Rate_Click | P > P_median * 1.15] - E[Rate_Click | P ∈ [P_median * 0.85, P_median * 1.15]]，需通过工具变量法（IV）或断点回归（RDD）控制卖家信誉、商品图片质量等混杂变量，以孤立高价对点击率的净因果效应。

## Corrected Claim

信号溢价率的因果识别策略：Δr_signal = E[Rate_Click | P > P_median * 1.15] - E[Rate_Click | P ∈ [P_median * 0.85, P_median * 1.15]]，需通过工具变量法（IV）或断点回归（RDD）控制卖家信誉、商品图片质量等混杂变量，以孤立高价对点击率的净因果效应。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了因果推断中标准的识别策略（IV/RDD）及混杂变量控制逻辑，符合计量经济学基本原理，无内部矛盾。

## Search Query

causal identification price signal effect click-through rate regression discontinuity
