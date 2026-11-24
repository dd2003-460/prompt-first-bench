# N467: Pareto 形状参数 α 的估计方法：采用最大似然估计 (MLE) 或 Hill 估计量，基于实测 RTT 样本尾部数据（如 Top 1% 样本）计算，α =

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

Pareto 形状参数 α 的估计方法：采用最大似然估计 (MLE) 或 Hill 估计量，基于实测 RTT 样本尾部数据（如 Top 1% 样本）计算，α = N / (Σ ln(x_i / x_min))。

## Corrected Claim

Pareto 形状参数 α 的估计方法：采用最大似然估计 (MLE) 或 Hill 估计量，基于实测 RTT 样本尾部数据（如 Top 1% 样本）计算，α = N / (Σ ln(x_i / x_min))。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布MLE公式及Hill估计量原理正确，量纲与数学推导自洽。
