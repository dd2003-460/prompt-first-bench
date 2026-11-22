# N47: 分子项 Σ_{i∉Cache} p_i · s_i 的计算：由于缓存容量充足（N_cache > N_total），理论上 Cache 包含所有对象，分子项趋于

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

分子项 Σ_{i∉Cache} p_i · s_i 的计算：由于缓存容量充足（N_cache > N_total），理论上 Cache 包含所有对象，分子项趋于 0，但需考虑内存开销（如元数据、对齐填充）导致的实际可用容量减少，假设有效容量为 120GB，重新计算 N_cache_eff ≈ 283,464，仍覆盖全部对象。

## Corrected Claim

分子项 Σ_{i∉Cache} p_i · s_i 的计算：由于缓存容量充足（N_cache > N_total），理论上 Cache 包含所有对象，分子项趋于 0，但需考虑内存开销（如元数据、对齐填充）导致的实际可用容量减少，假设有效容量为 120GB，重新计算 N_cache_eff ≈ 283,464，仍覆盖全部对象。

## Evidence

父节点级核验未通过：有冗余（子节点1和子节点2本质上是同一参数（有效缓存容量/开销比例）的不同取值，且均导致相同结论（分子项为0），属于冗余；子节点3引入了新的条件分支（容量不足），与前两者在逻辑上正交但前两者内部冗余。）
