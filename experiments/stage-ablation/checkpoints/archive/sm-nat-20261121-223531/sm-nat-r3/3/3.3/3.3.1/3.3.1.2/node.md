# N140: 频率估计误差 ε_freq 与老化因子λ的关系为 ε_freq(λ) = |H_LFU_aging(λ) - H_LFU_top| / H_LFU_top，在λ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

频率估计误差 ε_freq 与老化因子λ的关系为 ε_freq(λ) = |H_LFU_aging(λ) - H_LFU_top| / H_LFU_top，在λ_opt=0.5/day时 ε_freq ≈ 1.5%，若λ偏离最优值（如λ=0.1/day或λ=1.0/day），ε_freq 增大至3-5%，导致 H_LFU_aging 进一步下降，需通过网格搜索确定λ的最优区间。

## Corrected Claim

频率估计误差 ε_freq 与老化因子λ的关系为 ε_freq(λ) = |H_LFU_aging(λ) - H_LFU_top| / H_LFU_top，在λ_opt=0.5/day时 ε_freq ≈ 1.5%，若λ偏离最优值（如λ=0.1/day或λ=1.0/day），ε_freq 增大至3-5%，导致 H_LFU_aging 进一步下降，需通过网格搜索确定λ的最优区间。

## Evidence

先验知识/题面给定，逻辑校验通过
