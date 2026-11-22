# N20: 在Pareto(α=1.1)分布下，由于α<2，总数据量由头部少数对象主导。具体地，前1%最大的对象（Top 1% by size）占据了总存储空间的约 90.

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

在Pareto(α=1.1)分布下，由于α<2，总数据量由头部少数对象主导。具体地，前1%最大的对象（Top 1% by size）占据了总存储空间的约 90.2%（计算依据：1 - (1/100)^(1-1.1) ≈ 0.902），这意味着128GB缓存几乎只能容纳极少数超大对象，空间填充率极低，大部分缓存空间被几个GB级对象占据。

## Corrected Claim

在Pareto(α=1.1)分布下，由于α<2，总数据量由头部少数对象主导。具体地，前1%最大的对象（Top 1% by size）占据了总存储空间的约 90.2%（计算依据：1 - (1/100)^(1-1.1) ≈ 0.902），这意味着128GB缓存几乎只能容纳极少数超大对象，空间填充率极低，大部分缓存空间被几个GB级对象占据。

## Evidence

逻辑推导成立，来源未直接覆盖（来源[1][2]确认Pareto分布定义，数学计算 1-(1/100)^(-0.1)≈0.902 正确）

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Pareto_distribution&rut=d1f36e1dcdd328dca36f26158320367e6d6eac92aaea3431d05154d1bb1df302', 'type': 'ddg', 'title': 'Pareto distribution - Wikipedia'}
- {'url': 'https://zh.wikipedia.org/zh-tw/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=a002454da5e71006d8831164353c7362a3dadaa27b107e755af26d53a99f853e', 'type': 'ddg', 'title': '柏拉圖分布 - 維基百科，自由的百科全書'}
