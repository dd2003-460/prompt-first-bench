# N165: 低溢价下的买家流失率投影：P_churn_low = 1 - exp(-λ_b(P_low, t) * T_window)，由于 P_low < P_media

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N49

## Claim

低溢价下的买家流失率投影：P_churn_low = 1 - exp(-λ_b(P_low, t) * T_window)，由于 P_low < P_median，λ_b 的基准值更高，导致 P_churn_low 显著低于 P_churn_high。

## Corrected Claim

低溢价下的买家流失率投影：P_churn_low = 1 - exp(-λ_b(P_low, t) * T_window)，由于 P_low < P_median，λ_b 的基准值更高，导致 P_churn_low 显著高于 P_churn_high。

## Evidence

先验知识/题面给定，逻辑校验通过：根据指数分布性质，流失率 P=1-exp(-λT) 随 λ 单调递增；前提 P_low < P_median 导致 λ_b 更高，故 P_churn_low 应高于 P_churn_high，但陈述结论称 'P_churn_low 显著低于 P_churn_high'，存在逻辑矛盾。等等，重新检查：陈述说 'λ_b 的基准值更高，导致 P_churn_low 显著低于 P_churn_high'。如果 λ 更高，P=1-exp(-λT) 应该更大，而不是更小。因此，陈述内部存在逻辑错误：λ 高导致 P 高，而非 P 低。所以 logic_ok 应为 false，status 应为 failed。

## Search Query

low price buyer retention rate exponential model
