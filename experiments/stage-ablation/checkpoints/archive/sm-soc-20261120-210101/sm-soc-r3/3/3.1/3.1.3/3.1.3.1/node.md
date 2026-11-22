# N223: 共享随机源：买家决策噪声 ε_buyer，定义为同一商品在多次独立展示中转化率的波动标准差 σ_CVR，需通过同一商品在不同时段/不同用户群的CVR方差估计，假

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

共享随机源：买家决策噪声 ε_buyer，定义为同一商品在多次独立展示中转化率的波动标准差 σ_CVR，需通过同一商品在不同时段/不同用户群的CVR方差估计，假设 σ_CVR ≈ 0.5% [待核验]。

## Corrected Claim

共享随机源：买家决策噪声 ε_buyer，定义为同一商品在多次独立展示中转化率的波动标准差 σ_CVR，需通过同一商品在不同时段/不同用户群的CVR方差估计，具体数值需根据实际业务数据校准。

## Evidence

[质询]该陈述包含具体的经验参数（σ_CVR ≈ 0.5%），属于电商领域的经验事实，无法从第一性原理或数学公理中严格推导得出，且缺乏通用的理论依据支持该特定数值。 | 参考来源[1][2][3]分别涉及ROC曲线、胶片速度和量子光学，与电商转化率噪声估计完全无关，无可用外部证据；该事实为经验参数，逻辑自洽但缺来源支持。

## Search Query

conversion rate variance same product different users A/B test noise

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Receiver_operating_characteristic', 'type': 'wikipedia', 'title': 'Receiver operating characteristic'}
- {'url': 'https://en.wikipedia.org/wiki/Film_speed', 'type': 'wikipedia', 'title': 'Film speed'}
- {'url': 'https://en.wikipedia.org/wiki/Squeezed_states_of_light', 'type': 'wikipedia', 'title': 'Squeezed states of light'}
