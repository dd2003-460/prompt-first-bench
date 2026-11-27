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

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了JB统计量的理论推导、临界值与判定逻辑、以及AD检验的修正方法，三者内容独立且互补，无重复或矛盾，完整覆盖了父节点中关于JB和AD检验的核心要求。）

## Search Query

Jarque-Bera test critical value Laplace vs Normal distribution pricing residuals
