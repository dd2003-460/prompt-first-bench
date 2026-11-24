# N229: 自建POP回源流量单价 Unit_Price_Source_Self 的量化取值：自建节点回源通常通过内部专线或BGP多线接入，成本结构为 (专线月租 + 公网

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

自建POP回源流量单价 Unit_Price_Source_Self 的量化取值：自建节点回源通常通过内部专线或BGP多线接入，成本结构为 (专线月租 + 公网IP费用) / 流量，典型值约为 ¥0.05-0.10/GB（低于公有云零售价），需根据实际带宽采购合同确定

## Corrected Claim

自建POP回源流量单价通常低于公有云零售价，具体数值取决于专线月租、公网IP费用及实际流量规模，需根据实际带宽采购合同确定，典型值可能在 ¥0.05-0.10/GB 区间（需具体验证）。

## Evidence

[质询]该陈述包含具体的经验性价格区间（¥0.05-0.10/GB）和特定的成本结构假设，属于经验事实。参考来源均与该主题无关（来源1为SAP会计术语，来源2/3为AI API中转站搭建），无法提供外部证据支持该具体数值。 | 逻辑上，自建POP通过专线或BGP接入的成本确实通常低于公有云零售带宽价格，量级合理；但参考来源[1][2][3]均与CDN/POP回源流量成本无关，无法提供直接支持。根据经验事实排除条款，缺乏来源支持的经验参数应降级。

## Search Query

private BGP line cost per GB China 2024 data center interconnect pricing

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31134719/article/details/118919351&rut=610e8a88e3abeb8dedd29c116e68a5c51b595e77d445065ed1c8bd5a2cdd1f1b', 'type': 'ddg', 'title': 'pop和pup计算机原理,PUP成本核算原理.doc - CSDN博客'}
- {'url': 'https://obvps.com/posts/%E8%87%AA%E5%BB%BAapi%E4%B8%AD%E8%BD%AC%E7%AB%99%E5%AE%8C%E6%95%B4%E6%90%AD%E5%BB%BA%E6%8C%87%E5%8D%97-sub2api-flowpilot/&rut=efe8ade285579977cfb1a5e51d4565f26ce720477cc8c6bd5acf65350701a5e6', 'type': 'ddg', 'title': '自建 API 中转站完整搭建指南：Sub2API + FlowPilot + Codex接码 - OBVPS'}
- {'url': 'https://priceai.cc/guides/self-host-api-transit&rut=445b294b7fcecf97c9423c808cc4c75a51ab79fac950f7490d6d0a0eb7fd55d2', 'type': 'ddg', 'title': '怎么自己搭一个自用 API 中转站 | PriceAI'}
