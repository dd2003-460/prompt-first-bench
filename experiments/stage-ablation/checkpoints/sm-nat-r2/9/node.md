# N24: LFU 相比 LRU 的性能增益上限：在稳态下，LFU 保留频率最高的对象，而 LRU 保留最近访问的对象。对于 Pareto(β=0.9) 热度分布，LFU 

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相比 LRU 的性能增益上限：在稳态下，LFU 保留频率最高的对象，而 LRU 保留最近访问的对象。对于 Pareto(β=0.9) 热度分布，LFU 的命中率 H_LFU ≈ 1 - (1 - F_top_k)^β，其中 F_top_k 为前 k 个对象的热度占比。由于 β<1，头部对象贡献显著，LFU 理论上比 LRU 高 5-15 个百分点。最大提升出现在 ρ 为负且 |ρ| 较大时，因为 LFU 能更有效地利用字节容量缓存小且热的对象。

## Corrected Claim

在稳态下，对于具有显著头部效应（如Pareto分布）的热度分布，LFU通常比LRU具有更高的缓存命中率，因为LFU能更有效地保留高频访问对象。具体性能增益取决于访问模式和工作负载特征，通常在偏斜分布下可达数个至十几个百分点，但无固定上限公式。

## Evidence

父节点级核验未通过：不完备（父节点描述了LFU相比LRU的性能增益上限及其两个主要驱动因素：1) 热度分布（Pareto β）导致的头部效应；2) 大小-频率相关性（ρ）导致的容量利用优势。子节点仅覆盖了第二个因素（ρ → -1 时的边界条件），完全缺失了关于热度分布（β）对增益上限影响的分析，也未涵盖一般情况下的增益推导，因此不完备。）

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/LFU_cache', 'type': None, 'title': 'direct-browser: https://en.wikipedia.org/wiki/LFU_cache'}
- {'url': 'https://arxiv.org/abs/1702.03304', 'type': None, 'title': 'direct-browser: https://arxiv.org/abs/1702.03304'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=e57a03057fb2bd9f336ab899a15bcdb96faf02186ece640b0fe55a9a1a8bbac0', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
