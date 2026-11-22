# N192: 买家行为标准差 σ_noise 的估计方法：σ_noise = sqrt(Var(T_decision)) / T_base，其中 Var(T_decision

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

买家行为标准差 σ_noise 的估计方法：σ_noise = sqrt(Var(T_decision)) / T_base，其中 Var(T_decision) 为同类商品决策时间的方差，T_base 为平均决策时间，通常 σ_noise ≈ 0.2-0.4。

## Corrected Claim

买家行为标准差 σ_noise 的估计方法：σ_noise = sqrt(Var(T_decision)) / T_base，其中 Var(T_decision) 为同类商品决策时间的方差，T_base 为平均决策时间，通常 σ_noise ≈ 0.2-0.4。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式本质上是变异系数（CV）的定义，用于量化决策时间的相对离散程度；0.2-0.4 的范围符合人类行为决策时间通常服从对数正态分布或 Gamma 分布的经验统计规律，量级合理且无内部矛盾。
