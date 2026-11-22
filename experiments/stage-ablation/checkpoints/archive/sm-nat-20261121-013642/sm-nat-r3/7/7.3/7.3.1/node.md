# N239: 在 ρ=-0.3 且 α=1.1, β=0.9 的参数下，热门对象（freq 前 10%）的平均大小期望值 E[size | freq_top10] 的具体数值

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

在 ρ=-0.3 且 α=1.1, β=0.9 的参数下，热门对象（freq 前 10%）的平均大小期望值 E[size | freq_top10] 的具体数值约为 4.2 KB，而整体平均 E[size] 约为 5.8 KB，降低幅度为 (5.8-4.2)/5.8 ≈ 27.6%，修正了 N82 中 15%-25% 的估计区间 [待核验]

## Corrected Claim

在 ρ=-0.3 且 α=1.1, β=0.9 的参数下，热门对象（freq 前 10%）的平均大小期望值通常低于整体平均大小，具体数值需依赖特定数据集或仿真结果，原估计区间 15%-25% 可能偏低，实际降幅可能在 20%-30% 左右。

## Evidence

[质询]具体数值（4.2 KB, 5.8 KB）及由此推导的 27.6% 降幅属于特定仿真或经验数据，无法从给定的参数（ρ, α, β）通过第一性原理严格推导得出，且缺乏外部来源支持其精确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Pareto distribution conditional expectation negative correlation size frequency
