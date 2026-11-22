# N238: P(ΔT_deal < 0 | Data) 的贝叶斯后验概率：基于净周期判据（N47），该概率为 t 分布或正态分布的累积分布函数值，P(ΔT_deal < 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

P(ΔT_deal < 0 | Data) 的贝叶斯后验概率：基于净周期判据（N47），该概率为 t 分布或正态分布的累积分布函数值，P(ΔT_deal < 0) = Φ(-|ΔT_deal| / SE_ΔT)，其中 SE_ΔT 为周期差的标准误。

## Corrected Claim

P(ΔT_deal < 0 | Data) 的贝叶斯后验概率：基于净周期判据（N47），该概率为 t 分布或正态分布的累积分布函数值，P(ΔT_deal < 0) = Φ(-|ΔT_deal| / SE_ΔT)，其中 SE_ΔT 为周期差的标准误。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态或t分布的对称性，P(ΔT < 0) 确实等于分布左尾概率，即 Φ(-|ΔT|/SE) 或 t 分布对应分位数，公式推导符合统计学第一性原理。

## Search Query

bayesian posterior probability of difference being negative
