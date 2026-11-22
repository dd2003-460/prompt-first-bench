# N79: 分布形态检验的统计检验量：使用 Jarque-Bera 检验或 Anderson-Darling 检验对卖家定价偏差残差进行分布形态检验，需确定检验统计量 $J

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

分布形态检验的统计检验量：使用 Jarque-Bera 检验或 Anderson-Darling 检验对卖家定价偏差残差进行分布形态检验，需确定检验统计量 $JB = n[\frac{S^2}{6} + \frac{(K-3)^2}{24}]$ 的临界值，以在 95% 置信水平下拒绝正态分布假设并支持拉普拉斯分布假设。

## Corrected Claim

分布形态检验的统计检验量：使用 Jarque-Bera 检验或 Anderson-Darling 检验对卖家定价偏差残差进行分布形态检验，需确定检验统计量 $JB = n[\frac{S^2}{6} + \frac{(K-3)^2}{24}]$ 的临界值，以在 95% 置信水平下拒绝正态分布假设并支持拉普拉斯分布假设。

## Evidence

先验知识/题面给定，逻辑校验通过：Jarque-Bera 统计量公式正确，且 JB 检验确实用于检验正态性（拒绝正态假设后支持其他分布如拉普拉斯在逻辑上自洽）。

## Search Query

Jarque-Bera test critical value Laplace vs Normal distribution pricing residuals
