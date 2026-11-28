# N318: 知识缺失率的置信区间计算：基于二项分布，在 100 题样本中，若 Correct_Count = k，则知识缺失率 p = 1 - k/100 的 95% 置信

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

知识缺失率的置信区间计算：基于二项分布，在 100 题样本中，若 Correct_Count = k，则知识缺失率 p = 1 - k/100 的 95% 置信区间为 [p - 1.96*sqrt(p(1-p)/100), p + 1.96*sqrt(p(1-p)/100)]，用于量化'模型不知道'这一结论的统计可靠性

## Corrected Claim

知识缺失率的置信区间计算：基于二项分布，在 100 题样本中，若 Correct_Count = k，则知识缺失率 p = 1 - k/100 的 95% 置信区间为 [p - 1.96*sqrt(p(1-p)/100), p + 1.96*sqrt(p(1-p)/100)]，用于量化'模型不知道'这一结论的统计可靠性

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

binomial proportion confidence interval Wilson score interval
