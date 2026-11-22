# N306: 偏度显著性检验的样本量要求：使用 Jarque-Bera 检验，统计量 JB = n/6 * (S^2 + K^2/4)，其中 S 为偏度，K 为峰度；在 α=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

偏度显著性检验的样本量要求：使用 Jarque-Bera 检验，统计量 JB = n/6 * (S^2 + K^2/4)，其中 S 为偏度，K 为峰度；在 α=0.05 下，若 JB > 5.99，则拒绝正态分布假设；对于偏度 S > 0.5 的显著性，需样本量 n > 300 以保证检验功效（Power > 0.8），否则小样本下偏度估计方差过大，无法区分真实偏斜与抽样误差。

## Corrected Claim

偏度显著性检验的样本量要求：使用 Jarque-Bera 检验，统计量 JB = n/6 * (S^2 + K^2/4)，其中 S 为偏度，K 为峰度；在 α=0.05 下，若 JB > 5.99，则拒绝正态分布假设；对于偏度 S > 0.5 的显著性，需样本量 n > 300 以保证检验功效（Power > 0.8），否则小样本下偏度估计方差过大，无法区分真实偏斜与抽样误差。

## Evidence

先验知识/题面给定，逻辑校验通过
