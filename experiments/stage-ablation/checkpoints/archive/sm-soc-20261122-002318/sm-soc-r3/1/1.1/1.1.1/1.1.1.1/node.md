# N101: 卖家拒绝降价心理阈值公式 ΔP_refuse = λ * (P_ask - P_market) * (1 - w_tradeoff) 中的核心随机源：卖家对‘快

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34

## Claim

卖家拒绝降价心理阈值公式 ΔP_refuse = λ * (P_ask - P_market) * (1 - w_tradeoff) 中的核心随机源：卖家对‘快速成交时间价值’的权重 w_tradeoff，其服从 Beta(α_t, β_t) 分布，均值 E[w_tradeoff] = α_t / (α_t + β_t)，方差 Var(w_tradeoff) = (α_t β_t) / ((α_t + β_t)^2 (α_t + β_t + 1))。

## Corrected Claim

卖家拒绝降价心理阈值公式 ΔP_refuse = λ * (P_ask - P_market) * (1 - w_tradeoff) 中的核心随机源：卖家对‘快速成交时间价值’的权重 w_tradeoff，其服从 Beta(α_t, β_t) 分布，均值 E[w_tradeoff] = α_t / (α_t + β_t)，方差 Var(w_tradeoff) = (α_t β_t) / ((α_t + β_t)^2 (α_t + β_t + 1))。

## Evidence

先验知识/题面给定，逻辑校验通过：Beta分布的均值和方差公式符合标准数学定义，量纲与逻辑自洽。
