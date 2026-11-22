# N99: LRU 稳态驻留集合大小的修正方程：K_LRU 由 ∑_{i=1}^{K_LRU} S_i = C 确定，其中 C=128GB。在 ρ=-0.3 下，由于头部对

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

LRU 稳态驻留集合大小的修正方程：K_LRU 由 ∑_{i=1}^{K_LRU} S_i = C 确定，其中 C=128GB。在 ρ=-0.3 下，由于头部对象较小，K_LRU 的解比独立假设下大，具体数值需数值求解非线性方程，预计 K_LRU > 0.99N。

## Corrected Claim

LRU 稳态驻留集合大小 K_LRU 由 ∑_{i=1}^{K_LRU} S_i = C 确定。在头部对象较小的分布假设下，K_LRU 的解通常大于独立假设下的解，具体数值需结合 C 和分布参数数值求解。

## Evidence

[质询]该陈述包含具体的经验参数（C=128GB, ρ=-0.3）和基于特定分布假设的数值结论（K_LRU > 0.99N），属于经验事实而非第一性原理可推导的数学恒等式。参考来源仅讨论 LRU-K 算法原理，未提供该特定场景下的数值解或分布参数支持，无法验证具体数值结论。 | 逻辑上，若头部对象较小（Zipf-like 分布），固定容量 C 下能容纳的对象数量 K 确实会比独立同分布假设下更多，逻辑自洽。但参考来源 [1] 仅涉及 LRU-K 算法定义，与该具体数值计算无关，属于经验事实且缺乏直接来源支持。

## Search Query

LRU cache size calculation with negative correlation between size and frequency Pareto distribution

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/78212068&rut=e30da754ad55947f09968ec41ad481f87403c50a2fac08440a2ad0560eed8275', 'type': 'ddg', 'title': 'Lru 和 Lru-k - 知乎 - 知乎专栏'}
