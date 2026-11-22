# N338: β_platform 的置信区间 [0.7, 1.0] 的构造：基于 Bootstrap 重抽样 1000 次，每次从均衡稳定性数据中随机抽样并重新估计 β_p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

β_platform 的置信区间 [0.7, 1.0] 的构造：基于 Bootstrap 重抽样 1000 次，每次从均衡稳定性数据中随机抽样并重新估计 β_platform，取 2.5% 和 97.5% 分位数作为置信区间边界；若区间不包含 0，则平台驱动效应显著。

## Corrected Claim

β_platform 的置信区间 [0.7, 1.0] 的构造：基于 Bootstrap 重抽样 1000 次，每次从均衡稳定性数据中随机抽样并重新估计 β_platform，取 2.5% 和 97.5% 分位数作为置信区间边界；若区间不包含 0，则平台驱动效应显著。

## Evidence

先验知识/题面给定，逻辑校验通过：Bootstrap 置信区间的标准构造方法即为重抽样后取分位数，且区间不包含 0 是判断系数显著性的标准统计准则，逻辑自洽且符合统计学原理。
