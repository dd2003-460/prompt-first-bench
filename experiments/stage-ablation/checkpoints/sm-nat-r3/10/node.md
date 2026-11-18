# N25: LFU 机制差异解释：LFU 基于长期频率，对突发访问不敏感，但在对象热度稳定时更优。LRU 基于最近性，对突发访问敏感，但在热度漂移时更优。在本问题中，由于热

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 机制差异解释：LFU 基于长期频率，对突发访问不敏感，但在对象热度稳定时更优。LRU 基于最近性，对突发访问敏感，但在热度漂移时更优。在本问题中，由于热度服从 Pareto 分布且无显著漂移假设，LFU 的增益主要来自其能更精确地匹配字节容量与热度分布，避免缓存大而冷或小而热的对象。具体增益 ΔH = H_LFU - H_LRU ≈ 0.08 - 0.12（8-12 个百分点）。

## Corrected Claim

LFU 基于长期频率，对突发访问不敏感，但在对象热度稳定时更优；LRU 基于最近性，对突发访问敏感，但在热度漂移时更优。在本问题中，由于热度服从 Pareto 分布且无显著漂移假设，LFU 的增益主要来自其能更精确地匹配字节容量与热度分布，避免缓存大而冷或小而热的对象。具体增益 ΔH = H_LFU - H_LRU 取决于具体分布参数，通常表现为显著优于 LRU 的命中率提升。

## Evidence

[质询]具体数值增益（8-12个百分点）缺乏来源支持，且该数值高度依赖于具体的Pareto分布参数、对象大小分布及缓存容量，属于经验事实而非第一性原理可推导的通用结论。 | 来源[1]和[2]定性支持了LRU/LFU在突发访问与稳定热度下的机制差异（间接支持），但均未提供具体的量化增益数值（8-12%），该数值属于经验事实，逻辑自洽但缺来源直接支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=e57a03057fb2bd9f336ab899a15bcdb96faf02186ece640b0fe55a9a1a8bbac0', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
- {'url': 'http://arxiv.org/abs/2609.07566v3', 'type': 'arxiv', 'title': 'No-Regret Mixing of LRU and LFU with Optimal Switching Cost'}
