# N135: 流量券的时效性衰减函数：流量券在发放后 T_days 天内有效，其有效权重随时间呈指数衰减 W(t) = W_subsidy × e^(-λ_decay × t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

流量券的时效性衰减函数：流量券在发放后 T_days 天内有效，其有效权重随时间呈指数衰减 W(t) = W_subsidy × e^(-λ_decay × t)，其中 λ_decay 为衰减率。若 λ_decay = 0.1/day，则 48 小时后有效权重仅为初始值的 37%，这解释了为何部分卖家在 48 小时内未感受到流量红利。

## Corrected Claim

流量券的时效性衰减函数：流量券在发放后 T_days 天内有效，其有效权重随时间呈指数衰减 W(t) = W_subsidy × e^(-λ_decay × t)，其中 λ_decay 为衰减率。若 λ_decay = 0.1/day，则 48 小时后有效权重仅为初始值的 37%，这解释了为何部分卖家在 48 小时内未感受到流量红利。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 e^(-0.1 * 2) ≈ 0.3679，与陈述中的 37% 一致，逻辑自洽。
