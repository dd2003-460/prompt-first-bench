# N156: LRU缓存集合中对象的平均访问频率 F_LRU_avg 的量化估算：基于 Pareto(β=0.9) 分布，LRU 缓存的 K=50,000 个对象对应频率排名

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N62

## Claim

LRU缓存集合中对象的平均访问频率 F_LRU_avg 的量化估算：基于 Pareto(β=0.9) 分布，LRU 缓存的 K=50,000 个对象对应频率排名的尾部区间（约 50%-100% 分位）。在独立假设下，该区间对象的平均频率为 E[F | Rank_F ∈ [0.5N, N]] ≈ (Total_Freq * (0.5^(-β+1) - 1^(-β+1))) / (0.5N)，需结合 ρ=-0.3 的 Copula 修正因子计算最终数值。

## Corrected Claim

基于Pareto(β=0.9)分布和独立假设，LRU缓存中频率排名尾部区间（50%-100%分位）对象的平均频率可通过积分公式估算，但具体数值需结合Copula修正因子（ρ=-0.3）进行计算，当前缺乏外部数据验证该估算的准确性。

## Evidence

[质询]该陈述将具体的经验参数（Pareto β=0.9, K=50,000, ρ=-0.3）与特定的数学推导公式混合，属于经验事实与模型假设的结合。虽然公式在数学上可能自洽，但缺乏外部来源验证这些特定参数下的数值估算是否准确或符合实际系统行为，且Copula修正因子的具体应用方式未提供标准参考。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LRU cache average access frequency Pareto distribution beta 0.9 tail interval
