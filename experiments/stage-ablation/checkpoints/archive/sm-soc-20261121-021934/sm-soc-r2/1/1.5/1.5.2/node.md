# N36: 平台激励维持均衡的临界条件为 ∂Π_platform/∂P_ask > 0，即平台收益对挂价的偏导数为正；该条件成立当且仅当成交量弹性 ε_Q 满足 |ε_Q|

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

平台激励维持均衡的临界条件为 ∂Π_platform/∂P_ask > 0，即平台收益对挂价的偏导数为正；该条件成立当且仅当成交量弹性 ε_Q 满足 |ε_Q| < 1/P_ask（即价格上升1%导致成交量下降小于1%），需通过历史数据回归估计 ε_Q 的具体值。

## Corrected Claim

在特定简化模型（如固定佣金率、无成本、单一弹性主导）下，平台收益对挂价增加的临界条件近似为成交量价格弹性绝对值小于价格倒数（|ε_Q| < 1/P_ask）；但在一般情形下，需考虑佣金结构、成本及竞争动态，该条件并非普适的“当且仅当”关系。

## Evidence

[质询]该陈述将平台收益对价格的偏导数条件简化为单一的价格弹性阈值（|ε_Q| < 1/P_ask），忽略了平台收益通常由“佣金率×成交量×价格”构成，且佣金率本身可能随价格或市场状态变化，此外还忽略了成本项和竞争效应，导致“当且仅当”这一强逻辑关系在一般经济模型中不成立，属于过度简化的经验性结论。 | 来源[1]涉及平台均衡理论但未提供该具体弹性阈值公式；来源[2]讨论自适应控制，与本题无关。该陈述为经验性经济模型结论，逻辑上量纲自洽（若P_ask为百分比形式或特定归一化单位），但缺乏直接来源支持且存在模型假设局限，故降级。

## Search Query

platform revenue sensitivity listing price volume elasticity secondhand market

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2309.08781&rut=b3a773311febfdfee2115a371d5afeff39adf762e83f0c61cd0fc96199c4b72b', 'type': 'ddg', 'title': 'PlatformEquilibrium: AnalyzingSocialWelfareinOnline MarketPlaces'}
- {'url': 'https://www.zhihu.com/question/266601777/answer/375458125?utm_psn=1710461028381454336&rut=0c7135737e786501590d0f7da3875fc2dee62ea0ffc03d4093d34acdb6f1057d', 'type': 'ddg', 'title': '自适应控制中的持续激励条件怎么理解？ - 知乎'}
