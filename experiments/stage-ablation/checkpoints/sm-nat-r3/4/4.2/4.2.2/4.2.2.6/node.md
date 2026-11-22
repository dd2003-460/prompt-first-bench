# N207: 热点对象（Top 10%）的加权字节占比 W_hot 的精确计算：W_hot = (Σ_{i∈Top10%} p_i s_i) / (Σ_{all} p_i s

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71, N72, N73

## Claim

热点对象（Top 10%）的加权字节占比 W_hot 的精确计算：W_hot = (Σ_{i∈Top10%} p_i s_i) / (Σ_{all} p_i s_i)，需结合 Pareto(β=0.9) 热度分布和 Pareto(α=1.1) 大小分布，通过数值积分计算 W_hot 的具体数值（预计接近 89.1% 的请求量占比，但字节占比可能因负相关而略有不同），以量化 N73 中放大因子的基础。

## Corrected Claim

热点对象（Top 10%）的加权字节占比 W_hot 需结合 Pareto(β=0.9) 热度分布和 Pareto(α=1.1) 大小分布，在明确 Top 10% 排序依据及联合分布假设后，通过数值积分估算 W_hot 的具体数值（预计接近 89.1% 的请求量占比，字节占比可能因负相关而略有不同），以量化 N73 中放大因子的基础。

## Evidence

[质询]该陈述声称通过数值积分可计算出 W_hot 的“具体数值”，但仅给出 Pareto 分布参数（β=0.9, α=1.1）而未明确定义 Top 10% 的排序依据（是按请求频率 p_i 还是加权热度 p_i*s_i？），且未提供具体的联合分布假设或相关性系数，导致“精确计算”在数学上缺乏唯一解，属于经验/模型依赖事实而非第一性原理可推导事实。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且该数值依赖于未完全指定的模型假设，无法从第一性原理严格推出唯一值。

## Search Query

Pareto distribution weighted byte ratio top 10% hot objects
