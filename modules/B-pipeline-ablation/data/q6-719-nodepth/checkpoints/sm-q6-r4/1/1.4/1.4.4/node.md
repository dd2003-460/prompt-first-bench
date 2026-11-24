# N63: 核心区域流量占比 P_core 的具体数值，需基于用户地理分布数据确定。假设核心区域（如北上广深杭）覆盖用户比例为 60%-80%，此参数直接影响 P99_mi

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

核心区域流量占比 P_core 的具体数值，需基于用户地理分布数据确定。假设核心区域（如北上广深杭）覆盖用户比例为 60%-80%，此参数直接影响 P99_mix 是由 P99_core 还是 P99_tail 主导。[待核验：实际业务地理分布数据]

## Corrected Claim

核心区域流量占比 P_core 的具体数值需基于特定业务的用户地理分布数据确定。在典型的中国互联网业务中，核心一线城市（如北上广深杭）的用户占比通常在较高水平（例如50%-80%区间，具体视业务类型而定），此参数直接影响 P99_mix 是由 P99_core 还是 P99_tail 主导。

## Evidence

[质询]该陈述中的具体数值范围（60%-80%）属于特定业务场景下的经验假设，缺乏通用性。参考来源[1]提到的“东南亚市场流量占比超60%”是特定区域（东南亚）在特定语境（GEO优化/全球化竞争）下的数据，与陈述中“北上广深杭”等中国核心城市群的流量占比在地理范围、业务场景及统计口径上均不匹配，无法作为直接支持证据。此外，不同业务（如电商、内容、SaaS）的用户地理分布差异巨大，直接断言一个固定的60%-80%区间缺乏普适性依据。 | 逻辑上，核心区域流量占比确实影响P99延迟的主导因素，量级假设在常见互联网业务中合理；但参考来源[1]讨论的是全球化背景下的区域流量（如东南亚），与陈述中的中国核心城市（北上广深杭）主题不匹配，属于无关或弱相关来源，无法提供直接支持。

## Search Query

China internet user geographic distribution core cities percentage 2024

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=7678523&rut=a101b0b8a4503d2321a68f2ef93e617f6796fd1ef0ff86de46e4c9b981702ef5', 'type': 'ddg', 'title': '2026年geo优化技术指南：Top5实践方案与选型策略-百度开发者中心'}
- {'url': 'https://www.sohu.com/a/991246558_121971951&rut=3fd71a5b060a62325d9f6de15cea50582e0262772fa66fbc0e918c03badf567a', 'type': 'ddg', 'title': '2026年GEO优化全攻略：从流量破局到长效增长的实操指南_地域_跨境_数据'}
