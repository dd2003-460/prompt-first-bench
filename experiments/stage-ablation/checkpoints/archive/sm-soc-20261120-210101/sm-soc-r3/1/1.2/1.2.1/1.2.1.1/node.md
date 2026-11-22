# N136: 共享随机源：卖家决策噪声 ε_seller 的基础分布，ε_seller ~ N(0, σ_seller²)，其中 σ_seller = σ_base * ex

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34

## Claim

共享随机源：卖家决策噪声 ε_seller 的基础分布，ε_seller ~ N(0, σ_seller²)，其中 σ_seller = σ_base * exp(-k * Experience_years)，σ_base = 0.15 * μ_price，k = 0.1，即每增加1年交易经验，噪声标准差降低10%。

## Corrected Claim

共享随机源：卖家决策噪声 ε_seller 的基础分布，ε_seller ~ N(0, σ_seller²)，其中 σ_seller = σ_base * exp(-k * Experience_years)，σ_base = 0.15 * μ_price，k = 0.1，即每增加1年交易经验，噪声标准差降低10%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，量纲一致（噪声标准差与价格均值同量纲），指数衰减模型在经济学/行为学模型中常见且逻辑自洽。

## Search Query

seller pricing noise experience effect exponential decay
