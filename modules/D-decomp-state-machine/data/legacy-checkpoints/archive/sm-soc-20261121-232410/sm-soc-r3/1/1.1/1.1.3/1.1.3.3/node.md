# N101: σ=0.05与平台算法噪声的交互效应：若平台算法引入的随机扰动σ_algo > 0.02，则总噪声σ_total = √(σ_market² + σ_algo²

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

σ=0.05与平台算法噪声的交互效应：若平台算法引入的随机扰动σ_algo > 0.02，则总噪声σ_total = √(σ_market² + σ_algo²) > 0.05，导致实际覆盖概率低于0.9544；需量化σ_algo（如通过A/B测试中算法随机化组的方差估计）。

## Corrected Claim

σ=0.05与平台算法噪声的交互效应：若平台算法引入的随机扰动σ_algo > 0.02，则总噪声σ_total = √(σ_market² + σ_algo²) > 0.05，导致实际覆盖概率低于0.9544；需量化σ_algo（如通过A/B测试中算法随机化组的方差估计）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于独立噪声源方差相加原理（σ_total² = σ_market² + σ_algo²），若σ_market=0.05且σ_algo>0.02，则σ_total>√(0.0025+0.0004)=√0.0029≈0.05385，确实大于0.05，导致正态分布下覆盖概率低于2σ对应的0.9544，推导自洽。

## Search Query

algorithm noise variance price anchor
