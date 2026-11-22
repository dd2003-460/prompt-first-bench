# N144: S_buyer 的置信区间构造：利用 Delta Method 计算 S_buyer = (ΔUtility_lost / ΔTime_spent) 的标准误 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

S_buyer 的置信区间构造：利用 Delta Method 计算 S_buyer = (ΔUtility_lost / ΔTime_spent) 的标准误 SE(S_buyer)，并构建 95% 置信区间 [S_buyer - 1.96*SE, S_buyer + 1.96*SE]，若下限 > 0.5 则确认买家敏感度显著高于阈值，支持买家被动接受高挂价的假设。

## Corrected Claim

S_buyer 的置信区间构造：利用 Delta Method 计算 S_buyer = (ΔUtility_lost / ΔTime_spent) 的标准误 SE(S_buyer)，并构建 95% 置信区间 [S_buyer - 1.96*SE, S_buyer + 1.96*SE]，若下限 > 0.5 则确认买家敏感度显著高于阈值，支持买家被动接受高挂价的假设。

## Evidence

先验知识/题面给定，逻辑校验通过：Delta Method 是计算非线性函数（如比率）标准误的标准统计方法，基于正态近似构建 95% 置信区间（±1.96*SE）符合统计学原理，逻辑自洽。

## Search Query

delta method confidence interval for ratio of two random variables
