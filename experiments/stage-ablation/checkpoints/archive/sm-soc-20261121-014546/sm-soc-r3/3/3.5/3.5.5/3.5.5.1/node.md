# N264: 价格敏感度系数 γ_price 的估计公式：γ_price = -ln(1 - p_target) / ΔP_pct，其中 p_target 为基准价格下的成交

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

价格敏感度系数 γ_price 的估计公式：γ_price = -ln(1 - p_target) / ΔP_pct，其中 p_target 为基准价格下的成交概率（如 0.5），ΔP_pct 为价格偏离度（如 0.1），用于校准指数模型以匹配实际成交率。

## Corrected Claim

价格敏感度系数 γ_price 的估计公式：γ_price = -ln(1 - p_target) / ΔP_pct，其中 p_target 为基准价格下的成交概率（如 0.5），ΔP_pct 为价格偏离度（如 0.1），用于校准指数模型以匹配实际成交率。

## Evidence

先验知识/题面给定，逻辑校验通过
