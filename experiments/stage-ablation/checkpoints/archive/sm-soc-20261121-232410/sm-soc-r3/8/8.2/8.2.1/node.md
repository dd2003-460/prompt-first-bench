# N218: CVR_stable 的置信区间计算：CVR = Clicks / Impressions，假设 Impressions = 1000, Clicks = 12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

CVR_stable 的置信区间计算：CVR = Clicks / Impressions，假设 Impressions = 1000, Clicks = 120，则 CVR = 0.12；95% 置信区间为 CVR ± 1.96 * sqrt(CVR*(1-CVR)/n)，即 0.12 ± 1.96 * sqrt(0.12*0.88/1000) ≈ 0.12 ± 0.019，范围 [0.101, 0.139]，与题面 [0.08, 0.16] 存在偏差，需校准样本量 n 或波动率。

## Corrected Claim

CVR_stable 的置信区间计算：CVR = Clicks / Impressions，假设 Impressions = 1000, Clicks = 120，则 CVR = 0.12；95% 置信区间为 CVR ± 1.96 * sqrt(CVR*(1-CVR)/n)，即 0.12 ± 1.96 * sqrt(0.12*0.88/1000) ≈ 0.12 ± 0.019，范围 [0.101, 0.139]，与题面 [0.08, 0.16] 存在偏差，需校准样本量 n 或波动率。

## Evidence

先验知识/题面给定，逻辑校验通过：基于二项分布正态近似公式计算，sqrt(0.12*0.88/1000)≈0.01026，1.96*0.01026≈0.0201，区间[0.100, 0.140]与陈述中[0.101, 0.139]在舍入误差范围内一致，且正确指出了与题面给定区间的偏差。

## Search Query

conversion rate confidence interval calculation binomial proportion
