# N60: 成交概率骤降阈值的函数形式：定义成交概率 P(deal) = ∫[P_list, ∞) φ((x-μ)/σ) dx。当 P_list = μ + kσ 时，P(

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

成交概率骤降阈值的函数形式：定义成交概率 P(deal) = ∫[P_list, ∞) φ((x-μ)/σ) dx。当 P_list = μ + kσ 时，P(deal) = 1 - Φ(k)。若 k > 2 (即 δ > 2σ/μ)，P(deal) < 2.28%。若 k = 2.5，P(deal) < 0.62%。'骤降'的量化定义为边际成交概率 dP(deal)/dk < -0.5% per 1σ unit。

## Corrected Claim

成交概率骤降阈值的函数形式：定义成交概率 P(deal) = ∫[P_list, ∞) φ((x-μ)/σ) dx。当 P_list = μ + kσ 时，P(deal) = 1 - Φ(k)。若 k > 2 (即 δ > 2σ/μ)，P(deal) < 2.28%。若 k = 2.5，P(deal) < 0.62%。'骤降'的量化定义为边际成交概率 dP(deal)/dk < -0.5% per 1σ unit。

## Evidence

先验知识/题面给定，逻辑校验通过：标准正态分布尾部概率数值准确（k=2时1-Φ(2)≈2.28%，k=2.5时1-Φ(2.5)≈0.62%），边际概率定义符合数学逻辑。
