# N73: LRU 缓存中对象 i 的驻留时间窗口 W_i 的精确计算：W_i 不是全局常数，而是取决于对象 i 被替换前的累积请求数。对于排名 i 的对象，其被替换的临界

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

LRU 缓存中对象 i 的驻留时间窗口 W_i 的精确计算：W_i 不是全局常数，而是取决于对象 i 被替换前的累积请求数。对于排名 i 的对象，其被替换的临界请求数 M_i 由缓存容量 C 和对象大小分布决定。若假设大小独立，W_i ≈ C / (S_i * λ_i) 是错误的，正确逻辑是：LRU 栈中深度为 d 的对象，其 W 对应于该深度处所有对象的平均访问间隔倒数之和的倒数。简化模型下，W_i ≈ K / (λ_i * N_eff)，其中 K 为可缓存对象数，需迭代求解。

## Corrected Claim

LRU 缓存中对象 i 的驻留时间窗口 W_i 取决于其被替换前的累积请求数（或栈距离），并非全局常数。精确计算需基于访问序列或概率模型（如 IRM）进行迭代或静态分析，简单的 W_i ≈ K / (λ_i * N_eff) 仅在特定简化假设下近似成立，不具备普适性。

## Evidence

[质询]陈述中给出的简化公式 W_i ≈ K / (λ_i * N_eff) 缺乏明确的理论推导支持，且将复杂的 LRU 驻留时间（通常涉及栈距离分布或累积请求数）简化为与有效对象数 N_eff 成反比的形式，在一般独立参考模型（IRM）下并不成立，属于过度简化的经验性近似，容易误导对 LRU 动态行为的理解。 | 来源 [2] 确认 LRU 分析存在精确性与效率的权衡，但未直接支持该特定简化公式；来源 [1] 仅介绍 LRU 基本原理。该陈述逻辑上自洽（指出 W_i 非全局常数），但具体公式缺乏直接来源支持，且属于经验/模型假设范畴，故降级。

## Search Query

LRU cache residence time formula dependent on request rate and object size

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/161269766&rut=f8b3c2f4662a3b96e82928ec32c760bf519173056b562900244e4318262aa288', 'type': 'ddg', 'title': 'Lru原理与算法实现 - 知乎专栏'}
- {'url': 'http://arxiv.org/abs/1811.01670v2', 'type': 'arxiv', 'title': 'Fast and exact analysis for LRU caches'}
