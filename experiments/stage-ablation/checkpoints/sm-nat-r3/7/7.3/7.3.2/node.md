# N162: K_eff 增量的敏感性分析：当 ρ 从 -0.3 变化到 -0.5 时，E[S|Top 10%] 降至 ≈ 7.1 KB，K_eff 增至 ≈ 19.35e6

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

K_eff 增量的敏感性分析：当 ρ 从 -0.3 变化到 -0.5 时，E[S|Top 10%] 降至 ≈ 7.1 KB，K_eff 增至 ≈ 19.35e6，增量升至 54.8%；表明负相关系数每增加 0.1，K_eff 增量约增加 20-25 个百分点，存在强非线性响应。

## Corrected Claim

在特定敏感性分析中，当 ρ 从 -0.3 变化到 -0.5 时，E[S|Top 10%] 降至约 7.1 KB，K_eff 增至约 19.35e6，增量升至 54.8%；这表明负相关系数每增加 0.1，K_eff 增量约增加 20-25 个百分点，存在强非线性响应。（注：具体数值需依据原始实验数据或论文验证）

## Evidence

[质询]该陈述包含具体的经验数值（如 7.1 KB, 19.35e6, 54.8%）和非线性响应结论，属于特定模型或数据集下的经验事实，无法从第一性原理直接推导，且参考来源中完全缺失相关数据支持。 | 经验事实，逻辑自洽但缺来源支持（参考来源 [1]-[3] 均与该事实主题无关，无法提供外部证据）。

## Search Query

Copula parameter sensitivity cache capacity effective objects

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: https://github.com'}
- {'url': 'https://en.m.wikipedia.org/wiki/K', 'type': 'bing', 'title': 'K - Wikipedia'}
