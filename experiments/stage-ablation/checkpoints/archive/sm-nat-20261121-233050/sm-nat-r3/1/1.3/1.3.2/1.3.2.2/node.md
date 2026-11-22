# N86: LFU 缓存集合在 ρ=-0.3 下的字节覆盖量 B_LFU：基于 N59 确定的 K_max≈98,500 个对象，B_LFU = Σ_{i∈Top_K_by

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

LFU 缓存集合在 ρ=-0.3 下的字节覆盖量 B_LFU：基于 N59 确定的 K_max≈98,500 个对象，B_LFU = Σ_{i∈Top_K_by_Freq} S_i * F_i，由于负相关性，该集合包含高频小对象，估算值约为 Total_Bytes * 0.95 [待核验]。

## Corrected Claim

LFU 缓存集合在 ρ=-0.3 下的字节覆盖量 B_LFU 估算值约为 Total_Bytes 的 95%（基于特定分布假设的经验估算，缺乏通用理论或来源直接支持）。

## Evidence

[质询]该陈述包含具体的经验性数值估算（0.95），且依赖于特定的负相关系数（ρ=-0.3）和对象分布假设。参考来源仅讨论Redis中LRU与LFU的算法原理及实现差异，未提供关于特定负相关场景下字节覆盖量的量化数据或公式推导，无法直接支持该具体数值。 | 逻辑上，LFU基于频率选择对象，若存在负相关（高频小对象），Top-K频率集合确实可能覆盖大部分字节（因为小对象数量多，累积字节可能大，或者反之，取决于具体分布，但0.95是一个合理的经验估算量级）。然而，来源[1]仅涉及算法原理，未覆盖此特定统计估算，属于经验事实且缺乏直接来源支持。

## Search Query

LFU cache byte coverage Pareto distribution negative correlation simulation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/641841636&rut=96c5bc09c47f8a549e8849194645b4663ac2be524195b61a9f699c4474f03ff2', 'type': 'ddg', 'title': '深入解析Redis的LRU与LFU算法实现 - 知乎'}
