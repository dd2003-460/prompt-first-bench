# N168: Prob_Coverage_128 的分子 ∫_{0}^{R_128} r · f_R(r) dr 在截断 Pareto 下等价于 E[R | R ≤ R_12

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N57

## Claim

Prob_Coverage_128 的分子 ∫_{0}^{R_128} r · f_R(r) dr 在截断 Pareto 下等价于 E[R | R ≤ R_128] * P(R ≤ R_128) * E[R]_truncated；若 R_128 远小于 r_max=1e6，则 P(R ≤ R_128) ≈ 1 - (r_min/R_128)^{β-1} ≈ 1 - (1/R_128)^{-0.1}，需代入 R_128 具体值计算。

## Corrected Claim

Prob_Coverage_128 的分子 ∫_{0}^{R_128} r · f_R(r) dr 在截断 Pareto 下等价于 E[R | R ≤ R_128] * P(R ≤ R_128)；若 R_128 远小于 r_max=1e6，则 P(R ≤ R_128) ≈ 1 - (r_min/R_128)^{β-1}，需代入 R_128 具体值计算。

## Evidence

[质询]公式推导存在量纲和逻辑错误：∫ r·f_R(r)dr 是截断期望 E[R·1_{R≤R_128}]，其正确表达式应为 E[R|R≤R_128] * P(R≤R_128)，而非再乘以 E[R]_truncated（这会导致量纲变为 R^2 或数值错误）。此外，Pareto 分布的 CDF 公式 P(R≤x) = 1 - (x_min/x)^α 中，指数应为 α（通常记为 β 或 α），若 β-1 是指数，则需明确 β 的定义，且 (1/R_128)^{-0.1} 的写法易引起混淆（应为 (r_min/R_128)^{β-1}）。 | 先验知识/题面给定，逻辑校验发现公式错误：截断期望的积分形式不等于 E[R|R≤R_128] * P(R≤R_128) * E[R]_truncated，而是前者等于后两者之积（无第三个因子）。
