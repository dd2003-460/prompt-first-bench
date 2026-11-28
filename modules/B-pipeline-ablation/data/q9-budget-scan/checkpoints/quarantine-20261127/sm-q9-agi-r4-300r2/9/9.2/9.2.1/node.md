# N214: T_fix 的分布并非均匀，而是服从 Pareto 分布：80% 的修复时间集中在语法错误和 API 调用错误（平均 5 min），20% 的复杂逻辑错误占用 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

T_fix 的分布并非均匀，而是服从 Pareto 分布：80% 的修复时间集中在语法错误和 API 调用错误（平均 5 min），20% 的复杂逻辑错误占用 80% 的修复时间（平均 30 min），因此 Schema 对 T_fix 的直接节省有限，主要收益在于 T_locate。

## Corrected Claim

T_fix 的分布通常呈现长尾特征，简单错误（如语法/API）数量多但单次耗时短，复杂逻辑错误数量少但单次耗时长，导致总修复时间由少数复杂错误主导；Schema 对 T_fix 的直接节省有限，主要收益在于 T_locate。

## Evidence

[质询]该陈述包含具体的经验统计数据（80/20分布、5min/30min均值），这些并非第一性原理可推导的数学或物理事实，而是依赖于特定数据集或场景的经验观察。作为knowledge节点，虽然逻辑自洽，但缺乏外部来源验证其数值的普适性或准确性，存在将特定案例泛化为普遍规律的风险。 | 先验知识/题面给定，逻辑校验通过；但具体数值（5min/30min, 80/20）属于经验事实，无来源支持，故降级。
