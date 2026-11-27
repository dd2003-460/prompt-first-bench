# N83: Pareto 分布尾部截断对线性回归失效的量化：计算 Top-1% 样本中 Size 的实际条件均值 E[Size|Top-1%] 与线性回归预测值 E[Siz

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

Pareto 分布尾部截断对线性回归失效的量化：计算 Top-1% 样本中 Size 的实际条件均值 E[Size|Top-1%] 与线性回归预测值 E[Size|Heat=h_99%] 的相对误差 Δ_err = |Actual - Linear| / Linear，验证 5-10% 偏差范围。

## Corrected Claim

Pareto 分布尾部截断会导致线性回归在极端值预测上失效，具体相对误差 Δ_err 取决于分布参数，需通过具体数据计算验证，而非固定为 5-10%。

## Evidence

[质询]该陈述声称验证了具体的数值偏差范围（5-10%），但参考来源均未提供关于Pareto分布尾部截断对线性回归失效的具体量化数据或实验结果，属于缺乏外部证据支持的经验性数值断言。 | 逻辑上，Pareto分布具有重尾特性，线性回归在极端值处的预测确实会失效，但具体偏差范围（5-10%）依赖于具体的分布参数（如形状参数α）和截断点，无法从第一性原理直接推出固定值，且参考来源[1][2][3]均未提供相关量化支持。

## Search Query

Pareto distribution conditional mean linear regression bias truncation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Multivariate_normal_distribution', 'type': 'wikipedia', 'title': 'Multivariate normal distribution'}
- {'url': 'https://en.wikipedia.org/wiki/Normal_distribution', 'type': 'wikipedia', 'title': 'Normal distribution'}
- {'url': 'https://en.wikipedia.org/wiki/Harmonic_mean', 'type': 'wikipedia', 'title': 'Harmonic mean'}
