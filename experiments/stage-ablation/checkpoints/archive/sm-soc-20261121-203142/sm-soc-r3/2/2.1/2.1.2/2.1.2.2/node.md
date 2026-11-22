# N152: CTR 比值 1.5 的统计显著性检验：基于样本量 n_1, n_2 和标准误 SE_ctr，计算 Z-score = (CTR_1/CTR_2 - 1.5) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

CTR 比值 1.5 的统计显著性检验：基于样本量 n_1, n_2 和标准误 SE_ctr，计算 Z-score = (CTR_1/CTR_2 - 1.5) / SE_ratio，若 Z > 1.96 则确认 1.5 倍差异非随机波动；需估算 CTR 的二项分布方差 Var(CTR) = p(1-p)/n 以构建置信区间。

## Corrected Claim

CTR 比值 1.5 的统计显著性检验：基于样本量 n_1, n_2 和标准误 SE_ctr，计算 Z-score = (CTR_1/CTR_2 - 1.5) / SE_ratio，若 Z > 1.96 则确认 1.5 倍差异非随机波动；需估算 CTR 的二项分布方差 Var(CTR) = p(1-p)/n 以构建置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过
