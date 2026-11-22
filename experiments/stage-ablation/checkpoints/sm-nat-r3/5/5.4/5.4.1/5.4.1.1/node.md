# N241: 线性负相关 S_i = a - b * R_i 中参数 a 和 b 的确定：a 和 b 需满足 S_i > 0 且 R_i > 0，由 Pareto(α=1.1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

线性负相关 S_i = a - b * R_i 中参数 a 和 b 的确定：a 和 b 需满足 S_i > 0 且 R_i > 0，由 Pareto(α=1.1) 和 Pareto(β=0.9) 的矩条件确定，a = E[S] + b * E[R]，b = -ρ * σ_S / σ_R，其中 σ_S 和 σ_R 分别为大小和热度的标准差

## Corrected Claim

线性负相关 S_i = a - b * R_i 中参数 a 和 b 的确定：a 和 b 需满足 S_i > 0 且 R_i > 0，由 Pareto(α=1.1) 和 Pareto(β=0.9) 的矩条件确定，a = E[S] + b * E[R]，b = -ρ * σ_S / σ_R，其中 σ_S 和 σ_R 分别为大小和热度的标准差

## Evidence

先验知识/题面给定，逻辑校验通过：线性回归系数公式 b = -ρ * σ_S / σ_R 和截距 a = E[S] + b * E[R] 符合统计学定义，且满足正相关/负相关符号逻辑。
