# N78: Gaussian Copula 在重尾 Pareto 边缘下的尾部相关性偏差量化：由于 Gaussian Copula 假设联合尾部概率为 0，而实际 Pare

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Gaussian Copula 在重尾 Pareto 边缘下的尾部相关性偏差量化：由于 Gaussian Copula 假设联合尾部概率为 0，而实际 Pareto 联合分布可能存在非零尾部相关，需计算 P(S > S_99, f > f_99) 的 Copula 值与独立假设值的差异，预期偏差在 5-15% 范围内，需通过模拟验证。

## Corrected Claim

Gaussian Copula 在重尾 Pareto 边缘下会显著低估尾部相关性（因为 Gaussian Copula 假设联合尾部概率为 0，而 Pareto 分布存在非零尾部相关），具体偏差幅度取决于 Pareto 尾部指数和 Copula 参数，需通过模拟验证，典型偏差可能在百分之几到百分之几十之间。

## Evidence

[质询]「5-15%」的偏差范围缺乏普适性，具体数值高度依赖于Pareto分布的尾部指数（alpha）以及Copula参数（如相关系数rho）的具体取值，不同参数组合下偏差可能远小于或大于此范围，该数值属于特定模拟场景下的经验结果而非通用理论结论。 | 先验知识/题面给定，逻辑校验通过：Gaussian Copula确实假设联合尾部概率为0（椭圆Copula性质），而Pareto边缘具有厚尾特性，两者结合会导致尾部相关性被低估，逻辑自洽；但具体偏差数值5-15%为经验估计，无来源支持且非第一性原理可严格推导的固定值，故降级。
