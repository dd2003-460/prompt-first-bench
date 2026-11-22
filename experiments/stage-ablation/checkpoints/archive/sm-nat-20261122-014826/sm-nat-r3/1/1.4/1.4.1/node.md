# N33: 分母 Total = Σ r_i s_i 的精确数值：基于 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布，且引入 ρ=-0.3 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

分母 Total = Σ r_i s_i 的精确数值：基于 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布，且引入 ρ=-0.3 的负相关修正，计算加权总字节吞吐量。需构建联合分布 f(size, rank) 以消除相关性影响，Total ≈ N * E[r*s] * 5000万。

## Corrected Claim

分母 Total 需基于 Pareto(α=1.1) 和 Pareto(β=0.9) 分布及 ρ=-0.3 的负相关修正，通过构建联合分布 f(size, rank) 计算加权总字节吞吐量，具体数值需依据详细计算模型确定。

## Evidence

[质询]该陈述包含具体的经验性数值结果（Total ≈ ...），且依赖于特定的联合分布构建方法（负相关修正）。在缺乏具体计算过程或来源支持的情况下，无法验证该精确数值或近似值的正确性，属于经验事实而非纯逻辑推导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理直接推出）

## Search Query

joint distribution of file size and request frequency in CDN cache analysis Pareto alpha 1.1 beta 0.9
