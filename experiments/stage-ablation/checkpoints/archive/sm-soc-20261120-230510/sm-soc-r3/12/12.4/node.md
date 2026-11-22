# N320: 二手非标品类目特异性修正系数：不同品类（如数码 vs 服饰）的 σ_random/σ_total 比例差异显著，需基于历史咨询数据回归计算各品类的噪声占比 β_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N113

## Claim

二手非标品类目特异性修正系数：不同品类（如数码 vs 服饰）的 σ_random/σ_total 比例差异显著，需基于历史咨询数据回归计算各品类的噪声占比 β_category，典型值 β_digital ≈ 0.3, β_fashion ≈ 0.5 [待核验]。

## Corrected Claim

二手非标品类目特异性修正系数：不同品类的 σ_random/σ_total 比例存在差异，需基于历史咨询数据回归计算各品类的噪声占比 β_category。通常服饰类目的噪声占比高于数码类目，具体数值需根据实际数据分布确定。

## Evidence

[质询]具体数值（β_digital ≈ 0.3, β_fashion ≈ 0.5）缺乏公开权威数据支持，属于特定业务场景下的经验估计值，不同平台或数据集下可能差异巨大，存在将局部经验泛化为通用典型值的风险。 | 经验事实，逻辑自洽（服饰非标程度高于数码，噪声占比更高符合直觉）但缺来源支持，且检索无可用来源。

## Search Query

category specific noise ratio digital vs fashion second-hand market empirical study
