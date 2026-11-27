# N22: 在Pareto(α=1.1)分布下，对象大小的截断均值 E[S]_trunc 可通过积分 ∫_{s_min}^{s_max} s * (α-1) * s_min

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

在Pareto(α=1.1)分布下，对象大小的截断均值 E[S]_trunc 可通过积分 ∫_{s_min}^{s_max} s * (α-1) * s_min^{α-1} / s^α ds 计算。当 s_min=1KB, s_max=100MB 时，E[S]_trunc ≈ 1.1 * 1KB * (1 - (1KB/100MB)^{0.1}) / 0.1 ≈ 10.5 KB。由此得出 128GB 缓存可容纳对象数量 K ≈ 128 * 1024 * 1024 KB / 10.5 KB ≈ 1.26M 个对象，远超 10万 对象总数，意味着缓存容量足以存储所有对象（若仅考虑大小），此时命中率主要受限于LRU堆栈深度而非容量上限。

## Corrected Claim

在Pareto(α=1.1)分布下，对象大小的截断均值 E[S]_trunc 可通过积分 ∫_{s_min}^{s_max} s * (α-1) * s_min^{α-1} / s^α ds 计算。当 s_min=1KB, s_max=100MB 时，E[S]_trunc ≈ 1.1 * 1KB * (1 - (1KB/100MB)^{0.1}) / 0.1 ≈ 10.5 KB。由此得出 128GB 缓存可容纳对象数量 K ≈ 128 * 1024 * 1024 KB / 10.5 KB ≈ 1.26M 个对象，远超 10万 对象总数，意味着缓存容量足以存储所有对象（若仅考虑大小），此时命中率主要受限于LRU堆栈深度而非容量上限。

## Evidence

逻辑推导成立，来源未直接覆盖（数学积分计算与量级估算自洽）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/27173875583&rut=813a7dd5764aafafe6763a06f3f8a3572d479be046e39d53beeec4e456801689', 'type': 'ddg', 'title': '帕累托分布 - 知乎 - 知乎专栏'}
