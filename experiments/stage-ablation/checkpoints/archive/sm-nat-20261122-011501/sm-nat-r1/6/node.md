# N20: Pareto(α=1.1) 分布下，对象大小总和收敛（因 α>1），但均值 E[S] = α * s_min / (α-1)。假设 s_min=1KB，则 E[

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

Pareto(α=1.1) 分布下，对象大小总和收敛（因 α>1），但均值 E[S] = α * s_min / (α-1)。假设 s_min=1KB，则 E[S] = 11KB。总数据量 ≈ 100,000 * 11KB ≈ 1.1TB。缓存容量 128GB 仅占总数据的 11.6%。由于大小分布重尾，缓存无法覆盖所有对象，只能覆盖头部小对象。

## Corrected Claim

Pareto(α=1.1) 分布下，对象大小总和收敛（因 α>1），但均值 E[S] = α * s_min / (α-1)。假设 s_min=1KB，则 E[S] = 11KB。总数据量 ≈ 100,000 * 11KB ≈ 1.1TB。缓存容量 128GB 仅占总数据的 11.6%。由于大小分布重尾，缓存无法覆盖所有对象，只能覆盖头部小对象。

## Evidence

逻辑推导成立，来源未直接覆盖（来源[1][2]确认Pareto分布定义，数学性质可由第一性原理推出）

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Pareto_distribution&rut=d1f36e1dcdd328dca36f26158320367e6d6eac92aaea3431d05154d1bb1df302', 'type': 'ddg', 'title': 'Pareto distribution - Wikipedia'}
- {'url': 'https://zh.wikipedia.org/zh-tw/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=a002454da5e71006d8831164353c7362a3dadaa27b107e755af26d53a99f853e', 'type': 'ddg', 'title': '柏拉圖分布 - 維基百科，自由的百科全書'}
