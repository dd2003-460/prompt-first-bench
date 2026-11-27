# N34: LRU稳态驻留对象数N_resident的解析近似公式：N_resident ≈ 128GB / (s_min * C_α)，其中C_α为Pareto(α=1.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LRU稳态驻留对象数N_resident的解析近似公式：N_resident ≈ 128GB / (s_min * C_α)，其中C_α为Pareto(α=1.1)分布下前10%对象的平均大小与s_min的比值（约1.5-2.0倍），用于量化缓存实际能容纳的对象数量级（预计为总对象数的5%-10%）。

## Corrected Claim

LRU稳态驻留对象数N_resident的解析近似公式：N_resident ≈ 128GB / (s_min * C_α)，其中C_α为Pareto(α=1.1)分布下前10%对象的平均大小与s_min的比值（约1.5-2.0倍），用于量化缓存实际能容纳的对象数量级（预计为总对象数的5%-10%）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且正交：节点1定义数学公式，节点2进行数值推导并修正了父节点中的错误估计（1.5-2.0 vs 2.42），节点3基于修正值进行场景分析并指出边界条件。三者无重复，无矛盾（节点2的修正正是为了解决父节点的不精确性，属于迭代完善而非冲突）。）
