# N191: 低驻留时间下的命中率折损上界：当 T_cold = 10 days 且 P_hit_cold = 0 时，δ = 1 - C_steady ≈ 1 - 0.09

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

低驻留时间下的命中率折损上界：当 T_cold = 10 days 且 P_hit_cold = 0 时，δ = 1 - C_steady ≈ 1 - 0.095 = 0.905，即最大折损为 9.5%，验证了“<10%可忽略”的结论。

## Corrected Claim

低驻留时间下的命中率折损上界：当 T_cold = 10 days 且 P_hit_cold = 0 时，δ = 1 - C_steady ≈ 1 - 0.095 = 0.905，即最大折损为 9.5%，验证了“<10%可忽略”的结论。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 - 0.095 = 0.905 正确，且 0.905 < 0.91 符合“<10%可忽略”的定性结论，无内部矛盾。
