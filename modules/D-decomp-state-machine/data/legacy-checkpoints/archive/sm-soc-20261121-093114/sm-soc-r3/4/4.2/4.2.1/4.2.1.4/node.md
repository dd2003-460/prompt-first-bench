# N177: 建议价偏差的系统性偏误项：ε = |P_suggest - P_equilibrium| 不仅包含随机噪声，还包含系统性偏误 Bias_suggest = β_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N55

## Claim

建议价偏差的系统性偏误项：ε = |P_suggest - P_equilibrium| 不仅包含随机噪声，还包含系统性偏误 Bias_suggest = β_bias * (P_suggest - P_market_median)，需量化 β_bias 以区分随机误差与算法倾向性偏差。

## Corrected Claim

建议价偏差的系统性偏误项：ε = |P_suggest - P_equilibrium| 不仅包含随机噪声，还包含系统性偏误 Bias_suggest = β_bias * (P_suggest - P_market_median)，需量化 β_bias 以区分随机误差与算法倾向性偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
