# N217: 在公有云按峰值带宽计费模式下，10Gbps峰值带宽的月度预留成本约为¥20,000-40,000，具体取决于运营商（电信/联通/移动）及是否包含BGP多线接入，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69, N70, N71

## Claim

在公有云按峰值带宽计费模式下，10Gbps峰值带宽的月度预留成本约为¥20,000-40,000，具体取决于运营商（电信/联通/移动）及是否包含BGP多线接入，此成本远高于按流量计费模式下的同等流量成本

## Corrected Claim

在公有云按峰值带宽计费模式下，10Gbps峰值带宽的月度成本通常显著高于按流量计费模式下的同等流量成本，具体金额因云厂商、地域及合约类型而异，需参考具体厂商报价。

## Evidence

[质询]具体数值区间（¥20,000-40,000）属于经验事实，不同云厂商（如阿里云、腾讯云、AWS）及不同时期价格差异巨大，且10Gbps带宽在公有云通常需通过BGP多线或特定专线实现，单一运营商直连10Gbps在公有云标准产品中较少见，该数值可能基于特定厂商或特定促销/长期合约价格，缺乏普适性。 | 来源[1]仅提及计费模式分类，未提供具体价格数值，无法直接支持该经验事实；逻辑上按峰值计费确实通常高于按流量计费（针对突发流量场景），但具体金额缺乏外部证据支持。

## Search Query

China cloud CDN peak bandwidth pricing 10Gbps monthly cost telecom operator

## Retrieval Sources

- {'url': 'https://cloud.baidu.com/article/5133424&rut=090a1f84a501a5cf221162e1ad868a91a4c053723e5d36b8010581f4b7b5db81', 'type': 'ddg', 'title': '流媒体CDN带宽费用计算全解析：成本优化与策略选择'}
