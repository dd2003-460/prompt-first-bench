# N89: ρ=-0.3（负相关情况）下 Top K 对象集合的 Jaccard Index 计算：J(ρ=-0.3) = |Top_K_LRU ∩ Top_K_LFU| 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

ρ=-0.3（负相关情况）下 Top K 对象集合的 Jaccard Index 计算：J(ρ=-0.3) = |Top_K_LRU ∩ Top_K_LFU| / |Top_K_LRU ∪ Top_K_LFU|，由于负相关性导致高频小对象与低频大对象分离，两个集合的重叠率下降至约 0.75 [待核验]。

## Corrected Claim

在 ρ=-0.3 的负相关情况下，Top K 对象集合的 Jaccard Index 会因高频小对象与低频大对象的分离而显著下降（具体数值取决于 K 值及分布，示例中约为 0.75）。

## Evidence

[质询]数值量级与具体数值缺乏推导依据：Jaccard Index 的具体数值（0.75）高度依赖于 Top K 的大小、对象总数以及具体的分布形态，仅凭相关系数 ρ=-0.3 无法唯一确定重叠率，该数值属于特定实验或模拟下的经验结果，而非通用理论推导值。 | 来源 [1] 仅定义了 Jaccard Index 的通用公式，未涉及 LRU/LFU 缓存策略或特定相关性下的数值表现，属于无关来源；该事实为经验性数值结论，逻辑上自洽（负相关确实导致集合分离，Jaccard 下降），但缺乏直接来源支持具体数值 0.75，故降级。

## Search Query

Jaccard index LRU LFU cache sets negative correlation Pareto distribution

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Jaccard_index&rut=8f82e03fa3695779a61053b353c39a3e0cf2000ecbac9d4b9af26ec8ef223840', 'type': 'ddg', 'title': 'Jaccard index - Wikipedia'}
