# N49: Pareto(α=1.1) 大小分布的标准差 σ_S = sqrt(α/(α-2)) * X_min / sqrt(α-1) (当 α>2)，但 α=1.1<2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Pareto(α=1.1) 大小分布的标准差 σ_S = sqrt(α/(α-2)) * X_min / sqrt(α-1) (当 α>2)，但 α=1.1<2 时需截断到 S_max 后重新计算，截断后的 σ_S 需数值积分

## Corrected Claim

Pareto(α=1.1) 大小分布的标准差 σ_S = sqrt(α/(α-2)) * X_min / sqrt(α-1) (当 α>2)，但 α=1.1<2 时需截断到 S_max 后重新计算，截断后的 σ_S 需数值积分

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布标准差公式在α>2时成立，α<2时方差发散需截断，符合统计学原理
