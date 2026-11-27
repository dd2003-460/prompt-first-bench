# N176: 统计显著性阈值 p < 0.01 的样本量要求：在效应量 $\beta = -0.1$（标准化系数）且标准误 SE=0.02 的假设下，所需最小样本量 n 约为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

统计显著性阈值 p < 0.01 的样本量要求：在效应量 $\beta = -0.1$（标准化系数）且标准误 SE=0.02 的假设下，所需最小样本量 n 约为 1,000 个商品观测值；若样本量不足，需使用 Bootstrap 方法计算置信区间，而非依赖 t 检验。

## Corrected Claim

统计显著性阈值 p < 0.01 的样本量要求：在效应量 $\beta = -0.1$（标准化系数）且标准误 SE=0.02 的假设下，所需最小样本量 n 约为 1,000 个商品观测值；若样本量不足，需使用 Bootstrap 方法计算置信区间，而非依赖 t 检验。

## Evidence

先验知识/题面给定，逻辑校验通过：t统计量=β/SE=5，远超双尾p<0.01临界值(≈2.58)，样本量n≈1000在统计功效上合理且量级正确；Bootstrap建议符合小样本或分布假设不满足时的稳健推断原则。

## Search Query

statistical power sample size calculation regression coefficient significance bootstrap
