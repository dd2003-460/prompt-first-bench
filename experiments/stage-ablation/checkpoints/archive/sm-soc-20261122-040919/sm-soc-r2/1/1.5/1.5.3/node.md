# N47: 咨询概率的柠檬市场效应：P(consult|price_drop) = P(consult|base) × (1-d) × exp(-γ×(P_drop - P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9

## Claim

咨询概率的柠檬市场效应：P(consult|price_drop) = P(consult|base) × (1-d) × exp(-γ×(P_drop - P_market_avg)/P_market_avg)，其中 γ 是买家对'异常低价'的惩罚系数（γ=0.5）；当 P_drop 低于市场均价 10% 时，exp(-0.5×(-0.1)) = 1.05，但 d=0.4 导致整体概率下降至 P(consult|base)×0.6×1.05

## Corrected Claim

咨询概率的柠檬市场效应：P(consult|price_drop) = P(consult|base) × (1-d) × exp(-γ×(P_drop - P_market_avg)/P_market_avg)，其中 γ 是买家对'异常低价'的惩罚系数（γ=0.5）；当 P_drop 低于市场均价 10% 时，exp(-0.5×(-0.1)) = 1.05，但 d=0.4 导致整体概率下降至 P(consult|base)×0.6×1.05

## Evidence

先验知识/题面给定，逻辑校验通过：公式中 exp(-0.5 * (-0.1)) = exp(0.05) ≈ 1.051，与陈述中的 1.05 一致；(1-d) = 1-0.4 = 0.6，乘积 0.6 * 1.05 = 0.63，逻辑自洽且数值量级合理。
