# N272: 修正公式中 exp(λ_rarity * max(0, D - 25%)) 项的边界检查：当 D = 40% 时，若 λ_rarity = 0.05，则修正因子

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

修正公式中 exp(λ_rarity * max(0, D - 25%)) 项的边界检查：当 D = 40% 时，若 λ_rarity = 0.05，则修正因子为 exp(0.05 * 15) ≈ 2.117，导致 CTR' 超过 C0，这在逻辑上是否成立需通过‘最大可能 CTR = 100%’进行截断验证，并计算截断前的理论 CTR' 值。

## Corrected Claim

修正公式中 exp(λ_rarity * max(0, D - 25%)) 项的边界检查：当 D = 40% 时，若 λ_rarity = 0.05，则修正因子为 exp(0.05 * 15) ≈ 2.117，导致 CTR' 超过 C0，这在逻辑上是否成立需通过‘最大可能 CTR = 100%’进行截断验证，并计算截断前的理论 CTR' 值。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 exp(0.05 * 15) ≈ 2.117 正确，且 CTR 截断逻辑符合概率上限约束
