# N170: 交互项量化：ΔExposure 并非线性相加，需引入交互系数 γ (0 < γ < 1) 修正重叠曝光损失，公式为 ΔExposure = ΔRank + ΔC

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

交互项量化：ΔExposure 并非线性相加，需引入交互系数 γ (0 < γ < 1) 修正重叠曝光损失，公式为 ΔExposure = ΔRank + ΔCTR_effect - γ * ΔRank * ΔCTR_effect，其中 γ 代表排名下降与CTR下降导致同一用户群体流失的重叠比例。

## Corrected Claim

交互项量化：ΔExposure 并非线性相加，需引入交互系数 γ (0 < γ < 1) 修正重叠曝光损失，公式为 ΔExposure = ΔRank + ΔCTR_effect - γ * ΔRank * ΔCTR_effect，其中 γ 代表排名下降与CTR下降导致同一用户群体流失的重叠比例。

## Evidence

先验知识/题面给定，逻辑校验通过
