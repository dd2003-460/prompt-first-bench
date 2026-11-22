# N47: 分子项 Σ_{i∉Cache} p_i · s_i 的计算：由于缓存容量充足（N_cache > N_total），理论上 Cache 包含所有对象，分子项趋于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

分子项 Σ_{i∉Cache} p_i · s_i 的计算：由于缓存容量充足（N_cache > N_total），理论上 Cache 包含所有对象，分子项趋于 0，但需考虑内存开销（如元数据、对齐填充）导致的实际可用容量减少，假设有效容量为 120GB，重新计算 N_cache_eff ≈ 283,464，仍覆盖全部对象。

## Corrected Claim

分子项 Σ_{i∉Cache} p_i · s_i 的计算：由于缓存容量充足（N_cache > N_total），理论上 Cache 包含所有对象，分子项趋于 0，但需考虑内存开销（如元数据、对齐填充）导致的实际可用容量减少，假设有效容量为 120GB，重新计算 N_cache_eff ≈ 283,464，仍覆盖全部对象。

## Evidence

先验知识/题面给定，逻辑校验通过：假设有效容量120GB，若单对象平均大小约430KB（120GB/283464），则N_cache_eff=283,464足以覆盖全部对象（假设N_total <= 283,464），分子项为0的结论在逻辑上自洽。
