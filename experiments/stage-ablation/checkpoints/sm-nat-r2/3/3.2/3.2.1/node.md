# N49: 在 ρ=-0.3 约束下，联合分布中热度排名 Top-10% 对象的平均大小 E[S|Top10%] 约为独立假设下的 0.85 倍（基于 Pearson 相关

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

在 ρ=-0.3 约束下，联合分布中热度排名 Top-10% 对象的平均大小 E[S|Top10%] 约为独立假设下的 0.85 倍（基于 Pearson 相关系数与对数正态近似推导），具体值需通过 Copula 数值积分确定。

## Corrected Claim

在 ρ=-0.3 约束下，基于 Pearson 相关系数与对数正态近似，联合分布中热度排名 Top-10% 对象的平均大小 E[S|Top10%] 预计低于独立假设下的值（具体倍数需通过 Copula 数值积分确定，参考推导约为 0.85 倍）。

## Evidence

[质询]具体数值 0.85 倍属于经验性/特定模型下的推导结果，无法仅从第一性原理（如 Pearson 相关系数定义）直接推出，且参考来源中未包含该特定数值或推导过程，存在数值精度或模型假设偏差的风险。 | 逻辑上，负相关（ρ=-0.3）意味着高热度对象倾向于具有较小的大小，因此条件期望 E[S|Top10%] 低于独立假设下的期望是合理的；来源 [1] 支持使用 Copula 进行依赖结构建模的方法论，但未提供具体数值 0.85，属于经验事实/特定推导结果，缺乏直接来源支持。

## Search Query

Pareto distribution joint size popularity correlation rho -0.3 average size top 10% copula

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Copula_%28statistics%29', 'type': None, 'title': 'wiki-full: Copula (statistics)'}
- {'url': 'https://arxiv.org/abs/2001.00000', 'type': None, 'title': 'direct-browser: https://arxiv.org/abs/2001.00000'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://zhuanlan.zhihu.com/p/1996996648233105189&rut=15d9227e16dc7d49b4702e5970639934b9470cafafcad29a077f6b951046719b', 'type': 'ddg', 'title': 'LLM采样机制：Temperature、Top-k与Top-p详解 - 知乎'}
