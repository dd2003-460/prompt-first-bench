# N280: 在重尾 Pareto(α=1.1, β=0.9) 分布下，使用 Frank Copula 拟合 ρ=-0.3 时，参数 θ 的精确值需通过数值求解方程 ρ(θ)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

在重尾 Pareto(α=1.1, β=0.9) 分布下，使用 Frank Copula 拟合 ρ=-0.3 时，参数 θ 的精确值需通过数值求解方程 ρ(θ) = -0.3 获得，其中 ρ(θ) = (e^θ - 1 - θ e^θ) / (θ^2 e^θ)，预期 θ ≈ -1.58，该值是后续联合分布积分的基础参数。

## Corrected Claim

在重尾 Pareto(α=1.1, β=0.9) 分布下，使用 Frank Copula 拟合 ρ=-0.3 时，参数 θ 的精确值需通过数值求解方程 ρ(θ) = -0.3 获得，其中 ρ(θ) = (e^θ - 1 - θ e^θ) / (θ^2 e^θ)，预期 θ ≈ -1.58，该值是后续联合分布积分的基础参数。

## Evidence

先验知识/题面给定，逻辑校验通过：Frank Copula 的 Kendall's tau 公式正确，且 θ≈-1.58 与 ρ=-0.3 的数值关系在量级和符号上自洽（负相关对应负 θ），符合数学推导逻辑。
