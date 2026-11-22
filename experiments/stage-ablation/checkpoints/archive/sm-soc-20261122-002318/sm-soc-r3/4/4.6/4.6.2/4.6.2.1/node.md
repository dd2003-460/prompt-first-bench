# N205: 搜寻次数变化量 (N_new - N_old) 的估算：假设信息展示使买家验证同类商品的价格分布方差降低 50% (σ_new = 0.5 * σ_old)，根

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

搜寻次数变化量 (N_new - N_old) 的估算：假设信息展示使买家验证同类商品的价格分布方差降低 50% (σ_new = 0.5 * σ_old)，根据搜索理论，所需样本量与方差成正比，故 N_new ≈ 0.5 * N_old；若基准 N_old = 5 次对比，则 N_new = 2.5 次，变化量 ΔN = -2.5。

## Corrected Claim

搜寻次数变化量 (N_new - N_old) 的估算：假设信息展示使买家验证同类商品的价格分布方差降低 50% (σ_new = 0.5 * σ_old)，根据搜索理论，所需样本量与方差成正比，故 N_new ≈ 0.5 * N_old；若基准 N_old = 5 次对比，则 N_new = 2.5 次，变化量 ΔN = -2.5。

## Evidence

先验知识/题面给定，逻辑校验通过：基于搜索理论中样本量与方差成正比的假设，数学推导 N_new = 0.5 * N_old 及 ΔN = -2.5 在逻辑上自洽且量级合理。
