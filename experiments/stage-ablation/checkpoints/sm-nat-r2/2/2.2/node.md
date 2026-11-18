# N12: LRU 命中判定逻辑：对象 i 在缓存中当且仅当自上次访问以来的请求数小于 K，即其访问间隔 T_i < K

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 命中判定逻辑：对象 i 在缓存中当且仅当自上次访问以来的请求数小于 K，即其访问间隔 T_i < K

## Corrected Claim

LRU 命中判定逻辑：对象 i 在缓存中当且仅当自上次访问以来的请求数小于 K，即其访问间隔 T_i < K

## Evidence

父节点级核验未通过：不完备（父节点定义的是基于访问间隔 T_i < K 的 LRU 命中判定逻辑（条件/规则），而唯一的子节点讨论的是驻留时间 W_i 的稳态近似公式（性能/分布特性）。子节点并未分解或解释父节点中的核心逻辑（即 T_i 如何计算、K 的定义、命中判定的具体流程），而是引入了一个新的、虽然相关但不同的概念（驻留时间近似）。因此，子节点没有覆盖父节点的关键方面（命中判定逻辑本身），导致完备性不足。）

## Search Query

LRU hit probability access interval
