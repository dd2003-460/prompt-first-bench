# N20: 跨域/跨网流量传输费用：自建节点间回源流量（2TB/日）及跨运营商（电信/联通/移动）互联互通的流量结算费用（¥/GB）。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

跨域/跨网流量传输费用：自建节点间回源流量（2TB/日）及跨运营商（电信/联通/移动）互联互通的流量结算费用（¥/GB）。

## Corrected Claim

跨域/跨网流量传输费用取决于具体网络架构：自建节点间回源流量（2TB/日）通常通过内网或专线传输，费用取决于专线带宽或内网流量策略；跨运营商（电信/联通/移动）互联互通的流量结算费用需依据具体互联协议或公网出口流量计费标准（¥/GB），不同运营商和地区差异较大，需查询具体运营商资费表。

## Evidence

[质询]该陈述试图将“自建节点间回源”与“跨运营商互联互通”混为一谈，且缺乏具体的¥/GB数值。自建节点间的流量通常走内网或私有专线，不涉及跨运营商结算；而跨运营商结算通常发生在公网出口或特定互联点，两者计费逻辑和量级完全不同。此外，参考来源均为云厂商（腾讯云、阿里云）的计费文档，无法直接支持“自建节点”或“跨运营商互联互通”的具体结算费用，属于经验事实且缺乏直接来源支持。 | 逻辑上流量费用与数据量成正比，量级合理；但参考来源[1][2][3]均为云服务商计费规则，未覆盖“自建节点”及“跨运营商互联互通”的具体结算标准，属于经验事实，逻辑自洽但缺来源直接支持。

## Search Query

inter-carrier traffic settlement cost China telecom unicom mobile CDN origin pull

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/document/product/436/53863&rut=50f1b4b2bd996c31d41d24905c69b9b24823f6228c6c3cf6dae07f8040315719', 'type': 'ddg', 'title': '对象存储 流量费用_腾讯云'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-data-transfer-when-alibaba-cloud-cdn-is-used-with-other-alibaba-cloud-services&rut=9de4f007814d52bc72cd7eec17e0df310c5ba189e08f4eee53d03181777bd698', 'type': 'ddg', 'title': '阿里云CDN与阿里云其他产品配合使用时流量如何计费？'}
- {'url': 'https://help.aliyun.com/zh/express-connect/product-overview/description-of-cross-border-traffic-billing&rut=5aa5fc076dd15bca135fb44a5d705c5efda440ab6b53d7382df9a5dfc8af75e4', 'type': 'ddg', 'title': '跨地域流量计费（使用CDT结算）-高速通道 (Express Connect)-阿里云帮助中心'}
