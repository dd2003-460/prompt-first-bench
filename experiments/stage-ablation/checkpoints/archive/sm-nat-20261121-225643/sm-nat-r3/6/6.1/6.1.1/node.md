# N105: LRU驻留时间 T_resident_i 的近似解析式：对于幂律热度分布 λ_i = λ_max * (i/N)^{-β}，对象i的LRU驻留时间近似为 T_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

LRU驻留时间 T_resident_i 的近似解析式：对于幂律热度分布 λ_i = λ_max * (i/N)^{-β}，对象i的LRU驻留时间近似为 T_resident_i ≈ 1 / (λ_i * (1 - H_LRU))，其中H_LRU为全局命中率；对于头部对象(i=1, λ_1=λ_max)，T_resident_1 ≈ 1 / (λ_max * 0.413)，需代入λ_max的具体数值（基于总请求5e7/天和Pareto归一化系数）以计算具体毫秒/秒级数值。

## Corrected Claim

LRU驻留时间 T_resident_i 的近似解析式：对于幂律热度分布 λ_i = λ_max * (i/N)^{-β}，对象i的LRU驻留时间近似为 T_resident_i ≈ 1 / (λ_i * (1 - H_LRU))，其中H_LRU为全局命中率；对于头部对象(i=1, λ_1=λ_max)，T_resident_1 ≈ 1 / (λ_max * 0.413)，需代入λ_max的具体数值（基于总请求5e7/天和Pareto归一化系数）以计算具体毫秒/秒级数值。

## Evidence

先验知识/题面给定，逻辑校验通过
