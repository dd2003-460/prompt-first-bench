# N66: 信任维护成本 C_trust_maintenance 的具体构成：C_trust = C_dispute * F_dispute + C_refund * F_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N14

## Claim

信任维护成本 C_trust_maintenance 的具体构成：C_trust = C_dispute * F_dispute + C_refund * F_refund，其中 F_dispute 和 F_refund 为纠纷率和退款率；需量化高信号卖家（高挂价）的纠纷率相对于低信号卖家的差异（通常低 20%-40%）。

## Corrected Claim

信任维护成本 C_trust 可表示为 C_dispute * F_dispute + C_refund * F_refund。高信号卖家（高挂价）通常具有更低的纠纷率，但具体降低幅度（如20%-40%）需依据特定市场数据实证，缺乏通用来源支持。

## Evidence

[质询]该陈述包含具体的经验性数值（高信号卖家纠纷率比低信号卖家低20%-40%），这属于市场/行为经济学经验事实，无法从第一性原理推导，且参考来源完全无关，缺乏直接证据支持该具体数值区间。 | 逻辑上成本构成公式自洽，但具体数值差异（20%-40%）为经验事实，参考来源[1][2][3]均与电商信任机制或卖家纠纷率无关，无法提供外部支持，故降级。

## Search Query

dispute rate refund rate high price listing seller reputation used goods platform

## Retrieval Sources

- {'url': 'https://blog.csdn.net/sp60cn/article/details/157943521&rut=a7fce45ac516f874d559733a53c4fd88cd35bbbfc786010c6ae5031cf1d351de', 'type': 'ddg', 'title': 'Oracle云平台基础设施文档-计费与成本管理篇4-CSDN博客'}
- {'url': 'https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_05_0000.html&rut=a19ac4f703e84d8f9078e5d88c909ff1b9665528dafa53e8a65a5cb0d1e190b6', 'type': 'ddg', 'title': '成本优化支柱_卓越架构技术框架与实践_云架构中心-华为云'}
- {'url': 'https://trustc-project.com/&rut=75ab09d368a710975c6370ed2576b0f732572a2f843dc91749f8bcf94a01e0e0', 'type': 'ddg', 'title': 'TrustC'}
