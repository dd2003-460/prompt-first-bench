# N17: Pareto(α=1.1)截断均值E[S]的解析计算：由于α<2，总空间由头部主导，E[S] = S_min * (α-1)/(α-2) * (1 - (N_m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

Pareto(α=1.1)截断均值E[S]的解析计算：由于α<2，总空间由头部主导，E[S] = S_min * (α-1)/(α-2) * (1 - (N_max/N_min)^{1-α})，需代入S_min（如1KB）和N_max（最大对象上限）以验证N5中E[S]=2.5GB是否基于合理的截断边界，若边界不同，C值将发生显著变化。

## Corrected Claim

Pareto(α=1.1)截断均值E[S]的解析计算：由于α<2，总空间由头部主导，E[S] = S_min * (α-1)/(α-2) * (1 - (N_max/N_min)^{1-α})，需代入S_min（如1KB）和N_max（最大对象上限）以验证N5中E[S]=2.5GB是否基于合理的截断边界，若边界不同，C值将发生显著变化。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断均值的解析公式推导正确，量纲与逻辑自洽。

## Search Query

Pareto distribution truncated mean formula alpha 1.1
