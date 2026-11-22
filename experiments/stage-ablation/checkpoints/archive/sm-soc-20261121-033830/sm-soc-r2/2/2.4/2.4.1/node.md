# N54: P(Sale|P_high, v_high) 的具体计算形式为条件概率积分：P(Sale|P_high, v_high) = ∫_0^∞ λ_b(P_high)

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N12

## Claim

P(Sale|P_high, v_high) 的具体计算形式为条件概率积分：P(Sale|P_high, v_high) = ∫_0^∞ λ_b(P_high) * e^(-λ_b(P_high)*t) * v_high(t) dt，其中 λ_b 为买家到达率，v_high(t) 为卖家响应概率密度函数。

## Corrected Claim

P(Sale|P_high, v_high) = ∫_0^∞ λ_b(P_high) * e^(-λ_b(P_high)*t) * S_v(t) dt，其中 S_v(t) 为卖家在时刻 t 之前未响应的生存函数（或 v_high(t) 为卖家在时刻 t 响应的条件概率密度，需明确量纲归一化）。

## Evidence

[质询]公式中 v_high(t) 被定义为'卖家响应概率密度函数'，但在积分形式 ∫ λ e^(-λt) v(t) dt 中，若 v(t) 是概率密度函数（PDF），其量纲为 1/时间，导致整个积分的量纲为 1/时间，而非概率（无量纲）；若 v(t) 是'在时刻 t 响应'的条件概率或生存函数，则不应称为'概率密度函数'。存在术语定义与数学量纲/逻辑不自洽的风险。 | 先验知识/题面给定，但逻辑校验发现量纲/定义矛盾：若 v_high(t) 为 PDF，积分结果非概率；若为概率，则不应称为 PDF。来源未覆盖，无法排除定义错误。
