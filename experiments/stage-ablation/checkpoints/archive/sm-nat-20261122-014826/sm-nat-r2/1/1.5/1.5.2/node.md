# N37: 修正后命中率公式 H_LRU_actual 的推导：H_LRU_actual ≈ H_LRU_theoretical(C_eff) - H_LRU_theore

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

修正后命中率公式 H_LRU_actual 的推导：H_LRU_actual ≈ H_LRU_theoretical(C_eff) - H_LRU_theoretical(C)。利用 H ≈ 1 - (1-C/S)^(1/β')，计算 ΔH_corr = [1 - (1-C_eff/S)^(1/β')] - [1 - (1-C/S)^(1/β')]。代入 C=128GB, S=910GB, β'=0.9, C_eff=145GB，计算具体百分点增益。

## Corrected Claim

修正后命中率公式 H_LRU_actual 的推导：H_LRU_actual ≈ H_LRU_theoretical(C_eff) - H_LRU_theoretical(C)。利用 H ≈ 1 - (1-C/S)^(1/β')，计算 ΔH_corr = [1 - (1-C_eff/S)^(1/β')] - [1 - (1-C/S)^(1/β')]。代入 C=128GB, S=910GB, β'=0.9, C_eff=145GB，计算具体百分点增益。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合LRU缓存命中率模型的基本逻辑，数值代入量级合理（C_eff > C 导致命中率提升），无内部矛盾。
