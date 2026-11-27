# N199: 偏度 γ_skew=0.8 对应的具体分布族假设及其参数映射：例如若假设服从Pearson Type III (Gamma) 分布，则形状参数 shape α 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N56

## Claim

偏度 γ_skew=0.8 对应的具体分布族假设及其参数映射：例如若假设服从Pearson Type III (Gamma) 分布，则形状参数 shape α = (2/γ_skew)^2 = 6.25，尺度参数 scale = σ/√α，此参数化是后续计算尾部概率的基础。

## Corrected Claim

偏度 γ_skew=0.8 对应的具体分布族假设及其参数映射：例如若假设服从Pearson Type III (Gamma) 分布，则形状参数 shape α = (2/γ_skew)^2 = 6.25，尺度参数 scale = σ/√α，此参数化是后续计算尾部概率的基础。

## Evidence

先验知识/题面给定，逻辑校验通过：Gamma分布偏度公式为2/√α，代入γ=0.8得α=6.25，推导正确
