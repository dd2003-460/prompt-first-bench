# N35: 缓存命中率 (Cache Hit Ratio, CHR) 对带宽成本的影响模型：公有云 CDN 典型 CHR 为 85%-95%（因边缘节点多且共享缓存），自建

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了公有云CHR、自建CHR、混合策略CHR以及成本敏感度分析四个维度。虽然混合策略节点引用了前两者的数值，但其核心在于提供一个新的计算模型（加权平均），与前两个节点的“决定因素”侧重点不同，且成本敏感度节点独立于CHR计算本身，专注于经济影响，因此正交性良好。父节点中提到的“公有云”和“自建”典型值及“回源带宽公式/成本敏感度”均被子节点详细展开，完备性高。混合策略虽非父节点原文显式提及，但作为“影响模型”的延伸应用，增强了完整性而非冗余。各节点关注点明确，无实质内容重复。）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28309571/article/details/158051568&rut=08dad2f783b89a59ce498f9b616e7eb4cddbc40bbd2693fffba6cc86c7964e65', 'type': 'ddg', 'title': '手把手教你计算Cache命中率：从理论到Wireshark实战分析-CSDN博客'}
- {'url': 'https://blog.csdn.net/xiong_xin/article/details/143781620&rut=1283d34bf0cc897fae57f4d68b471f03efbb242f7497f85604defaeff4339257', 'type': 'ddg', 'title': 'cache中命中率和缺失率_cache hit rate-CSDN博客'}
- {'url': 'https://www.cloudflare.com/zh-cn/learning/cdn/what-is-a-cache-hit-ratio/&rut=0c72a820b0f7ce42a20a37ab8edc35701c4b16d1087605d179ce450c7c87f325', 'type': 'ddg', 'title': '什么是缓存命中率？ | Cloudflare'}
