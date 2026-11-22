# N21: 在 Pareto(α=1.1) 大小分布和 128GB 容量约束下，LRU 稳态驻留的对象数量 N_resident 可通过积分 ∫_{s_min}^{s_ma

- **status**: degraded
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

检索失败: no sources from any channel (all 5 failed)
