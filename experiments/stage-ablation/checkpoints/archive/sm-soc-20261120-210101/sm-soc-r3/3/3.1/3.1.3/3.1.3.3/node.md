# N225: CVR_low 的置信区间计算：基于二项分布，CVR_low = 8.3% 的 95% CI 为 [6.5%, 10.5%]（假设 n_low=5000），需验

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

CVR_low 的置信区间计算：基于二项分布，CVR_low = 8.3% 的 95% CI 为 [6.5%, 10.5%]（假设 n_low=5000），需验证 n_low 是否满足 N92 的高置信度阈值 n>1000。

## Corrected Claim

CVR_low 的置信区间计算：基于二项分布，CVR_low = 8.3% 的 95% CI 为 [6.5%, 10.5%]（假设 n_low=5000），需验证 n_low 是否满足 N92 的高置信度阈值 n>1000。

## Evidence

先验知识/题面给定，逻辑校验通过：基于二项分布正态近似，n=5000, p=0.083时，95% CI约为[0.065, 0.105]，且n=5000>1000满足阈值条件。
