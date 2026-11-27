# N88: ρ=0（独立情况）下 Top K 对象集合的 Jaccard Index 计算：J(ρ=0) = |Top_K_LRU ∩ Top_K_LFU| / |Top_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

ρ=0（独立情况）下 Top K 对象集合的 Jaccard Index 计算：J(ρ=0) = |Top_K_LRU ∩ Top_K_LFU| / |Top_K_LRU ∪ Top_K_LFU|，在 Pareto 分布下，由于热度与大小独立，两个集合的重叠率约为 0.85 [待核验]。

## Corrected Claim

在 Pareto 分布下，由于热度与大小独立，Top K LRU 与 Top K LFU 集合的 Jaccard Index 取决于 K 值及分布参数，通常表现出较高的重叠率，但具体数值（如 0.85）需结合特定参数计算，不能一概而论。

## Evidence

[质询]数值量级与具体参数缺失：Jaccard Index 的具体数值（0.85）高度依赖于 Top K 的大小、Pareto 分布的具体参数（如 alpha 值）以及对象总数。在缺乏这些具体约束条件的情况下，断言重叠率“约为 0.85”缺乏普适性，且参考来源中完全未涉及 LRU/LFU 在 Pareto 分布下的具体重叠率数值，属于无来源支持的经验性断言。 | 参考来源 [1][2][3] 仅解释了 Jaccard 系数的定义和计算方法，未提供 LRU/LFU 在 Pareto 分布下的具体重叠率数据，无法直接支持 0.85 这一具体数值；该数值属于经验事实，逻辑上虽可能自洽（取决于具体参数），但缺乏来源直接支持或多源一致验证。

## Search Query

Jaccard index LRU LFU cache sets independent Pareto distribution

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_66526635/article/details/135047038&rut=8f6274c74837d68f3312df9cf2e98d11ad37a5a95f58644490ba95ffb49847c1', 'type': 'ddg', 'title': '【数据挖掘 | 相关性分析】Jaccard相似系数详解、关于集合的相关性（详细案例、附完详细代码实现和实操、学习资源）'}
- {'url': 'https://cloud.tencent.com/developer/article/2505049&rut=800b6d64d7b6a6ba86425a359ca1ba8cae9e34b3685d00b5e578bc579c0b8f92', 'type': 'ddg', 'title': '【数据挖掘 | 相关性分析】Jaccard相似系数详解、关于集合的相关性（详细案例、附完详细代码实现和实操、学习资源）'}
- {'url': 'https://blog.csdn.net/qq_34333481/article/details/84024513&rut=e8b163f98f2cc4ebed490297fcba3c96f7b4be4a5f6666aa8c216c44d04652b3', 'type': 'ddg', 'title': '相似度计算之Jaccard系数_jaccard相似系数怎么算-CSDN博客'}
