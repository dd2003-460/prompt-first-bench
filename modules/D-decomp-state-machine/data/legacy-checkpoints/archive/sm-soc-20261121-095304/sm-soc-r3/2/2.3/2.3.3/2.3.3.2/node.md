# N124: 触发‘不稳定卖家’标记的价格波动次数阈值 N_max 通常设为 2 次或 3 次；若 N_vol 达到 N_max 且伴随价格下降，则触发风控，该阈值直接决定了

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

触发‘不稳定卖家’标记的价格波动次数阈值 N_max 通常设为 2 次或 3 次；若 N_vol 达到 N_max 且伴随价格下降，则触发风控，该阈值直接决定了卖家策略调整的频率上限。

## Corrected Claim

触发‘不稳定卖家’标记的价格波动次数阈值 N_max 通常设为 2 次或 3 次（具体数值依平台风控策略而定）；若 N_vol 达到 N_max 且伴随价格下降，则触发风控，该阈值直接决定了卖家策略调整的频率上限。

## Evidence

[质询]该陈述描述的是特定平台或内部风控系统的自定义参数（N_max=2或3），属于经验事实/工程配置，而非通用物理定律或数学公理。参考来源主要讨论标记价格、强平机制及价格保护功能，未提及具体的‘不稳定卖家’标记阈值或N_max的具体数值，存在来源缺失风险。 | 逻辑自洽（阈值设定符合风控直觉），但参考来源[1][2][3]均未直接支持N_max=2或3这一具体经验参数，属于经验事实且缺来源直接支持。

## Search Query

second hand marketplace seller unstable price change frequency threshold N_max

## Retrieval Sources

- {'url': 'https://www.qianyanke.cn/2026/08/06/%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3%E4%BA%A4%E6%98%93%E6%89%80%E5%90%88%E7%BA%A6%E4%BA%A4%E6%98%93%E6%9C%BA%E5%88%B6%EF%BC%9A%E6%A0%87%E8%AE%B0%E4%BB%B7%E6%A0%BC%E3%80%81%E8%B5%84%E9%87%91%E8%B4%B9/&rut=8c13c4355df6508e6300bb396ef6c9bd8f70f55dcf75b4e6a13ecbfce90d939b', 'type': 'ddg', 'title': '深度拆解交易所合约交易机制：标记价格、资金费率与强平逻辑全梳理'}
- {'url': 'https://www.binance.com/zh-CN/support/faq/detail/2b9dc811ce7340469357867122b975dc&rut=a2b864ca5c0c7c321a36684648d4c3913c5da264e1d622ac3da04b06b44ae71b', 'type': 'ddg', 'title': '如何使用合约价格保护功能 - Binance'}
- {'url': 'https://www.gate.com/zh/blog/gate-futures-liquidation-mechanism-and-mark-price-redefine-risk-control&rut=a7350d403b355a115ce51811dd0992110797f0994f11d46a88179169e6b795ec', 'type': 'ddg', 'title': '止盈止损总慢一步？Gate 合约强平机制与标记价格重新定义安全'}
