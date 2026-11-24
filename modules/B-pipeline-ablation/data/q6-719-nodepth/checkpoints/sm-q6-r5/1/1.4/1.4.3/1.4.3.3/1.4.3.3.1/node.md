# N480: 公有云突发流量计费条款：阿里云/Cloudflare 对超出预留带宽 B_reserve 的部分，通常按更高单价（如 1.5-2 倍基础价）计费或触发 QoS 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

公有云突发流量计费条款：阿里云/Cloudflare 对超出预留带宽 B_reserve 的部分，通常按更高单价（如 1.5-2 倍基础价）计费或触发 QoS 降级；需查询具体厂商的‘突发流量’定义及计费阈值（如超过 95th percentile 带宽的部分）。

## Corrected Claim

公有云突发流量计费条款：阿里云等厂商对超出预留/保底带宽的部分，通常按实际用量进行后付费计费（如弹性业务带宽）或触发QoS降级；具体单价倍率及计费阈值（如是否基于95th percentile）需查询具体厂商的最新计费文档。

## Evidence

[质询]陈述中关于“1.5-2倍基础价”的具体倍率以及“95th percentile”计费阈值属于特定厂商的商务条款细节，参考来源仅证实了“超出部分按实际用量后付费”或“弹性带宽计费”的存在，但未提供具体的倍率数值或百分位阈值，且不同厂商（如Cloudflare）的具体条款未在来源中体现，存在以偏概全或数值不精确的风险。 | 来源[2]直接支持了阿里云在DDoS防护场景下，业务流量峰值超出保底规格时，弹性业务带宽按实际用量产生后付费费用（即突发流量计费机制存在），但未提供具体倍率或95th percentile阈值，属于间接支持/部分支持，故降级。

## Search Query

Alibaba Cloud CDN burst traffic pricing policy 95th percentile billing

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1696416&rut=2278d5fdf9c4bc7957547186877560a6fc55d7b7f021aa66088246395a19af65', 'type': 'ddg', 'title': '阿里云服务器按使用流量计费：适用场景、收费标准及费用控制详解'}
- {'url': 'https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/billing-of-the-burstable-clean-bandwidth-feature&rut=ecd94240cc8ab7ef9f10a64359573259771811245d4ccfdc0ff543481301334f', 'type': 'ddg', 'title': '弹性业务带宽是如何计费的。-DDoS防护 (Anti-DDoS)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1667924&rut=079224053068aab39cdfc053aa42c64e25bbb2d71a3a0da63d0ff308870c64f5', 'type': 'ddg', 'title': '阿里云服务器公网带宽收费标准：按固定带宽和使用流量计费规则'}
