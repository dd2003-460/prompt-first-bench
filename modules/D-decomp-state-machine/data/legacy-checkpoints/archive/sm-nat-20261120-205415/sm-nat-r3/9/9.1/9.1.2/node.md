# N220: LFU与LRU稳态集合差异的基准工作点：在Gaussian Copula(ρ=-0.3)下，通过数值积分计算F△L中对象的平均大小差ΔS_avg与热度差Δh_a

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

LFU与LRU稳态集合差异的基准工作点：在Gaussian Copula(ρ=-0.3)下，通过数值积分计算F△L中对象的平均大小差ΔS_avg与热度差Δh_avg，量化|F△L|对ΔH的贡献项，修正幅度约为-0.5%至-1%。

## Corrected Claim

在特定统计模型（如Gaussian Copula）下，LFU与LRU稳态集合差异对热度贡献的修正幅度可能较小（约-0.5%至-1%），但具体数值依赖于模型参数与数据分布，需具体实验验证。

## Evidence

[质询]该陈述包含极其具体的数值结论（-0.5%至-1%）和特定的统计模型参数（Gaussian Copula, ρ=-0.3），属于经验事实或特定研究结论，无法从第一性原理直接推导。参考来源仅涉及Redis缓存策略的通用科普，未包含任何关于数值积分、Copula模型或具体修正幅度的数据，无法提供外部支持。 | 逻辑上，LFU与LRU在稳态下的集合差异确实会导致热度与大小的统计偏差，修正幅度为负且较小符合直觉；但作为经验事实，缺乏来源直接支持（来源[1]无关），故降级。

## Search Query

Gaussian Copula cache hit rate difference LFU LRU negative correlation Pareto distribution

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=7d58a4a126ac95d842e1a792f5b31de9d44ec9b6d2a091d938002417e9278387', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
