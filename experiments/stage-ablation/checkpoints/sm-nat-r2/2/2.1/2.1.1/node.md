# N38: LRU 缓存的有效对象数 K_eff 不能简单用 C/E[S] 计算，而应基于热度排序：K_eff 是满足 Σ_{i=1}^{K_eff} S_i ≤ C 的最

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LRU 缓存的有效对象数 K_eff 不能简单用 C/E[S] 计算，而应基于热度排序：K_eff 是满足 Σ_{i=1}^{K_eff} S_i ≤ C 的最大整数，其中 S_i 由条件分布 E[S_i | r_i] 给出，这反映了负相关导致头部对象更小从而 K_eff > C/E[S] 的效应。

## Corrected Claim

LRU 缓存的有效对象数 K_eff 不能简单用 C/E[S] 计算，而应基于热度排序：K_eff 是满足 Σ_{i=1}^{K_eff} S_i ≤ C 的最大整数，其中 S_i 由条件分布 E[S_i | r_i] 给出，这反映了负相关导致头部对象更小从而 K_eff > C/E[S] 的效应。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

effective cache size calculation with correlated size and popularity
