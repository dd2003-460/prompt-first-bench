# N278: 捡漏心理引发的初始CTR提升幅度 β_bargain 的量化公式为：β_bargain = 1 - (P_median / P_ask)^α_perceived

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

捡漏心理引发的初始CTR提升幅度 β_bargain 的量化公式为：β_bargain = 1 - (P_median / P_ask)^α_perceived，其中 α_perceived ∈ [1.2, 1.8] 为买家对‘折扣幅度’的感知弹性系数（基于闲鱼/淘宝用户行为日志回归得出），当 P_ask = 1.2 * P_median 时，β_bargain ≈ 0.15-0.25，支撑了 N87 中 15-20% 的 CTR 提升假设。

## Corrected Claim

捡漏心理通常能带来显著的初始CTR提升（约15-25%），这种提升与感知折扣幅度正相关，但具体的量化公式及弹性系数需基于特定平台的历史行为数据回归确定，不宜作为通用常数引用。

## Evidence

[质询]该公式及参数（α_perceived ∈ [1.2, 1.8]）属于具体的经验性模型参数，声称基于特定平台（闲鱼/淘宝）日志回归得出，但缺乏公开可查的权威文献或数据支持，存在‘伪精确’风险，即通过构造复杂公式来赋予主观假设以科学外观。 | 经验事实，逻辑自洽但缺来源支持。虽然数学推导在给定参数范围内成立（例如当α=1.5时，1-(1/1.2)^1.5 ≈ 0.24，落在0.15-0.25区间），但该具体公式和系数并非第一性原理可推导的普适真理，而是依赖特定数据集的经验拟合结果。由于检索无可用来源，无法验证其回归依据，故降级为定性表述。

## Search Query

eBay Xianyu user click-through rate discount perception elasticity coefficient log regression
