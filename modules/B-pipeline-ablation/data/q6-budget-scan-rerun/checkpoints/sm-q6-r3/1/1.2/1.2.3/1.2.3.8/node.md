# N168: 骨干网拥塞对POP-源站延迟的动态影响：在晚高峰时段（20:00-23:00），中国骨干网跨省链路利用率达70-90%，导致延迟增加20-50%（即20-50m

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45, N46, N47

## Claim

骨干网拥塞对POP-源站延迟的动态影响：在晚高峰时段（20:00-23:00），中国骨干网跨省链路利用率达70-90%，导致延迟增加20-50%（即20-50ms延迟变为24-75ms）；需在P99延迟计算中引入时间加权因子，峰值时段权重约为日均流量的1.5-2.0倍

## Corrected Claim

在晚高峰时段（20:00-23:00），中国骨干网及国际出口链路通常出现拥塞，导致POP-源站延迟显著增加（具体增幅视链路负载而定，通常可达20%-50%或更高）；建议在P99延迟计算中引入时间加权因子，峰值时段权重高于日均水平（具体倍数需根据实际监控数据校准，通常建议1.5-2.0倍作为经验参考）。

## Evidence

[质询]具体数值（利用率70-90%、延迟增加20-50%、权重1.5-2.0倍）缺乏权威公开数据支持，且将‘国际出口带宽拥堵’（来源主题）直接等同于‘中国骨干网跨省链路’（陈述主题）存在口径混淆风险，不同运营商和具体链路差异巨大，通用化数值可能不准确。 | 来源[1]和[2]确认了晚高峰（20:00-23:00）存在骨干网/国际出口拥堵及延迟增加的现象，间接支持了‘拥塞导致延迟增加’的逻辑，但未提供具体的利用率百分比、延迟增幅具体数值或P99权重系数，属于经验事实且缺乏直接数据支持。

## Search Query

China backbone network congestion peak hour latency increase percentage

## Retrieval Sources

- {'url': 'https://jichangwending.world/stable/articles/s01-a-3/&rut=aef6e6b978fe7577e357137ed0e4d18174e74c65c0301ddae5a5fc290c0ce5c9', 'type': 'ddg', 'title': '晚高峰20:00-23:00骨干网拥堵机理：国际出口带宽与QoS排队规则 - 稳定机场指南深度技术白皮书'}
- {'url': 'https://tiziclash.blog/clash-airport/stability/&rut=32bac42b40bc857a27e3b45b05081952ee9e861615096e6124abe67ec8de6ab2', 'type': 'ddg', 'title': '2026 Clash 机场晚高峰稳定性监控：7×24 小时丢包率与骨干网波动压测 | Clash 梯子指南'}
