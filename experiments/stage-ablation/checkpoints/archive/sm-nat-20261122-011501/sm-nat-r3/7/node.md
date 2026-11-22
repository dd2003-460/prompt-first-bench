# N21: 在 Pareto(α=1.1) 大小分布和 128GB 容量约束下，LRU 稳态驻留的对象数量 N_resident 可通过积分 ∫_{s_min}^{s_ma

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 Pareto(α=1.1) 大小分布和 128GB 容量约束下，LRU 稳态驻留的对象数量 N_resident 可通过积分 ∫_{s_min}^{s_max} (128GB / s) * f_S(s) ds 估算，其中 f_S(s) 是大小密度函数。由于 α 接近 1，少量极大对象会占用大量空间，导致 N_resident 远小于总对象数 10 万，预计仅覆盖 Top 5%-10% 的小对象。

## Corrected Claim

在 Pareto(α=1.1) 大小分布和 128GB 容量约束下，LRU 稳态驻留的对象数量 N_resident 可通过积分 ∫_{s_min}^{s_max} (128GB / s) * f_S(s) ds 估算，其中 f_S(s) 是大小密度函数。由于 α 接近 1，少量极大对象会占用大量空间，导致 N_resident 远小于总对象数 10 万，预计仅覆盖 Top 5%-10% 的小对象。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于分布参数（截断期望）对总容量/字节数估算的修正，子节点2聚焦于在特定容量约束下驻留对象数的具体计算方法（离散求和 vs 连续积分）及结果预估。两者分别处理了'分布特性/参数校准'和'约束求解/数量估算'两个不同维度，逻辑上互补且无重叠。父节点中的核心观点（积分估算的局限性、重尾效应导致N_resident远小于总数、具体的数量级预测）均被子节点覆盖或细化。）
