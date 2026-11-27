# N116: 触发风控标记后，卖家搜索权重 W_new 的计算公式为 W_new = W_old × (1 - k_penalty)，其中 k_penalty 在单次触发时为

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37, N40, N41

## Claim

触发风控标记后，卖家搜索权重 W_new 的计算公式为 W_new = W_old × (1 - k_penalty)，其中 k_penalty 在单次触发时为 0.2，若 30 天内累计触发 3 次则 k_penalty 升级为 0.5。

## Corrected Claim

触发风控标记后，卖家搜索权重通常会受到惩罚性下调，具体计算公式及惩罚系数（如k_penalty）取决于特定电商平台的内部风控策略，常见策略中单次触发可能伴随一定比例的权重衰减，多次触发会加重惩罚，但具体数值（如0.2/0.5）需以平台官方文档为准。

## Evidence

[质询]该陈述包含具体的算法参数（k_penalty=0.2/0.5）和逻辑规则，属于特定平台（如淘宝、京东等）的内部风控策略细节。此类经验事实无法从第一性原理推导，且不同平台或不同时期的策略可能不同，缺乏通用性。 | 参考来源[1][2][3]均与该电商风控事实主题无关（分别为英国2026/2024年事件及次贷危机），无可用外部证据支持。该陈述为经验事实，逻辑自洽但缺来源支持。

## Search Query

platform search weight penalty formula k_penalty 0.2 0.5 cumulative trigger 30 days

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/2026_in_the_United_Kingdom', 'type': 'wikipedia', 'title': '2026 in the United Kingdom'}
- {'url': 'https://en.wikipedia.org/wiki/2024_in_the_United_Kingdom', 'type': 'wikipedia', 'title': '2024 in the United Kingdom'}
- {'url': 'https://en.wikipedia.org/wiki/Subprime_mortgage_crisis', 'type': 'wikipedia', 'title': 'Subprime mortgage crisis'}
