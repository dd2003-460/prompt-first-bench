# N99: 好评率项 $\frac{N_{pos}}{N_{tot}}$ 的拉普拉斯平滑修正：为避免小样本偏差，实际算法中使用 $\hat{R} = \frac{N_{po

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

好评率项 $\frac{N_{pos}}{N_{tot}}$ 的拉普拉斯平滑修正：为避免小样本偏差，实际算法中使用 $\hat{R} = \frac{N_{pos} + \alpha}{N_{tot} + \alpha + \beta}$，其中 $\alpha, \beta$ 为先验伪计数（通常 $\alpha=2, \beta=1$），确保新卖家初始分数不为0或1，而是趋向中性值。

## Corrected Claim

好评率项 $\frac{N_{pos}}{N_{tot}}$ 的拉普拉斯平滑修正：为避免小样本偏差，实际算法中使用 $\hat{R} = \frac{N_{pos} + \alpha}{N_{tot} + \alpha + \beta}$，其中 $\alpha, \beta$ 为先验伪计数（通常 $\alpha=2, \beta=1$），确保新卖家初始分数不为0或1，而是趋向中性值。

## Evidence

先验知识/题面给定，逻辑校验通过：拉普拉斯平滑（Beta-Binomial 共轭先验）是处理小样本比例估计的标准统计方法，公式形式及参数逻辑自洽。

## Search Query

Laplace smoothing rating score formula alpha beta prior
