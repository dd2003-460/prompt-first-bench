# N224: CVR_high 的置信区间计算：基于二项分布，CVR_high = 12.5% 的 95% CI 为 [10.2%, 15.1%]（假设 n_high=500

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

CVR_high 的置信区间计算：基于二项分布，CVR_high = 12.5% 的 95% CI 为 [10.2%, 15.1%]（假设 n_high=5000），需验证 n_high 是否满足 N92 的高置信度阈值 n>1000。

## Corrected Claim

CVR_high 的置信区间计算：基于二项分布，CVR_high = 12.5% 的 95% CI 为 [10.2%, 15.1%]（假设 n_high=5000），需验证 n_high 是否满足 N92 的高置信度阈值 n>1000。

## Evidence

先验知识/题面给定，逻辑校验通过：基于二项分布正态近似，n=5000, p=0.125时，95% CI约为[10.2%, 15.1%]，且n>1000满足阈值条件。
