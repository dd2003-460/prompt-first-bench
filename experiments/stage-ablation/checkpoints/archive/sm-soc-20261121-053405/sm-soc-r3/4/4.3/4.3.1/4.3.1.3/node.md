# N186: 工作点3（低置信高成本）：假设 θ_disclosure = 0.5（激进估计），λ_base = 0.05/h，Δt = 48h，则 P_consult = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N68

## Claim

工作点3（低置信高成本）：假设 θ_disclosure = 0.5（激进估计），λ_base = 0.05/h，Δt = 48h，则 P_consult = 1 - e^{-0.5×0.05×48} = 1 - e^{-1.2} ≈ 0.699。此工作点适用于平台完全黑箱且数据透明度低场景，置信度上限 0.75（基于 N74 修正），需额外 A/B 测试验证。

## Corrected Claim

工作点3（低置信高成本）：假设 θ_disclosure = 0.5（激进估计），λ_base = 0.05/h，Δt = 48h，则 P_consult = 1 - e^{-0.5×0.05×48} = 1 - e^{-1.2} ≈ 0.699。此工作点适用于平台完全黑箱且数据透明度低场景，置信度上限 0.75（基于 N74 修正），需额外 A/B 测试验证。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - e^(-1.2) ≈ 0.6988 与陈述中的 0.699 一致，量纲与逻辑自洽。
