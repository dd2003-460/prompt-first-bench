# N175: 架构迁移成本（Migration Cost）：从公有云CDN迁移至自建节点或反之，主要成本在于DNS切换期间的缓存预热（Cache Warming）和回源风暴。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

架构迁移成本（Migration Cost）：从公有云CDN迁移至自建节点或反之，主要成本在于DNS切换期间的缓存预热（Cache Warming）和回源风暴。缓存预热需预加载Top 20%热点内容（约占80%流量），预计耗时24-48小时，期间需双倍带宽成本；此外，配置迁移（规则、证书、日志格式）的人力成本约为¥50k-100k（一次性）。

## Corrected Claim

架构迁移成本主要在于DNS切换期间的缓存预热和回源风暴。缓存预热通常需预加载热点内容（具体比例视业务而定，常引用80/20法则），耗时及带宽成本取决于内容规模；配置迁移的人力成本因复杂度而异，需具体评估。

## Evidence

[质询]具体数值（Top 20%占80%流量、24-48小时预热、¥50k-100k人力成本）属于高度依赖具体业务场景的经验数据，缺乏通用性，且参考来源未提供这些具体参数，存在以偏概全或数据无据的风险。 | 逻辑自洽（缓存预热和回源风暴确实是迁移主要成本，80/20法则在CDN场景常见），但参考来源[1][2]仅讨论云迁移通用成本框架，未涉及CDN特定迁移细节及具体数值，属于经验事实且缺直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_34129696/article/details/88831581&rut=0ef3f76f092b2d6a3869d612fd047021f1b9225621c6443173b9d522be272a8c', 'type': 'ddg', 'title': '云迁移成本计算-csdn博客'}
- {'url': 'https://blog.csdn.net/newtyun/article/details/116677789&rut=9187c4b610332b50f0606d8d5551cc1c8ffdd290ea2e249c6d06167ddb753f2d', 'type': 'ddg', 'title': '云迁移成本计算与策略-csdn博客'}
