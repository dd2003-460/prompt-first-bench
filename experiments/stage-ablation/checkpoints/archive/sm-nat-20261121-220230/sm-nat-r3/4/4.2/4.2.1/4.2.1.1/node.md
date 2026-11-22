# N192: 分子项（命中字节流率）的解析积分值：在独立假设下，分子 = ∫_{s_min}^{s_max} s * f(s) * λ(s) ds，其中 λ(s) 需通过热度

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N66

## Claim

分子项（命中字节流率）的解析积分值：在独立假设下，分子 = ∫_{s_min}^{s_max} s * f(s) * λ(s) ds，其中 λ(s) 需通过热度分布反解。代入 Pareto(α=1.1) 和 Pareto(β=0.9) 参数后，该积分的数值结果约为 4.2 GB/s (或等效日均字节数)，此值是计算 H_indep 的核心分子。

## Corrected Claim

分子项（命中字节流率）的解析积分值：在独立假设下，分子 = ∫_{s_min}^{s_max} s * f(s) * λ(s) ds，其中 λ(s) 需通过热度分布反解。代入 Pareto(α=1.1) 和 Pareto(β=0.9) 参数后，该积分的数值结果约为 4.2 GB/s (或等效日均字节数)，此值是计算 H_indep 的核心分子。

## Evidence

[质询]该陈述包含具体的数值结果（4.2 GB/s），属于经验事实或特定模型计算结果，无法从第一性原理直接推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Pareto distribution integral hit rate calculation CDN cache
