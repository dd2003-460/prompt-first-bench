# N97: 社区实测数据 (Reddit/GitHub) 的置信区间计算方法：当样本量 n>5 时，采用平均值 ± 1.96 * (标准差 / sqrt(n)) 作为 95

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

社区实测数据 (Reddit/GitHub) 的置信区间计算方法：当样本量 n>5 时，采用平均值 ± 1.96 * (标准差 / sqrt(n)) 作为 95% 置信区间；若标准差 > 20% 的平均值，则标记为 '高方差'，不可用于最终决策，需增加样本量至 n>10 或寻找更可控的测试环境。

## Corrected Claim

社区实测数据 (Reddit/GitHub) 的置信区间计算方法：当样本量 n>5 时，采用平均值 ± 1.96 * (标准差 / sqrt(n)) 作为 95% 置信区间；若标准差 > 20% 的平均值，则标记为 '高方差'，不可用于最终决策，需增加样本量至 n>10 或寻找更可控的测试环境。

## Evidence

先验知识/题面给定，逻辑校验通过
