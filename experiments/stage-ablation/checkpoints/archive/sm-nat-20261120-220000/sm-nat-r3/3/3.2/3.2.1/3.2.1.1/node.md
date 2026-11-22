# N105: 修正N37中的LogNormal参数定义：通常LogNormal分布由线性尺度下的均值μ_log和标准差σ_log定义。若t_refill ~ LogNorma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

修正N37中的LogNormal参数定义：通常LogNormal分布由线性尺度下的均值μ_log和标准差σ_log定义。若t_refill ~ LogNormal(μ_log=ln(5ms), σ_log=0.3)，则均值 E[t] = exp(μ_log + σ_log^2/2) ≈ 5.25ms。需明确μ=5ms是指中位数还是均值，若为中位数则公式不同。

## Corrected Claim

修正N37中的LogNormal参数定义：通常LogNormal分布由线性尺度下的均值μ_log和标准差σ_log定义。若t_refill ~ LogNormal(μ_log=ln(5ms), σ_log=0.3)，则均值 E[t] = exp(μ_log + σ_log^2/2) ≈ 5.25ms。需明确μ=5ms是指中位数还是均值，若为中位数则公式不同。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布均值公式 E[t] = exp(μ + σ²/2) 正确，数值计算 exp(ln(5) + 0.045) ≈ 5.228ms，与陈述中的 5.25ms 在合理精度范围内一致，且明确指出了中位数与均值的区别。
