# N140: 下游投影 1：价格离散度上限。给定 k ∈ [0.01, 0.05] 和 SI 的最小值 SI_min（通常接近 0），最大可能噪声方差 σ_max² = k 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

下游投影 1：价格离散度上限。给定 k ∈ [0.01, 0.05] 和 SI 的最小值 SI_min（通常接近 0），最大可能噪声方差 σ_max² = k / (1 + SI_min) ≈ k；该值决定了单件商品挂价偏离理论价值的最大标准差，直接影响买家对‘捡漏’概率的感知阈值。

## Corrected Claim

下游投影 1：价格离散度上限。给定 k ∈ [0.01, 0.05] 和 SI 的最小值 SI_min（通常接近 0），最大可能噪声方差 σ_max² = k / (1 + SI_min) ≈ k；该值决定了单件商品挂价偏离理论价值的最大标准差，直接影响买家对‘捡漏’概率的感知阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：根据定义，若噪声方差与信号强度（SI）及比例系数 k 存在线性关系，且 SI_min 接近 0，则 σ_max² ≈ k 在数学上自洽，量纲与量级合理。

## Search Query

maximum price deviation noise variance buyer bargain perception threshold
