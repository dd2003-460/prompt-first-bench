# N85: 对于 LRU 策略，更新导致的命中率折损系数 δ_update = 1 - exp(-u * T_avg_residency)，其中 T_avg_residen

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于 LRU 策略，更新导致的命中率折损系数 δ_update = 1 - exp(-u * T_avg_residency)，其中 T_avg_residency 是缓存中对象从插入到被替换的平均时间；在稳态下，T_avg_residency ≈ C / (S_avg * R_miss)，需迭代求解。

## Corrected Claim

在假设对象驻留时间服从指数分布的特定LRU缓存模型中，更新导致的命中率折损系数可近似表示为 δ_update = 1 - exp(-u * T_avg_residency)，其中 T_avg_residency ≈ C / (S_avg * R_miss) 需在稳态下迭代求解。

## Evidence

[质询]该公式属于特定缓存模型（如基于指数分布驻留时间的LRU近似）的经验性推导，并非LRU策略的通用第一性原理定义；且参考来源与缓存算法完全无关，无法提供外部支持。 | 逻辑自洽（量纲与稳态关系合理），但参考来源[1]为光谱学论文，与缓存命中率无关，属经验事实且缺来源支持。

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/1806.07361v3', 'type': 'arxiv', 'title': 'Comparing the emission spectra of U and Th hollow cathode lamps and a new U line'}
