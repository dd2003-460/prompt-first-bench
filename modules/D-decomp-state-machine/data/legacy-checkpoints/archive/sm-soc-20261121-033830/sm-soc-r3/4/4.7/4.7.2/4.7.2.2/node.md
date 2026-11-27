# N282: MCMC 采样收敛诊断指标：为确保后验分布估计的稳定性，需设定有效样本量 ESS ≥ 1000 以及 Gelman-Rubin 统计量 R-hat < 1.01

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

MCMC 采样收敛诊断指标：为确保后验分布估计的稳定性，需设定有效样本量 ESS ≥ 1000 以及 Gelman-Rubin 统计量 R-hat < 1.01 作为停止准则；若未满足，需增加迭代次数或调整步长。

## Corrected Claim

MCMC 采样收敛诊断指标：为确保后验分布估计的稳定性，需设定有效样本量 ESS ≥ 1000 以及 Gelman-Rubin 统计量 R-hat < 1.01 作为停止准则；若未满足，需增加迭代次数或调整步长。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

MCMC convergence diagnostics ESS R-hat threshold
