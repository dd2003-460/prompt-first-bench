# N202: 工作点A（高价格敏感度/低噪声）：定义价格敏感型点击率 CTR_price = f(P_ask/P_market)，基准值 CTR_price_base = 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

工作点A（高价格敏感度/低噪声）：定义价格敏感型点击率 CTR_price = f(P_ask/P_market)，基准值 CTR_price_base = 1.5% (假设基准CTR 2.5%中的60%为价格敏感)，弹性系数 ε_ctr_price = ∂ln(CTR_price)/∂ln(P_ask) ≈ -1.2 (基于Cobb-Douglas近似)，用于量化真实需求对价格的直接响应。

## Corrected Claim

工作点A（高价格敏感度/低噪声）：定义价格敏感型点击率 CTR_price = f(P_ask/P_market)，基准值 CTR_price_base = 1.5% (假设基准CTR 2.5%中的60%为价格敏感)，弹性系数 ε_ctr_price = ∂ln(CTR_price)/∂ln(P_ask) ≈ -1.2 (基于Cobb-Douglas近似)，用于量化真实需求对价格的直接响应。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

used goods marketplace price elasticity of click-through rate
