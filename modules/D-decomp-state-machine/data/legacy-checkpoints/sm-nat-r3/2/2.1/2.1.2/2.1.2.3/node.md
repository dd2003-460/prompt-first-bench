# N140: 在假设对象大小分布重尾且 x_max 较大导致 E[S] 显著增大的工作点下，若 N_cache_eff < 100,000，则 Cache 不包含全部对象，分

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

在假设对象大小分布重尾且 x_max 较大导致 E[S] 显著增大的工作点下，若 N_cache_eff < 100,000，则 Cache 不包含全部对象，分子项 Σ_{i∉Cache} p_i · s_i > 0，需计算被驱逐对象的字节加权访问概率之和，LRU 字节命中率下界将低于 100%。

## Corrected Claim

在假设对象大小分布重尾且 x_max 较大导致 E[S] 显著增大的工作点下，若 N_cache_eff < 100,000，则 Cache 不包含全部对象，分子项 Σ_{i∉Cache} p_i · s_i > 0，需计算被驱逐对象的字节加权访问概率之和，LRU 字节命中率下界将低于 100%。

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

Pareto heavy tail impact on cache hit rate
