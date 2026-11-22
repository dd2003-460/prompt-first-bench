# N197: Gaussian Copula 在 ρ=-0.3 下计算边缘概率时的数值积分截断误差：积分区间 [0,1]^2 在 u 或 v < 10^-6 时，被积函数梯度

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Gaussian Copula 在 ρ=-0.3 下计算边缘概率时的数值积分截断误差：积分区间 [0,1]^2 在 u 或 v < 10^-6 时，被积函数梯度剧烈变化，若使用标准 Simpson 积分，相对误差可能超过 10%，需采用自适应积分或解析边界修正。

## Corrected Claim

Gaussian Copula 在 ρ=-0.3 下计算边缘概率时的数值积分截断误差：积分区间 [0,1]^2 在 u 或 v < 10^-6 时，被积函数梯度剧烈变化，若使用标准 Simpson 积分，相对误差可能超过 10%，需采用自适应积分或解析边界修正。

## Evidence

先验知识/题面给定，逻辑校验通过
