# N194: MCMC 采样收敛诊断：使用 R-hat 统计量判断链收敛，若 R-hat < 1.1 则收敛；有效样本量 ESS 需 > 1000 以确保后验分布估计精度；若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

MCMC 采样收敛诊断：使用 R-hat 统计量判断链收敛，若 R-hat < 1.1 则收敛；有效样本量 ESS 需 > 1000 以确保后验分布估计精度；若 ESS < 500 则需增加迭代次数或重新参数化模型。

## Corrected Claim

MCMC 采样收敛诊断：使用 R-hat 统计量判断链收敛，若 R-hat < 1.1 则收敛；有效样本量 ESS 需 > 1000 以确保后验分布估计精度；若 ESS < 500 则需增加迭代次数或重新参数化模型。

## Evidence

先验知识/题面给定，逻辑校验通过
