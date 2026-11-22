# N49: 缓存内对象的平均驻留时间 T_avg 与对象的热度排名 rank_i 成正比，具体关系为 T_avg ≈ K_cap / R_i（以请求次数为单位），对于 Pa

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

缓存内对象的平均驻留时间 T_avg 与对象的热度排名 rank_i 成正比，具体关系为 T_avg ≈ K_cap / R_i（以请求次数为单位），对于 Pareto(β=0.9) 分布，T_avg 的分布也是重尾的，均值 E[T_avg] 由前几个最热门对象主导，需通过积分计算 E[1/R] 来得到精确值。

## Corrected Claim

缓存内对象的平均驻留时间 T_avg 与对象的热度排名 rank_i 成正比，具体关系为 T_avg ≈ K_cap / R_i（以请求次数为单位），对于 Pareto(β=0.9) 分布，T_avg 的分布也是重尾的，均值 E[T_avg] 由前几个最热门对象主导，需通过积分计算 E[1/R] 来得到精确值。

## Evidence

先验知识/题面给定，逻辑校验通过：在LRU缓存模型中，对象驻留时间确实与其访问频率（热度）成反比关系，且Pareto分布下均值由头部主导符合重尾分布特性。
