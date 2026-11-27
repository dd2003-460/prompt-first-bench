# N217: 卖家信用因子 g(S_seller) 的量化：信用评分对咨询率的边际影响，建模为 g(S_seller) = exp(κ * S_seller)，其中 κ 为信

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N77

## Claim

卖家信用因子 g(S_seller) 的量化：信用评分对咨询率的边际影响，建模为 g(S_seller) = exp(κ * S_seller)，其中 κ 为信用敏感度系数，需通过回归分析估计 κ，若 κ > 0.1 则高信用卖家咨询率显著高于基线。

## Corrected Claim

卖家信用因子 g(S_seller) 的量化：信用评分对咨询率的边际影响，可建模为 g(S_seller) = exp(κ * S_seller)，其中 κ 为信用敏感度系数，需通过回归分析估计 κ；若估计出的 κ 显著为正，则表明高信用卖家咨询率高于基线。

## Evidence

[质询]该陈述包含具体的经验性阈值（κ > 0.1）和特定的函数形式（指数函数），属于经验事实/模型假设，无法从第一性原理严格推导，且缺乏外部来源支持其具体数值和形式的有效性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

seller credit score impact on buyer inquiry rate regression analysis
