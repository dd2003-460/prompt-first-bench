# N93: Gaussian Copula 假设下，Pareto 重尾分布与高斯尾部的偏差量化：当 r 处于尾部（r > 99th percentile）时，高斯近似导致的

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Gaussian Copula 假设下，Pareto 重尾分布与高斯尾部的偏差量化：当 r 处于尾部（r > 99th percentile）时，高斯近似导致的条件期望 E[S|R] 相对误差 [待核验]，预计误差 >30%，需引入 t-Copula 或 Empirical Copula 修正。

## Corrected Claim

Gaussian Copula 假设下，对于 Pareto 重尾分布，高斯近似会低估尾部依赖强度，导致条件期望 E[S|R] 出现显著偏差（具体幅度取决于分布参数），通常需引入 t-Copula 或 Empirical Copula 进行修正。

## Evidence

[质询]该陈述包含具体的经验性数值断言（误差 >30%），但缺乏具体的分布参数（如自由度、相关系数、尾部阈值定义）作为前提。不同参数组合下，高斯近似与真实重尾分布的条件期望偏差可能远小于或远大于30%，因此该具体数值缺乏普适性，属于未经验证的特定场景结论。 | 先验知识/题面给定，逻辑校验通过。Gaussian Copula 确实无法捕捉重尾依赖结构，导致尾部条件期望估计偏差，这是金融风险管理中的已知缺陷；但具体误差幅度（>30%）依赖于具体分布参数，属于经验事实，在无外部来源支持且参数未固定的情况下，降级为定性表述。

## Search Query

Gaussian copula tail dependence bias Pareto distribution
