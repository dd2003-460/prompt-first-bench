# N205: 共享随机源：卖家内在价值 μ 的分布服从对数正态分布 LogN(μ_ln, σ_ln²)，其中 μ_ln 和 σ_ln 需基于平台商品数据估计；该分布是计算合规

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

共享随机源：卖家内在价值 μ 的分布服从对数正态分布 LogN(μ_ln, σ_ln²)，其中 μ_ln 和 σ_ln 需基于平台商品数据估计；该分布是计算合规损失 E[Loss] 的基础随机输入。

## Corrected Claim

共享随机源：卖家内在价值 μ 的分布服从对数正态分布 LogN(μ_ln, σ_ln²)，其中 μ_ln 和 σ_ln 需基于平台商品数据估计；该分布是计算合规损失 E[Loss] 的基础随机输入。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布常用于建模正偏态的经济变量（如价值、价格），且作为随机输入计算期望损失在数学上自洽。
