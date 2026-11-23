# N22: 用户地理分布长尾度：剩余 90% 流量分布在非核心区域的请求占比（%），决定混合策略中长尾公有云流量比例

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

用户地理分布长尾度：剩余 90% 流量分布在非核心区域的请求占比（%），决定混合策略中长尾公有云流量比例

## Corrected Claim

用户地理分布通常呈现长尾特征，但具体剩余90%流量分布在非核心区域的占比需依据实际业务数据确定，现有来源未提供直接证据。

## Evidence

[质询]来源[1]和[2]讨论的是SEO/营销领域的“长尾关键词”流量占比，而非云计算或网络服务中“用户地理分布”的长尾度。将营销长尾词占比（90%）直接等同于地理分布长尾度（90%）属于概念混淆和口径错误，且来源未提供地理分布的具体数据支持。 | 来源[1][2]主题相关度低（营销长尾词 vs 地理分布），且数值90%在来源中对应的是长尾词流量占比而非地理分布占比，无法直接支持该事实，但逻辑上长尾分布存在是合理的，故降级。

## Search Query

China CDN traffic distribution long-tail regions percentage outside top 10 cities

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/907882250_122424952&rut=dc149c05d7829168bf85178310beec4d26c4b0d12a8d7c225d81945931233ed9', 'type': 'ddg', 'title': '长尾流量占比90%!百模晓教你挖掘细分领域隐藏客户的秘诀_大词_品牌_用户'}
- {'url': 'https://www.sohu.com/a/1020315174_120116647&rut=5fef7194f815f6b90d5ec2cfa90f50a999825f328e517d497cf3a9dbea5fa26f', 'type': 'ddg', 'title': '"地名+服务"的长尾流量池：帮你挖出90%的本地精准订单_搜索_商家_用户'}
