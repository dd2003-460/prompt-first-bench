# N80: LFU 在热度漂移下的性能衰减率：若热度分布以速率 δ 漂移（即 Pareto 指数 β(t) = β_0 + δ*t），LFU 的命中率衰减速度比 LRU 快

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

LFU 在热度漂移下的性能衰减率：若热度分布以速率 δ 漂移（即 Pareto 指数 β(t) = β_0 + δ*t），LFU 的命中率衰减速度比 LRU 快。量化为 dH_LFU/dt ≈ -δ * ∂H/∂β，其中 ∂H/∂β 为命中率对热度的敏感度。

## Corrected Claim

LFU 算法基于访问频率，当请求热度分布发生漂移时，其命中率可能会因频率统计滞后而受到影响，具体衰减率取决于热度分布变化的速率及算法参数，通常认为其对分布变化的适应性不如基于时间的 LRU 算法灵活，但具体量化公式需结合特定模型推导。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了LFU敏感度、LRU敏感度以及LFU特有的滞后效应，三者逻辑独立且互补，共同支撑父节点关于'LFU衰减比LRU快'的量化论证。虽然敏感度公式形式相似，但物理意义和参数不同（K值差异及滞后项），不构成冗余。）

## Search Query

LFU cache performance degradation under popularity drift

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: https://github.com'}
- {'url': 'https://zhuanlan.zhihu.com/p/686994451&rut=ce880e6f5290907748a63f8411f1be25b7764ef8de31379055d785f85105f74b', 'type': 'ddg', 'title': '缓存数据淘汰算法: Lru 和 Lfu - 知乎'}
