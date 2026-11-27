# N188: β_signal 的品类依赖量化：β_signal = β_base * (1 + γ_cat * Category_Index)，其中 β_base=0.1，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N52, N53, N54

## Claim

β_signal 的品类依赖量化：β_signal = β_base * (1 + γ_cat * Category_Index)，其中 β_base=0.1，γ_cat=0.5，Category_Index 为品类热度指数（0-1），需通过历史 A/B 测试数据回归估计 β_base 和 γ_cat 的置信区间

## Corrected Claim

β_signal 的品类依赖量化模型形式为 β_signal = β_base * (1 + γ_cat * Category_Index)，其中 β_base 和 γ_cat 为需通过历史 A/B 测试数据回归估计的参数，Category_Index 为品类热度指数（0-1）。

## Evidence

[质询]该陈述包含具体的经验参数（β_base=0.1, γ_cat=0.5）和特定的模型结构，属于经验事实而非第一性原理可推导的数学/物理定律。在缺乏外部来源支持的情况下，无法验证这些具体数值和模型形式的准确性或行业通用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

second hand platform pricing algorithm beta signal coefficient category specific AB test
