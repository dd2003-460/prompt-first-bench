# N80: LFU 在热度漂移下的性能衰减率：若热度分布以速率 δ 漂移（即 Pareto 指数 β(t) = β_0 + δ*t），LFU 的命中率衰减速度比 LRU 快

- **status**: degraded
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

[质询]该陈述包含具体的数学推导结论（LFU在热度漂移下衰减比LRU快）及特定公式，属于经验/理论混合事实。参考来源[3]仅介绍了LRU和LFU的基本定义，未涉及热度漂移（Pareto指数变化）下的性能对比或微分公式，无法提供直接支持。虽然逻辑上LFU对历史频率敏感，在分布变化时确实可能比LRU（对近期时间敏感）更慢适应，但具体量化公式 dH_LFU/dt ≈ -δ * ∂H/∂β 缺乏来源验证，且“衰减速度比LRU快”这一比较性结论在缺乏具体模型假设（如LRU的敏感度）时属于未证实的经验断言。 | 来源[3]仅定义算法，未覆盖热度漂移下的性能衰减率及具体公式，属于经验事实且缺来源直接支持，逻辑上LFU对分布变化敏感是合理的，但具体量化关系无法从现有来源验证。

## Search Query

LFU cache performance degradation under popularity drift

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: https://github.com'}
- {'url': 'https://zhuanlan.zhihu.com/p/686994451&rut=ce880e6f5290907748a63f8411f1be25b7764ef8de31379055d785f85105f74b', 'type': 'ddg', 'title': '缓存数据淘汰算法: Lru 和 Lfu - 知乎'}
