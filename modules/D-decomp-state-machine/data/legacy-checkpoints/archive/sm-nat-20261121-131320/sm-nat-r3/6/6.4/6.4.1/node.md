# N130: 头部 100 个对象在 ρ=-0.3 负相关下的总字节占用量 S_top100：通过积分 E[S|F∈Top100] * 100 估算，由于热门对象偏小，S_t

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

头部 100 个对象在 ρ=-0.3 负相关下的总字节占用量 S_top100：通过积分 E[S|F∈Top100] * 100 估算，由于热门对象偏小，S_top100 显著小于 100 * E[S]，具体值需结合 Copula 模拟确定，预计小于 100 * 11KB = 1.1MB

## Corrected Claim

头部 100 个对象在 ρ=-0.3 负相关下的总字节占用量 S_top100 预计显著小于 100 * E[S]（即小于 1.1MB），具体数值需通过 Copula 模拟确定。

## Evidence

[质询]该陈述包含具体的数值估算（1.1MB）和统计结论（显著小于），属于经验事实/模拟结果，无法仅从第一性原理严格推出，且缺乏外部来源支持。 | 逻辑自洽：负相关意味着大对象更可能不在Top100，小对象更可能在Top100，因此Top100的平均大小应小于总体平均大小，总字节数小于1.1MB在逻辑上成立。但作为经验事实/模拟估算，缺乏来源直接支持，依据经验事实排除条款降级。

## Search Query

CDN cache hit rate top 100 objects size distribution Pareto correlation
