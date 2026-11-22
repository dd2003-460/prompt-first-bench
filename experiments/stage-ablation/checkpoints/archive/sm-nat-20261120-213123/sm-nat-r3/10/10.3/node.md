# N78: 修正因子 B_corr / B_indep 的数值估算：B_corr ≈ B_indep * (1 + ρ * σ_logS * σ_logH) = B_ind

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

修正因子 B_corr / B_indep 的数值估算：B_corr ≈ B_indep * (1 + ρ * σ_logS * σ_logH) = B_indep * (1 - 0.3 * 0.828 * 1.425) = B_indep * (1 - 0.353) = 0.647 * B_indep。即负相关导致字节命中率下界降低约 35.3%，这是 LRU 策略在给定参数下的最大理论惩罚。

## Corrected Claim

修正因子 B_corr / B_indep 的数值估算：B_corr ≈ B_indep * (1 + ρ * σ_logS * σ_logH) = B_indep * (1 - 0.3 * 0.828 * 1.425) = B_indep * (1 - 0.353) = 0.647 * B_indep。即负相关导致字节命中率下界降低约 35.3%，这是 LRU 策略在给定参数下的最大理论惩罚。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.3 * 0.828 * 1.425 ≈ 0.353 正确，1 - 0.353 = 0.647 正确，推导逻辑自洽。

## Search Query

cache hit rate correlation correction factor numerical example
