# N160: Bootstrap 收敛性检验指标：计算 BIC (Bayesian Information Criterion) 或 AIC 在重抽样过程中的变异系数 CV_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N51

## Claim

Bootstrap 收敛性检验指标：计算 BIC (Bayesian Information Criterion) 或 AIC 在重抽样过程中的变异系数 CV_BIC = std(BIC_b) / mean(BIC_b)；若 CV_BIC < 0.05，则认为 1000 次重抽样足以捕捉参数不确定性；否则需增加至 5000 次。

## Corrected Claim

Bootstrap 收敛性检验指标：计算 BIC (Bayesian Information Criterion) 或 AIC 在重抽样过程中的变异系数 CV_BIC = std(BIC_b) / mean(BIC_b)；若 CV_BIC < 0.05，则认为 1000 次重抽样足以捕捉参数不确定性；否则需增加至 5000 次。

## Evidence

先验知识/题面给定，逻辑校验通过
