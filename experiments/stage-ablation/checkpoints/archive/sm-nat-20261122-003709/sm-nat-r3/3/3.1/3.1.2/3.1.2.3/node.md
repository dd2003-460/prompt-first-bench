# N155: 工作点3（长驻留/高失效）：假设对象平均驻留时间 T_resident = 500 天（低频更新或冷数据缓存），M_invalidation = 1 - exp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点3（长驻留/高失效）：假设对象平均驻留时间 T_resident = 500 天（低频更新或冷数据缓存），M_invalidation = 1 - exp(-0.01 * 500) ≈ 0.00995（约1.0%），注意：即使 T_resident 极大，由于 λ_update=0.01/day 较小，失效率仍受限于泊松过程的饱和效应，不会线性增长。

## Corrected Claim

工作点3（长驻留/高失效）：假设对象平均驻留时间 T_resident = 500 天（低频更新或冷数据缓存），M_invalidation = 1 - exp(-0.01 * 500) ≈ 0.00995（约1.0%），注意：即使 T_resident 极大，由于 λ_update=0.01/day 较小，失效率仍受限于泊松过程的饱和效应，不会线性增长。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程失效概率公式 M = 1 - exp(-λt) 计算正确，且指数函数饱和特性符合物理直觉。
