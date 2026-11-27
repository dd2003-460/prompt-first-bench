# N168: 工作点2（中响应/中溢价）：当 v_high(t) 服从指数分布 v(t) = (1/τ) * exp(-t/τ) 且 P_high = 1.1 * P_med

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

工作点2（中响应/中溢价）：当 v_high(t) 服从指数分布 v(t) = (1/τ) * exp(-t/τ) 且 P_high = 1.1 * P_median 时，积分结果呈现最优性价比，需推导解析解 P(Sale) = λ_b / (λ_b + 1/τ) 并代入典型 τ 值。

## Corrected Claim

工作点2（中响应/中溢价）：当 v_high(t) 服从指数分布 v(t) = (1/τ) * exp(-t/τ) 且 P_high = 1.1 * P_median 时，积分结果呈现最优性价比，需推导解析解 P(Sale) = λ_b / (λ_b + 1/τ) 并代入典型 τ 值。

## Evidence

先验知识/题面给定，逻辑校验通过：在泊松过程与指数分布假设下，积分推导出的概率公式 P = λ_b / (λ_b + 1/τ) 符合数学推导逻辑，量纲与数值量级合理。

## Search Query

exponential response time sale probability analytical solution
