# N283: 公有云CDN控制粒度 N_regions 的精确数值：阿里云中国内地实际可独立配置缓存策略/回源规则的区域数为 31 个省级行政区（部分合并后约 25 个独立配

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N91

## Claim

公有云CDN控制粒度 N_regions 的精确数值：阿里云中国内地实际可独立配置缓存策略/回源规则的区域数为 31 个省级行政区（部分合并后约 25 个独立配置单元）；Cloudflare 全球 Anycast 网络中，用户可自定义 Cache Rules 的地理粒度为 5-10 个预设区域（如 'Asia-Pacific', 'North America'），并非 200 个独立配置点，200 为物理 PoP 数量而非逻辑配置单元数。

## Corrected Claim

阿里云CDN覆盖中国内地等全球区域，拥有数千个节点；其缓存策略通常基于域名或路径配置，支持地域访问控制，但具体可独立配置的省级行政区数量需参考最新产品文档；Cloudflare支持基于地理区域的缓存规则，具体预设区域数量随产品版本更新可能变化，通常包含主要大洲/区域划分。

## Evidence

[质询]阿里云CDN的缓存策略和回源规则通常基于域名（Domain）或路径（Path）进行全局配置，而非直接按“省级行政区”进行独立配置；虽然支持基于地域的访问控制或特定功能，但“31个省级行政区作为独立配置单元”这一具体数值和配置粒度描述缺乏官方文档直接支持，且Cloudflare的Cache Rules地理粒度具体数值（5-10个）也属于经验性描述，未能在提供的来源中得到精确验证。 | 来源[1]和[3]仅提供了阿里云CDN的全球节点分布和覆盖范围（如3200+节点、覆盖中国内地等），未提及具体的“省级行政区独立配置单元数”或“Cloudflare Cache Rules地理粒度”的具体数值，属于经验事实且缺乏直接来源支持。

## Search Query

Alibaba Cloud CDN regional configuration units count Cloudflare cache rules geographic granularity

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/pop-distribution&rut=595d01782e84eb3f196fd24fe446f89853ad8641b852b08195096df39b95249e', 'type': 'ddg', 'title': '全球节点资源规格与覆盖范围-cdn-阿里云'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://www.alibabacloud.com/help/tc/cdn/product-overview/pop-distribution&rut=34c120a6f55567052a7d0a5789adea8ce45264e46c577ced67c626594d2d229b', 'type': 'ddg', 'title': 'CDN全球高效能節點分布與覆蓋地區-CDN-阿里雲 - Alibaba Cloud'}
