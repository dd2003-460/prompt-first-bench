# N122: 在LogNormal(μ_log, σ_log²)模型中，μ_log 的具体数值估计需基于平台历史成交数据的对数均值，对于常见二手电子产品品类，μ_log 通常

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

在LogNormal(μ_log, σ_log²)模型中，μ_log 的具体数值估计需基于平台历史成交数据的对数均值，对于常见二手电子产品品类，μ_log 通常对应中位市场价的自然对数，具体值需检索该品类最近90天的成交记录计算得出。

## Corrected Claim

在LogNormal(μ_log, σ_log²)模型中，μ_log 的数值估计基于平台历史成交数据的对数均值，理论上对应中位市场价的自然对数；具体数值需根据实际业务需求选取合适时间窗口的成交记录计算得出。

## Evidence

[质询]该陈述包含具体的经验性操作建议（如“最近90天”的数据窗口），这属于经验事实而非第一性原理可推导的数学性质，且参考来源未提供此类具体业务参数支持。 | 逻辑上，对数正态分布的对数均值确实对应中位数的对数，但“90天”这一具体经验参数缺乏来源支持，属于经验事实，故降级。

## Search Query

used electronics market median price lognormal distribution parameters

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Log-normal_distribution&rut=891a232f03f37070747e08759a7e64325545f311405770b5cf657784a15b7f8c', 'type': 'ddg', 'title': 'Log-normal distribution - Wikipedia'}
