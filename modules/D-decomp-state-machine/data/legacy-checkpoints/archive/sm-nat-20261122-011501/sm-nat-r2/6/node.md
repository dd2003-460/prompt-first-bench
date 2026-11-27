# N20: Pareto(α=1.1) 分布下，对象大小总和收敛（因 α>1），但均值 E[S] = α * s_min / (α-1)。假设 s_min=1KB，则 E[

- **status**: pending
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

父节点级核验未通过：不完备（子节点在数学修正（截断均值）和参数敏感度（s_min变化）上正交且无冗余。但父节点明确指出了'缓存无法覆盖所有对象，只能覆盖头部小对象'这一基于重尾分布的结构性结论，而两个子节点仅讨论了数值计算修正和参数敏感性，未单独分解'重尾分布导致的头部/尾部覆盖不对称性'或'命中率与对象大小分布的具体耦合机制'，因此未完全覆盖父节点中关于分布形态对缓存策略影响的定性/结构性方面。）

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Pareto_distribution&rut=d1f36e1dcdd328dca36f26158320367e6d6eac92aaea3431d05154d1bb1df302', 'type': 'ddg', 'title': 'Pareto distribution - Wikipedia'}
- {'url': 'https://zh.wikipedia.org/zh-tw/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=a002454da5e71006d8831164353c7362a3dadaa27b107e755af26d53a99f853e', 'type': 'ddg', 'title': '柏拉圖分布 - 維基百科，自由的百科全書'}
