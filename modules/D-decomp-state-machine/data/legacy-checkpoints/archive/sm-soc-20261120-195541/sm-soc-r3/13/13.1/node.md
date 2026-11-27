# N211: 卖家收益下降幅度 ΔU_S 的 95% 置信区间计算：基于 N42 公式，ΔU_S_CI = [ΔU_S_hat - 1.96 * SE(ΔU_S), ΔU_S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

卖家收益下降幅度 ΔU_S 的 95% 置信区间计算：基于 N42 公式，ΔU_S_CI = [ΔU_S_hat - 1.96 * SE(ΔU_S), ΔU_S_hat + 1.96 * SE(ΔU_S)]，其中 SE(ΔU_S) 需通过历史价格弹性 ε_price 的方差传播计算，SE(ΔU_S) = |P_ask - P_ask'| * Q_base * SE(ε_price) / (ε_price * P_ask)

## Corrected Claim

卖家收益下降幅度 ΔU_S 的 95% 置信区间计算：基于 N42 公式，ΔU_S_CI = [ΔU_S_hat - 1.96 * SE(ΔU_S), ΔU_S_hat + 1.96 * SE(ΔU_S)]，其中 SE(ΔU_S) 需通过历史价格弹性 ε_price 的方差传播计算，SE(ΔU_S) = |P_ask - P_ask'| * Q_base * SE(ε_price) / (ε_price * P_ask)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

confidence interval for revenue loss under price intervention with elasticity uncertainty
