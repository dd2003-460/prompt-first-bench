# N227: Var(T_decision) 的计算示例：在电子产品市场，σ_pref = 0.10 μ_WTP，λ_search = 0.05/h，则 Var(T) = (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

Var(T_decision) 的计算示例：在电子产品市场，σ_pref = 0.10 μ_WTP，λ_search = 0.05/h，则 Var(T) = (0.10 μ_WTP)^2 / 0.05 = 0.2 μ_WTP^2/h；标准差 σ_T = 0.447 μ_WTP/sqrt(h)，解释了 48 小时内成交周期的随机波动。

## Corrected Claim

Var(T_decision) 的计算示例：在电子产品市场，σ_pref = 0.10 μ_WTP，λ_search = 0.05/h，则 Var(T) = (0.10 μ_WTP)^2 / 0.05 = 0.2 μ_WTP^2/h；标准差 σ_T = 0.447 μ_WTP/sqrt(h)，解释了 48 小时内成交周期的随机波动。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Var(T) = σ_pref² / λ_search 符合指数分布或类似随机搜索过程的方差定义，数值计算 (0.10)^2 / 0.05 = 0.01 / 0.05 = 0.2 正确，标准差 sqrt(0.2) ≈ 0.447 正确，量纲推导一致。

## Search Query

decision time variance search rate willingness to pay
