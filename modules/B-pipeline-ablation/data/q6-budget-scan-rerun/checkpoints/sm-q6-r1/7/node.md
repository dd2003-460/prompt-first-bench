# N35: 缓存命中率 (Cache Hit Ratio, CHR) 对带宽成本的影响模型：公有云 CDN 典型 CHR 为 85%-95%（因边缘节点多且共享缓存），自建

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

缓存命中率 (Cache Hit Ratio, CHR) 对带宽成本的影响模型：公有云 CDN 典型 CHR 为 85%-95%（因边缘节点多且共享缓存），自建 10 POP 点因节点少且流量分散，典型 CHR 为 60%-75%。实际回源带宽 B_origin = B_total * (1 - CHR)。CHR 每降低 10%，回源带宽成本增加约 15-20%（取决于回源单价与边缘单价差异）。

## Corrected Claim

缓存命中率 (CHR) 对带宽成本有显著影响，回源带宽 B_origin = B_total * (1 - CHR)。公有云 CDN 通常因节点多、缓存共享度高而拥有较高的 CHR，自建少量 POP 点通常 CHR 较低。具体数值范围及成本敏感度需根据实际业务流量特征和定价策略测算，典型参考值需结合具体案例验证。

## Evidence

[质询]具体数值区间（公有云85-95%，自建60-75%）及成本敏感度（10%命中率降低导致15-20%成本增加）属于经验性工程数据，缺乏通用理论支持，且受具体业务流量分布、对象大小、TTL策略等影响极大，不同场景下差异显著，不能一概而论。 | 来源[3]仅定义CDN缓存命中率概念，未提供具体数值范围或成本模型；来源[1][2]讨论的是计算机体系结构中的CPU Cache，与CDN网络带宽成本无关。该陈述中的具体数值为经验事实，逻辑自洽但缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28309571/article/details/158051568&rut=08dad2f783b89a59ce498f9b616e7eb4cddbc40bbd2693fffba6cc86c7964e65', 'type': 'ddg', 'title': '手把手教你计算Cache命中率：从理论到Wireshark实战分析-CSDN博客'}
- {'url': 'https://blog.csdn.net/xiong_xin/article/details/143781620&rut=1283d34bf0cc897fae57f4d68b471f03efbb242f7497f85604defaeff4339257', 'type': 'ddg', 'title': 'cache中命中率和缺失率_cache hit rate-CSDN博客'}
- {'url': 'https://www.cloudflare.com/zh-cn/learning/cdn/what-is-a-cache-hit-ratio/&rut=0c72a820b0f7ce42a20a37ab8edc35701c4b16d1087605d179ce450c7c87f325', 'type': 'ddg', 'title': '什么是缓存命中率？ | Cloudflare'}
