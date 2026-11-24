# N48: 公有云 CDN 节点密度指标：阿里云/Cloudflare 在中国/全球拥有 >1000 个边缘节点，而自建 10 个 POP 的覆盖半径平均约为 500km，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

公有云 CDN 节点密度指标：阿里云/Cloudflare 在中国/全球拥有 >1000 个边缘节点，而自建 10 个 POP 的覆盖半径平均约为 500km，导致长尾区域用户到最近节点的物理距离增加 200-400km，RTT 增加 10-20ms。

## Corrected Claim

公有云 CDN 节点密度指标：阿里云在中国/全球拥有 >1000 个边缘节点（来源显示为3200+），而自建 10 个 POP 的覆盖半径平均约为 500km，导致长尾区域用户到最近节点的物理距离增加 200-400km，RTT 增加 10-20ms（此部分为经验估算，缺乏直接来源支持）。

## Evidence

[质询]陈述中关于自建10个POP导致RTT增加10-20ms的具体数值缺乏来源支持，且阿里云节点数量（3200+）与陈述中的阈值（>1000）虽兼容但非直接对应，Cloudflare数据完全缺失。 | 来源[1][2]直接支持阿里云拥有>1000个节点（实际为3200+），但关于自建POP覆盖半径及RTT增加的具体经验数值无来源支持，属于经验事实缺来源。

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/pop-distribution&rut=595d01782e84eb3f196fd24fe446f89853ad8641b852b08195096df39b95249e', 'type': 'ddg', 'title': '全球节点资源规格与覆盖范围-cdn-阿里云'}
- {'url': 'https://www.alibabacloud.com/help/zh/cdn/product-overview/pop-distribution&rut=773c801dd19eeb228983bb4636dbb9f0a7a0df6488fc92afaf34a79b1c5086c6', 'type': 'ddg', 'title': '全球节点分布与覆盖范围 - CDN - 阿里云 - Alibaba Cloud'}
- {'url': 'https://www.alibabacloud.com/help/tc/cdn/product-overview/pop-distribution&rut=34c120a6f55567052a7d0a5789adea8ce45264e46c577ced67c626594d2d229b', 'type': 'ddg', 'title': 'CDN全球高效能節點分布與覆蓋地區-CDN-阿里雲 - Alibaba Cloud'}
