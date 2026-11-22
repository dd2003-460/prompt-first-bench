# N140: Gaussian Copula 下，对数大小 ln(s_i) 与对数排名 ln(i) 的标准化残差 z_i 满足 E[ln(s_i)|ln(i)] = μ_s 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53, N54, N55

## Claim

Gaussian Copula 下，对数大小 ln(s_i) 与对数排名 ln(i) 的标准化残差 z_i 满足 E[ln(s_i)|ln(i)] = μ_s - ρ * σ_s * (ln(i) - μ_i)/σ_i，其中 ρ=-0.3 导致头部对象（ln(i) 小）的 ln(s_i) 期望值比独立假设低 Δln_s = 0.3 * σ_s * (μ_i - ln(i_100))/σ_i。

## Corrected Claim

Gaussian Copula 下，对数大小 ln(s_i) 与对数排名 ln(i) 的标准化残差 z_i 满足 E[ln(s_i)|ln(i)] = μ_s - ρ * σ_s * (ln(i) - μ_i)/σ_i，其中 ρ=-0.3 导致头部对象（ln(i) 小）的 ln(s_i) 期望值比独立假设低 Δln_s = 0.3 * σ_s * (μ_i - ln(i_100))/σ_i。

## Evidence

先验知识/题面给定，逻辑校验通过：基于高斯Copula的线性回归性质，条件期望公式推导正确，且负相关系数导致头部（小排名）期望值降低的定性结论与数学推导一致。
