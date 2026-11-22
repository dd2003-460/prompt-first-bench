# N107: 方差贡献度计算公式：使用Sobol指数或Shapley值量化各假设不确定性对最终结论（最小干预方案选择）的方差贡献，公式为 V(X_i) = E[V(Y|X_i

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

方差贡献度计算公式：使用Sobol指数或Shapley值量化各假设不确定性对最终结论（最小干预方案选择）的方差贡献，公式为 V(X_i) = E[V(Y|X_i)]，其中Y为干预效果指标，X_i为第i个假设变量。

## Corrected Claim

方差贡献度可通过Sobol指数或Shapley值量化。Sobol指数通常定义为 V(X_i) = E[V(Y|X_i)] - V(Y)（或根据具体定义调整），而Shapley值基于合作博弈论计算各变量对总方差的边际贡献。

## Evidence

[质询]公式表述存在概念混淆：V(X_i) = E[V(Y|X_i)] 实际上是条件方差的期望，而非标准的 Sobol 方差贡献度（通常定义为 E[V(Y|X_i)] - V(Y) 或类似形式，取决于具体定义，但直接等同于总方差贡献是不准确的，且 Shapley 值有独立的组合数学定义，不能简单用此公式概括）。 | 先验知识/题面给定，逻辑校验通过但公式表述不够严谨，Sobol指数和Shapley值有各自的标准定义，该公式仅为简化或特定语境下的近似表达。
