# N437: RTX 3090 Ti 的能效比计算：基于 N373 的实测吞吐量 32.8 tokens/s 和 P_avg 245W (70% TDP)，能效比 = 32.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N147

## Claim

RTX 3090 Ti 的能效比计算：基于 N373 的实测吞吐量 32.8 tokens/s 和 P_avg 245W (70% TDP)，能效比 = 32.8 / 245 ≈ 0.134 tokens/s/W。N147 声称的 0.10-0.11 tokens/s/W 偏低，可能未考虑 INT4 量化带来的带宽效率提升或使用了更保守的效率系数。

## Corrected Claim

RTX 3090 Ti 的能效比计算：基于 N373 的实测吞吐量 32.8 tokens/s 和 P_avg 245W (70% TDP)，能效比 = 32.8 / 245 ≈ 0.134 tokens/s/W。N147 声称的 0.10-0.11 tokens/s/W 偏低，可能未考虑 INT4 量化带来的带宽效率提升或使用了更保守的效率系数。

## Evidence

先验知识/题面给定，逻辑校验通过：32.8/245≈0.134计算正确，量纲合理，且对N147偏差的解释符合INT4量化提升带宽效率的工程常识。
