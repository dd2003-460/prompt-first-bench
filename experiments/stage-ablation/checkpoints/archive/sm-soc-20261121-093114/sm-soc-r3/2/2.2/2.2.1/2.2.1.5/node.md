# N152: 不确定性水平 σ_posterior 的衰减：σ_posterior = σ_prior * (1 - ρ_information)，其中 ρ_informat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

不确定性水平 σ_posterior 的衰减：σ_posterior = σ_prior * (1 - ρ_information)，其中 ρ_information 为信息获取效率系数（0-1），取决于买家是否查看了详情页、评论及卖家信用分；σ_posterior 直接决定买家对‘降价’信号的敏感度阈值，σ_posterior 越高，买家越倾向于将降价解读为随机噪声而非缺陷信号。

## Corrected Claim

不确定性水平 σ_posterior 的衰减：σ_posterior = σ_prior * (1 - ρ_information)，其中 ρ_information 为信息获取效率系数（0-1），取决于买家是否查看了详情页、评论及卖家信用分；σ_posterior 直接决定买家对‘降价’信号的敏感度阈值，σ_posterior 越高，买家越倾向于将降价解读为随机噪声而非缺陷信号。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

posterior uncertainty reduction information acquisition efficiency Bayesian model
