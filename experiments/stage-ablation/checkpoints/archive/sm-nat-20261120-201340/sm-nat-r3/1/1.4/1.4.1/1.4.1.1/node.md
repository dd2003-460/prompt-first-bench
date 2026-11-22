# N94: 形状常数 c 的精确推导：在双 Pareto 分布 (α=1.1, β=0.9) 且 ρ=-0.3 的约束下，c 并非简单的 1/√(α-1)≈3.16，而需通

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

形状常数 c 的精确推导：在双 Pareto 分布 (α=1.1, β=0.9) 且 ρ=-0.3 的约束下，c 并非简单的 1/√(α-1)≈3.16，而需通过 Copula 函数（如 Clayton 或 Gumbel-Hougaard）求解，使得联合分布的 Pearson 相关系数匹配 -0.3，此时 c 的实际值约为 1.2-1.5，导致压缩因子 (1 - c*ρ*...) 从 2.0 降至 1.36-1.45。

## Corrected Claim

在双 Pareto 分布 (α=1.1, β=0.9) 且 ρ=-0.3 的约束下，形状常数 c 需通过 Copula 函数求解以匹配 Pearson 相关系数，其值通常显著小于 1/√(α-1)，具体数值依赖于所选 Copula 类型及参数化方式，需通过数值积分或模拟确定。

## Evidence

[质询]该陈述包含具体的数值结论（c≈1.2-1.5，压缩因子1.36-1.45），属于经验/计算事实，无法仅从第一性原理直接推出，且缺乏来源支持其具体数值范围；此外，'压缩因子'的具体公式未在陈述中给出，导致'从2.0降至...'这一推导链条不完整，存在逻辑跳跃。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

bivariate Pareto distribution copula Pearson correlation coefficient calculation
