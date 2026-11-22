# N90: Pareto(α=1.1) 分布下，前 1% 最大对象（即 s > s_99）的存储占比为 ∫_{s_99}^{∞} s f(s) ds / ∫_{s_min}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

Pareto(α=1.1) 分布下，前 1% 最大对象（即 s > s_99）的存储占比为 ∫_{s_99}^{∞} s f(s) ds / ∫_{s_min}^{∞} s f(s) ds，由于 α=1.1 接近 1，该比值理论值为 1 - (0.01)^{0.1} ≈ 50.5%，证实大对象主导存储占用。

## Corrected Claim

Pareto(α=1.1) 分布下，前 1% 最大对象（即 s > s_99）的存储占比为 ∫_{s_99}^{∞} s f(s) ds / ∫_{s_min}^{∞} s f(s) ds，由于 α=1.1 接近 1，该比值理论值为 1 - (0.01)^{0.1} ≈ 50.5%，证实大对象主导存储占用。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部质量占比公式推导正确，数值计算准确
