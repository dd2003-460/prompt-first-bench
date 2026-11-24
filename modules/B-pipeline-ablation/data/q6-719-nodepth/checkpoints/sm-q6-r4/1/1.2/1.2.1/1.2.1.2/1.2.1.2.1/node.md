# N459: 互联网骨干网单跳路由抖动的典型标准差 σ_hop_std 在正常负载下约为 1-3ms，但在 BGP 路由收敛或链路拥塞期间可突增至 10-50ms，该值需通过

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

互联网骨干网单跳路由抖动的典型标准差 σ_hop_std 在正常负载下约为 1-3ms，但在 BGP 路由收敛或链路拥塞期间可突增至 10-50ms，该值需通过 traceroute 时间序列分析获取。

## Corrected Claim

互联网骨干网单跳路由抖动在正常负载下通常较低（毫秒级），但在 BGP 路由收敛或链路拥塞期间会显著增加（可达数十毫秒），具体数值需通过 traceroute 时间序列分析获取。

## Evidence

[质询]具体数值范围（1-3ms 和 10-50ms）属于经验性统计结论，不同网络环境、运营商及测量方法下差异巨大，缺乏普适性的标准定义，且参考来源未提供该具体数值支持。 | 来源[1]讨论了跨境链路抖动和路由收敛问题，主题相关但仅定性描述，未提供具体的标准差数值范围；来源[2]和[3]与互联网骨干网路由抖动数值无关。该陈述逻辑自洽（抖动在故障时增大符合直觉），但具体数值缺乏直接来源支持，属于经验事实。

## Search Query

internet backbone per-hop jitter standard deviation ms BGP convergence

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/developer/article/2698212&rut=754aed67ef7b2f3be6b4ec137408b426509e58de23775530282b7cb82c9b99ac', 'type': 'ddg', 'title': '跨境专线高频故障深度复盘：晚高峰丢包、路由绕行、链路抖动根因与排查方案-腾讯云开发者社区-腾讯云'}
- {'url': 'https://zsc.github.io/chip_packaging_interconnect/chapter3.html&rut=48da5699e1e165f850f21bff0bdcb8b74ee3f048efb65e4a100d001299c6011d', 'type': 'ddg', 'title': '第3章：NoC性能建模与优化 | chip_packaging_interconnect'}
- {'url': 'https://support.huawei.com/enterprise/zh/doc/EDOC1100411451/dee028f1&rut=43e122437922f41f703aa76f54a4c532e8ac3f681553f83cc5c4218052e44554', 'type': 'ddg', 'title': '了解BFD单跳/多跳检测 - CloudEngine S16700 V600R024C00 配置指南-可靠性 - 华为'}
