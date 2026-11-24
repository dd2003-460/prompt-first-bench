# N15: 带宽成本（¥/1000 req）：公有云 CDN 的出口带宽费用，基于日均下载量 2TB 与单价计算。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

带宽成本（¥/1000 req）：公有云 CDN 的出口带宽费用，基于日均下载量 2TB 与单价计算。

## Corrected Claim

带宽成本（¥/1000 req）：公有云 CDN 的出口带宽费用，需根据具体云厂商的实时单价及日均下载量 2TB 进行计算。

## Evidence

[质询]该陈述是一个具体的成本计算结果（经验事实），但参考来源仅提供了计费模式（按流量或带宽）和一般性定价说明，未提供具体的单价数值或针对“日均2TB”这一特定场景的计算结果，无法直接验证其数值准确性。 | 来源[1][2][3]确认了公有云CDN存在基于带宽或流量的计费模式，逻辑上支持该成本项的存在，但缺乏具体单价数据以直接验证计算结果，属于经验事实且缺来源直接支持。

## Search Query

CDN egress bandwidth cost per GB 2024

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://cloud.tencent.com/document/product/228/2949&rut=542d233b8262f3993114a18c919001fdeb3f7eb243434a2d2580d5feca18250a', 'type': 'ddg', 'title': '内容分发网络 Cdn 计费概述_腾讯云'}
