# N188: LRU驻留对象数 K_LRU 的精确求解：需解方程 ∑_{i=1}^{K} S_{(i)} = 128GB。由于大小 S 与热度 H 存在负相关 (ρ=-0.3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N77

## Claim

LRU驻留对象数 K_LRU 的精确求解：需解方程 ∑_{i=1}^{K} S_{(i)} = 128GB。由于大小 S 与热度 H 存在负相关 (ρ=-0.3)，LRU 驻留集合并非单纯的 'K 个最小对象'，而是 '访问间隔最短的对象'。在 Pareto(α=1.1, β=0.9) 联合分布下，K_LRU 会略大于 N77 中基于纯大小排序估算的 15,000，因为小对象往往更热（驻留时间更长），而大对象虽少但驱逐快。具体修正系数需通过联合分布积分计算，预计 K_LRU ≈ 16,000-18,000。

## Corrected Claim

LRU驻留对象数 K_LRU 的求解需考虑大小与热度的负相关，其值预计略大于基于纯大小排序的估算值（如15,000），具体数值需通过联合分布积分计算确定。

## Evidence

[质询]该陈述包含具体的数值估算（K_LRU ≈ 16,000-18,000）和基于特定分布参数（Pareto α=1.1, β=0.9, ρ=-0.3）的推导结论，属于经验事实或特定模型下的计算结果，无法仅从第一性原理严格推出，且缺乏外部来源支持。 | 逻辑自洽：LRU基于访问间隔而非单纯大小，负相关导致小对象更热，驻留数略大于纯大小排序估算符合直觉；但具体数值区间为经验估算，无来源直接支持，且检索无可用来源。

## Search Query

LRU cache resident set size joint distribution Pareto size heat correlation
