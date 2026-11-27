# N339: 15% 流失率的置信区间验证：通过蒙特卡洛模拟 10,000 次，结合参数不确定性（β1, Activity 分布），计算流失率的 95% 置信区间；若区间不包

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

15% 流失率的置信区间验证：通过蒙特卡洛模拟 10,000 次，结合参数不确定性（β1, Activity 分布），计算流失率的 95% 置信区间；若区间不包含 15%，则需修正预测值或标记假设失效。

## Corrected Claim

15% 流失率的置信区间验证：通过蒙特卡洛模拟 10,000 次，结合参数不确定性（β1, Activity 分布），计算流失率的 95% 置信区间；若区间不包含 15%，则需修正预测值或标记假设失效。

## Evidence

先验知识/题面给定，逻辑校验通过：蒙特卡洛模拟是处理参数不确定性并计算置信区间的标准统计方法，10,000次迭代在计算上可行且能收敛，逻辑自洽。

## Search Query

monte carlo simulation churn rate confidence interval uncertainty analysis
