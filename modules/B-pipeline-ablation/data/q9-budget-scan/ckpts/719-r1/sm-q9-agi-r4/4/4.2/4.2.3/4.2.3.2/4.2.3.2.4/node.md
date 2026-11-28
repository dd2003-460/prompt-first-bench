# N611: FCR_0.7的95%置信区间计算公式：CI_95 = mean(FCR) ± t_{0.025, df=9} * (std(FCR) / sqrt(10))，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

FCR_0.7的95%置信区间计算公式：CI_95 = mean(FCR) ± t_{0.025, df=9} * (std(FCR) / sqrt(10))，其中df=9（n-1），t临界值约为2.262，std为10次实验中FCR的样本标准差

## Corrected Claim

FCR_0.7的95%置信区间计算公式：CI_95 = mean(FCR) ± t_{0.025, df=9} * (std(FCR) / sqrt(10))，其中df=9（n-1），t临界值约为2.262，std为10次实验中FCR的样本标准差

## Evidence

先验知识/题面给定，逻辑校验通过：基于中心极限定理和t分布定义，自由度df=n-1=9，t_{0.025,9}≈2.262，公式结构正确
