# N163: σ_max 的动态修正项：在存在价格泡沫或社会传染效应时，σ_max 并非固定为 0.4*μ，而是随市场热度指数 H 增加，修正公式为 σ_max(t) = 0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

σ_max 的动态修正项：在存在价格泡沫或社会传染效应时，σ_max 并非固定为 0.4*μ，而是随市场热度指数 H 增加，修正公式为 σ_max(t) = 0.4 * μ * (1 + 0.1 * H(t))，其中 H(t) 为近7天同类商品成交量/搜索量的比值，需通过时间序列数据估计 H 的波动范围。

## Corrected Claim

在特定市场热度模型中，σ_max 可能随市场热度指数 H 动态修正，例如采用 σ_max(t) = 0.4 * μ * (1 + 0.1 * H(t)) 的形式，其中 H(t) 需通过时间序列数据估计，但该公式的具体系数和形式依赖于特定模型假设，并非通用常数。

## Evidence

[质询]该公式属于特定模型或假设下的经验性参数设定，缺乏通用理论支持，且参考来源均未涉及此具体数学关系，存在将特定场景假设误认为普遍规律的风险。 | 逻辑上自洽（量纲一致，修正项随热度增加符合直觉），但参考来源[1][2][3]均与该具体公式无关，无法提供外部支持，且作为经验事实无法从第一性原理严格推导。

## Search Query

price bubble market heat index volatility correction factor second hand platform

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Economic_impact_of_the_COVID-19_pandemic', 'type': 'wikipedia', 'title': 'Economic impact of the COVID-19 pandemic'}
- {'url': 'https://en.wikipedia.org/wiki/History_of_the_United_States_%281991%E2%80%932016%29', 'type': 'wikipedia', 'title': 'History of the United States (1991–2016)'}
- {'url': 'https://en.wikipedia.org/wiki/British_enterprise_law', 'type': 'wikipedia', 'title': 'British enterprise law'}
