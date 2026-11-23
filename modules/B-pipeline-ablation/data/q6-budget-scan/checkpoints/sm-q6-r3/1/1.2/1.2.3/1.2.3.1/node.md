# N89: 公有云 CDN 在中国大陆偏远地区（如西部/东北）的 P99 延迟通常高于 100ms，主要受限于当地 PoP 密度低及跨省骨干网拥塞；具体数值需参考阿里云/腾

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

公有云 CDN 在中国大陆偏远地区（如西部/东北）的 P99 延迟通常高于 100ms，主要受限于当地 PoP 密度低及跨省骨干网拥塞；具体数值需参考阿里云/腾讯云 CDN 的延迟热力图或实测报告。

## Corrected Claim

公有云 CDN 在中国大陆偏远地区（如西部/东北）的 P99 延迟通常显著高于核心城市，主要受限于当地 PoP 密度低及跨省骨干网拥塞；具体数值需参考阿里云/腾讯云 CDN 的延迟热力图或实测报告。

## Evidence

[质询]具体数值（>100ms）属于经验事实，缺乏直接来源支持，且不同运营商和具体地理位置差异巨大，单一阈值可能不准确。 | 逻辑自洽（偏远地区PoP少导致延迟高符合网络常识），但参考来源[1]讨论的是大模型API网关，与CDN无关，无外部证据支持具体数值，属经验事实缺来源支持。

## Search Query

Alibaba Cloud CDN China remote region P99 latency 100ms 200ms

## Retrieval Sources

- {'url': 'https://www.163.com/dy/article/KUK0RUJI0556M7K3.html&rut=c3ab387e5b33e857c89a8689927f29bb18da898a70a9c3ba3ead2cb3ff2de468', 'type': 'ddg', 'title': '2026大模型API调用稳定服务商评测：TOP5平台如何解决P99延迟痛点|路由|网关|top|sla_网易订阅'}
