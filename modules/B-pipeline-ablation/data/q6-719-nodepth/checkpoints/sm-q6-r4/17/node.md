# N426: 自建边缘节点架构拓扑特征：固定 10 个 POP 点，流量分发需自建调度系统（如基于 GeoIP 的 DNS 轮询或 L4 负载均衡），核心区域 POP 承载 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

自建边缘节点架构拓扑特征：固定 10 个 POP 点，流量分发需自建调度系统（如基于 GeoIP 的 DNS 轮询或 L4 负载均衡），核心区域 POP 承载 60-80% 流量，长尾区域依赖回源或公有云兜底，P99 延迟受限于 POP 覆盖密度与本地网络质量，具备更高的可控性但缺乏弹性。

## Corrected Claim

自建边缘节点架构通常具备更高的可控性但缺乏弹性，流量分发需自建调度系统（如基于 GeoIP 的 DNS 或 L4 负载均衡），P99 延迟受限于 POP 覆盖密度与本地网络质量；具体 POP 数量及流量分布比例（如核心区域占比）取决于业务规模与地域分布，非固定值。

## Evidence

[质询]陈述中关于“固定 10 个 POP 点”和“核心区域 POP 承载 60-80% 流量”的具体数值属于特定场景下的经验性假设或特定案例数据，并非自建边缘节点的通用架构特征或第一性原理必然结论，缺乏普适性来源支持。 | 来源[1]和[2]仅涉及 CDN/边缘计算的一般架构概念（如 POP 定义、分层结构、算力下沉），未提供关于具体 POP 数量、流量分布比例或特定调度策略（如 GeoIP DNS 轮询）的直接数据支持，属于经验事实且缺来源支持。

## Retrieval Sources

- {'url': 'https://infi.cn/articles/cdn-architecture-diagram-content-delivery-network-design.html&rut=0391149b598c99136997f8c61145e1449a91372bbe3ed97737aadfab7ba647ec', 'type': 'ddg', 'title': 'Cdn架构图绘制：内容分发网络设计 - 英飞思想家'}
- {'url': 'https://jishuzhan.net/article/2087175092588396545&rut=173c5104555b563289cd6604c00063cbb6a69bdca160bb273d7e316873b34e23', 'type': 'ddg', 'title': '边缘计算架构：算力下沉的设计挑战 - 技术栈'}
