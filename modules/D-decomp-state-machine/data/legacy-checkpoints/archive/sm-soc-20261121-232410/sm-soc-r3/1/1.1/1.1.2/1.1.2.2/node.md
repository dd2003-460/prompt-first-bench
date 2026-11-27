# N97: k_anchor分布的重尾性Kurtosis检验：若Kurtosis > 3（尖峰厚尾），则标准误SE=0.005可能被低估，导致t统计量虚高；需计算样本Kur

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

k_anchor分布的重尾性Kurtosis检验：若Kurtosis > 3（尖峰厚尾），则标准误SE=0.005可能被低估，导致t统计量虚高；需计算样本Kurtosis，若>5则改用Bootstrap方法重新估计μ的置信区间。

## Corrected Claim

k_anchor分布的重尾性Kurtosis检验：若Kurtosis > 3（尖峰厚尾），则标准误SE=0.005可能被低估，导致t统计量虚高；需计算样本Kurtosis，若>5则改用Bootstrap方法重新估计μ的置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过：Kurtosis>3确实指示厚尾分布，可能导致基于正态假设的标准误低估，Bootstrap是处理非正态分布置信区间的标准稳健方法，逻辑自洽。

## Search Query

kurtosis test price anchor distribution bootstrap
