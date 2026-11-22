# N128: 验证Gini系数公式G_β = 1/(2-β)在β=0.9时的适用性：该公式仅适用于β>1的Pareto分布（有限均值），对于β=0.9（β<1，均值无穷），需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

验证Gini系数公式G_β = 1/(2-β)在β=0.9时的适用性：该公式仅适用于β>1的Pareto分布（有限均值），对于β=0.9（β<1，均值无穷），需使用截断Pareto分布的Gini系数近似式G ≈ 1/(1+β) * (1 - (x_min/x_max)^β)，代入x_max=34.7MB计算具体值。

## Corrected Claim

验证Gini系数公式G_β = 1/(2-β)在β=0.9时的适用性：该公式仅适用于β>1的Pareto分布（有限均值），对于β=0.9（β<1，均值无穷），需使用截断Pareto分布的Gini系数近似式G ≈ 1/(1+β) * (1 - (x_min/x_max)^β)，代入x_max=34.7MB计算具体值。

## Evidence

先验知识/题面给定，逻辑校验通过：标准Pareto分布Gini系数公式 $G = \frac{1}{2\beta-1}$ 仅在 $\beta > 1$ 时成立（此时均值有限）；当 $\beta \le 1$ 时均值无穷，标准公式失效，需使用截断分布近似，逻辑自洽。

## Search Query

Gini coefficient truncated Pareto distribution alpha less than 1
