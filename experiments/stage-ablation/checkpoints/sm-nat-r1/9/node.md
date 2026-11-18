# N24: LFU 相比 LRU 的性能增益上限：在稳态下，LFU 保留频率最高的对象，而 LRU 保留最近访问的对象。对于 Pareto(β=0.9) 热度分布，LFU 

- **status**: degraded
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

[质询]陈述中给出的命中率公式 H_LFU ≈ 1 - (1 - F_top_k)^β 在数学上缺乏严谨推导支持，且将复杂的缓存替换策略简化为单一静态公式存在逻辑跳跃；此外，'5-15个百分点'的具体数值增益属于经验性断言，缺乏通用理论保证，且参考来源中未包含支持该具体数值或公式的直接证据。 | 来源[4]仅定性描述了LRU与LFU的区别（LRU看最近，LFU看频率），未提供具体命中率公式或5-15%的量化增益数据；来源[1]为Wikipedia不存在页面提示，来源[2]和[3]与缓存算法无关。该陈述属于经验事实与特定模型推导，逻辑上自洽（LFU在偏斜分布下通常优于LRU），但缺乏来源直接支持具体数值和公式，故降级。

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/LFU_cache', 'type': None, 'title': 'direct-browser: https://en.wikipedia.org/wiki/LFU_cache'}
- {'url': 'https://arxiv.org/abs/1702.03304', 'type': None, 'title': 'direct-browser: https://arxiv.org/abs/1702.03304'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=e57a03057fb2bd9f336ab899a15bcdb96faf02186ece640b0fe55a9a1a8bbac0', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
