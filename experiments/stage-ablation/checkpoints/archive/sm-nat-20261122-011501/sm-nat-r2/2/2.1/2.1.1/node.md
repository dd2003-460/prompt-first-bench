# N34: LRU稳态驻留对象数N_resident的解析近似公式：N_resident ≈ 128GB / (s_min * C_α)，其中C_α为Pareto(α=1.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LRU稳态驻留对象数N_resident的解析近似公式：N_resident ≈ 128GB / (s_min * C_α)，其中C_α为Pareto(α=1.1)分布下前10%对象的平均大小与s_min的比值（约1.5-2.0倍），用于量化缓存实际能容纳的对象数量级（预计为总对象数的5%-10%）。

## Corrected Claim

LRU稳态驻留对象数N_resident的解析近似公式：N_resident ≈ 128GB / (s_min * C_α)，其中C_α为Pareto(α=1.1)分布下前10%对象的平均大小与s_min的比值（约1.5-2.0倍），用于量化缓存实际能容纳的对象数量级（预计为总对象数的5%-10%）。

## Evidence

先验知识/题面给定，逻辑校验通过
