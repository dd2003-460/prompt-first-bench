# N166: 平台佣金随机收益投影 B_commission_noise：基于 ε ~ N(μ_ε, σ_ε²)，平台单笔佣金收入 r * P_deal 的方差 Var(B_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48

## Claim

平台佣金随机收益投影 B_commission_noise：基于 ε ~ N(μ_ε, σ_ε²)，平台单笔佣金收入 r * P_deal 的方差 Var(B_commission) = (r * σ_ε)²，代入 r=0.05, σ_ε=0.15*P_market，计算 Var(B_commission) = (0.0075 * P_market)²，用于评估平台收入波动性。

## Corrected Claim

平台佣金随机收益投影 B_commission_noise：基于 ε ~ N(μ_ε, σ_ε²)，平台单笔佣金收入 r * P_deal 的方差 Var(B_commission) = (r * σ_ε)²，代入 r=0.05, σ_ε=0.15*P_market，计算 Var(B_commission) = (0.0075 * P_market)²，用于评估平台收入波动性。

## Evidence

先验知识/题面给定，逻辑校验通过：方差公式 Var(aX) = a²Var(X) 应用正确，数值代入 (0.05 * 0.15)² = 0.0075² 计算无误。
