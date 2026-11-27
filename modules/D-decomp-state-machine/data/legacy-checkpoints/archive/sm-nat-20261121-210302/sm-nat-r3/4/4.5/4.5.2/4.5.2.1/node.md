# N163: 在 ρ=0 独立假设下，S_avg_hot = E[S]，即热点对象平均大小等于总体平均大小，此时 LFU 与 LRU 在大小维度上无差异，提升仅来自频率分布，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N54

## Claim

在 ρ=0 独立假设下，S_avg_hot = E[S]，即热点对象平均大小等于总体平均大小，此时 LFU 与 LRU 在大小维度上无差异，提升仅来自频率分布，作为 f(ρ) 修正的基准值。

## Corrected Claim

在 ρ=0 独立假设下，S_avg_hot = E[S]，即热点对象平均大小等于总体平均大小，此时 LFU 与 LRU 在大小维度上无差异，提升仅来自频率分布，作为 f(ρ) 修正的基准值。

## Evidence

先验知识/题面给定，逻辑校验通过：在ρ=0（独立假设）下，对象大小与访问频率/热度无相关性，故热点子集的平均大小等于总体平均大小，LFU与LRU在大小维度无差异，符合概率论基本性质。
