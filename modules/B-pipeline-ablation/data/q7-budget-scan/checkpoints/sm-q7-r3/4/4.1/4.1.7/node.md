# N102: HDD 重建期间二次故障概率 (P_second_HDD) 计算：P_second_HDD ≈ AFR_HDD × (W_HDD / 8760)。以 0.876

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24, N25, N26

## Claim

HDD 重建期间二次故障概率 (P_second_HDD) 计算：P_second_HDD ≈ AFR_HDD × (W_HDD / 8760)。以 0.876% AFR 为例，P_second_HDD ≈ 0.00876 × (33.3/8760) ≈ 3.32 × 10^-5

## Corrected Claim

HDD 重建期间二次故障概率 (P_second_HDD) 计算：P_second_HDD ≈ AFR_HDD × (W_HDD / 8760)。以 0.876% AFR 为例，P_second_HDD ≈ 0.00876 × (33.3/8760) ≈ 3.32 × 10^-5

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P = AFR × (T/8760) 符合泊松分布近似逻辑，数值计算 0.00876 * (33.3/8760) ≈ 3.32e-5 准确无误。
