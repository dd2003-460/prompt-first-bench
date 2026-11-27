# N74: λ 对卖家保留价格 P_reserve 的传导弹性：基于前景理论，P_reserve = C_acq + (λ-1)*C_acq*(1 - Prob(Deal)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

λ 对卖家保留价格 P_reserve 的传导弹性：基于前景理论，P_reserve = C_acq + (λ-1)*C_acq*(1 - Prob(Deal))，需计算 ∂P_reserve/∂λ = C_acq*(1 - Prob(Deal))，以量化当 λ 从 2.25 变动至 2.40 时，卖家心理底价的上移幅度及其对成交概率 Prob(Deal) 的边际抑制作用。

## Corrected Claim

λ 对卖家保留价格 P_reserve 的传导弹性：基于前景理论，P_reserve = C_acq + (λ-1)*C_acq*(1 - Prob(Deal))，需计算 ∂P_reserve/∂λ = C_acq*(1 - Prob(Deal))，以量化当 λ 从 2.25 变动至 2.40 时，卖家心理底价的上移幅度及其对成交概率 Prob(Deal) 的边际抑制作用。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_reserve = C_acq + (λ-1)*C_acq*(1 - Prob(Deal)) 中，对 λ 求偏导数 ∂P_reserve/∂λ 确实等于 C_acq*(1 - Prob(Deal))，数学推导自洽，量纲合理。
