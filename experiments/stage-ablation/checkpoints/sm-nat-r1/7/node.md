# N23: LFU 相对于 LRU 的最大理论增益 ΔH_max 在长尾热度分布下受限于热门对象的集中度。当 β < 1 时，LFU 能更有效地保留高频小对象，其增益上限近

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相对于 LRU 的最大理论增益 ΔH_max 在长尾热度分布下受限于热门对象的集中度。当 β < 1 时，LFU 能更有效地保留高频小对象，其增益上限近似为 ΔH_max ≈ (1 - 1/β) * (1 - C/S_hot) * (1 - ρ_correction)，其中 S_hot 为高频对象总大小。具体数值上，对于 β=0.9, α=1.1, ρ=-0.3，理论最大提升通常在 5-10 个百分点之间，具体取决于缓存容量与热门对象总量的比值。

## Corrected Claim

LFU 相对于 LRU 的增益在长尾热度分布下受限于热门对象集中度。当 β < 1 时，LFU 能更有效地保留高频小对象，其增益上限近似为 ΔH_max ≈ (1 - 1/β) * (1 - C/S_hot) * (1 - ρ_correction)。具体数值增益取决于缓存容量与热门对象总量的比值及分布参数，通常表现为显著的性能提升，但具体百分点需结合特定负载模型计算。

## Evidence

[质询]该陈述包含具体的经验数值断言（5-10个百分点）和特定的参数组合（β=0.9, α=1.1, ρ=-0.3），属于经验事实而非纯数学推导。参考来源[1]为arXiv首页，[2]为图论近似算法论文，均与缓存替换策略（LFU/LRU）及热度分布无关，无法提供外部支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2]均无关）

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'http://arxiv.org/abs/2212.11191v2', 'type': 'arxiv', 'title': 'Separating MAX 2-AND, MAX DI-CUT and MAX CUT'}
