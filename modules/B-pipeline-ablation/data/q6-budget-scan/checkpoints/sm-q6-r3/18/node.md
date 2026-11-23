# N375: 在中国大陆运营C端视频平台，CDN节点需具备ICP备案及公安备案资格，公有云CDN自动继承云厂商资质，而自建节点需独立申请ICP许可证（周期约20-30个工作日

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在中国大陆运营C端视频平台，CDN节点需具备ICP备案及公安备案资格，公有云CDN自动继承云厂商资质，而自建节点需独立申请ICP许可证（周期约20-30个工作日）；若未备案导致节点被封锁，平均恢复时间MTTR为4-8小时，期间所有流量需切换至备用合规节点，导致P99延迟飙升且产生额外带宽切换成本。

## Corrected Claim

在中国大陆运营C端视频平台，CDN节点需具备ICP备案及公安备案资格，公有云CDN通常继承云厂商资质，而自建节点需独立申请ICP许可证；若未备案导致节点被封锁，需切换至备用合规节点，期间可能产生延迟增加及额外带宽成本，具体恢复时间视运营商处理效率而定。

## Evidence

[质询]陈述中关于“MTTR为4-8小时”、“P99延迟飙升”及“额外带宽切换成本”的具体数值和后果描述属于经验性运营数据，参考来源仅覆盖ICP备案的合规要求，未提供此类故障恢复时间或性能影响的具体数据支持，存在将一般性运维经验绝对化的风险。 | 来源[1][2][3]直接支持了CDN节点需ICP备案及公有云/自建节点备案差异的合规逻辑，但缺乏对MTTR具体时长及故障期间性能/成本影响的直接数据支持，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/icp-filing/basic-icp-service/product-overview/use-alibaba-cloud-cdn&rut=c9dc5cf6a45bd7b00b33e209513f61179d9932b44bd6e2dd0c429c20cc829f63', 'type': 'ddg', 'title': '使用阿里云cdn加速域名的icp备案要求-备案-阿里云'}
- {'url': 'https://edgeone.ai/zh/blog/details/the-ultimate-guide-to-icp-filing&rut=1df6a2d567ea70213437e11b8f05a969e0d3a5976e55ce4f137eb673c53d707b', 'type': 'ddg', 'title': '终极ICP备案指南：如何合法部署您的网站与中国CDN'}
- {'url': 'https://help.aliyun.com/zh/icp-filing/basic-icp-service/product-overview/icp-filing-requirements-for-a-regular-website&rut=cb8bad2e72c18d9c7dc6717f3fa41e870e3cb4ba8cea6be483c88970d8955191', 'type': 'ddg', 'title': '常见网站的ICP备案场景及备案要求-备案 (Filing Service)-阿里云帮助中心'}
