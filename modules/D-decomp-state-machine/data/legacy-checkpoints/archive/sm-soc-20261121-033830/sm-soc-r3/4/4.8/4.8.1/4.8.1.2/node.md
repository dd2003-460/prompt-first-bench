# N288: 总平方和 SS_tot 的参考基准：SS_tot = Σ (f_obs(P_i) - f_mean)² * w_i，其中 f_mean 为观测分布的均值或中位数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

总平方和 SS_tot 的参考基准：SS_tot = Σ (f_obs(P_i) - f_mean)² * w_i，其中 f_mean 为观测分布的均值或中位数；需验证 f_mean 是否受极端高价离群点影响，若影响显著，应改用鲁棒统计量（如中位数）作为基准以反映典型定价偏差。

## Corrected Claim

总平方和 SS_tot 的参考基准：SS_tot = Σ (f_obs(P_i) - f_mean)² * w_i，其中 f_mean 为观测分布的均值或中位数；需验证 f_mean 是否受极端高价离群点影响，若影响显著，应改用鲁棒统计量（如中位数）作为基准以反映典型定价偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：加权总平方和公式定义正确，且指出均值受离群点影响需改用中位数符合统计学鲁棒性原则。

## Search Query

total sum of squares robust baseline median vs mean for density
