# N78: Copula 模型对尾部特性的保持验证：Gaussian Copula 在尾部相关系数为 0（即尾部独立），而 Pareto 分布具有重尾特性，因此 Gauss

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

Copula 模型对尾部特性的保持验证：Gaussian Copula 在尾部相关系数为 0（即尾部独立），而 Pareto 分布具有重尾特性，因此 Gaussian Copula 会低估尾部对象（大 i）的联合概率；需使用 t-Copula 或 Clayton Copula 以更好地捕捉重尾依赖结构。

## Corrected Claim

Copula 模型对尾部特性的保持验证：Gaussian Copula 在尾部相关系数为 0（即尾部独立），而 Pareto 分布具有重尾特性，因此 Gaussian Copula 会低估尾部对象（大 i）的联合概率；需使用 t-Copula 或 Clayton Copula 以更好地捕捉重尾依赖结构。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 具有尾部独立性质（upper/lower tail dependence coefficient 为 0），而 Pareto 分布具有重尾特性，因此 Gaussian Copula 确实会低估尾部联合概率；t-Copula 和 Clayton Copula 分别具有上尾和下尾依赖性，能更好地捕捉重尾依赖结构。
