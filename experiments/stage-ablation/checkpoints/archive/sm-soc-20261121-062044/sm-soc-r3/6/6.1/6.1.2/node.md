# N244: 工作点B（中信号/中噪声）：当基线咨询数 Inquiry_base 位于 [1, 5] 区间时，相对误差 σ_rel = 1/√Inquiry_base 显著放

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

工作点B（中信号/中噪声）：当基线咨询数 Inquiry_base 位于 [1, 5] 区间时，相对误差 σ_rel = 1/√Inquiry_base 显著放大（最大 100%），需采用贝叶斯收缩估计，将观测值向类目均值 μ_category 收缩，收缩强度 k = (1 - Inquiry_base/10) * 0.5，以平衡个体波动与群体趋势。

## Corrected Claim

工作点B（中信号/中噪声）：当基线咨询数 Inquiry_base 位于 [1, 5] 区间时，相对误差 σ_rel = 1/√Inquiry_base 显著放大（最大 100%），需采用贝叶斯收缩估计，将观测值向类目均值 μ_category 收缩，收缩强度 k = (1 - Inquiry_base/10) * 0.5，以平衡个体波动与群体趋势。

## Evidence

先验知识/题面给定，逻辑校验通过
