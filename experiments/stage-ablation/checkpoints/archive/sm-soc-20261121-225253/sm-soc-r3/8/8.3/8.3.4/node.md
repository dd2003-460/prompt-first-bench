# N121: 在样本量受限（N_high 或 N_drop < 30）的工作点下，Z 检验的正态近似失效，需改用基于二项分布的精确检验（Exact Test），此时检验的统计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47, N48

## Claim

在样本量受限（N_high 或 N_drop < 30）的工作点下，Z 检验的正态近似失效，需改用基于二项分布的精确检验（Exact Test），此时检验的统计功效（Power）显著低于大样本 Z 检验，可能导致无法检测出实际存在的平台流量偏差（Type II error 风险增加）。

## Corrected Claim

在样本量受限（N_high 或 N_drop < 30）的工作点下，Z 检验的正态近似失效，需改用基于二项分布的精确检验（Exact Test），此时检验的统计功效（Power）显著低于大样本 Z 检验，可能导致无法检测出实际存在的平台流量偏差（Type II error 风险增加）。

## Evidence

先验知识/题面给定，逻辑校验通过：小样本下正态近似失效是统计学基本事实，精确检验功效低于大样本近似检验符合统计原理。

## Search Query

exact binomial test vs Z test small sample power loss
