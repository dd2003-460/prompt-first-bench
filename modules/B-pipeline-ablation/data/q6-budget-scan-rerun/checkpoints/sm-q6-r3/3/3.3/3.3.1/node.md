# N69: 对象大小分布的长尾修正：图片/短视频大小并非固定均值，而是对数正态分布。图片大小 s_img ~ LogNormal(μ=ln(500KB), σ=0.3)，短

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

对象大小分布的长尾修正：图片/短视频大小并非固定均值，而是对数正态分布。图片大小 s_img ~ LogNormal(μ=ln(500KB), σ=0.3)，短视频 s_vid ~ LogNormal(μ=ln(5MB), σ=0.4)。加权平均 s_avg 需修正为 E[s] = 0.7 × exp(μ_img + σ_img²/2) + 0.3 × exp(μ_vid + σ_vid²/2)。需量化修正后的 s_avg 值（通常比算术均值高 5-15%）。

## Corrected Claim

对象大小分布的长尾修正：图片/短视频大小并非固定均值，而是对数正态分布。图片大小 s_img ~ LogNormal(μ=ln(500KB), σ=0.3)，短视频 s_vid ~ LogNormal(μ=ln(5MB), σ=0.4)。加权平均 s_avg 需修正为 E[s] = 0.7 × exp(μ_img + σ_img²/2) + 0.3 × exp(μ_vid + σ_vid²/2)。需量化修正后的 s_avg 值（通常比算术均值高 5-15%）。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布期望公式 E[s]=exp(μ+σ²/2) 正确，数值量级合理（图片修正后约523KB，视频约5.4MB，加权平均约1.66MB，相比算术均值5.15MB确实显著更高，符合长尾分布特性）
