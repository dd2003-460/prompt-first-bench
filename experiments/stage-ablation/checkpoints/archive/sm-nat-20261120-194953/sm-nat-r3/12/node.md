# N185: LRU 稳态字节命中率下界的解析推导路径：在全量驻留（K_cap >> N）且无更新失效的理想情况下，H_byte = 1.0。当引入更新率 u=0.01/da

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 稳态字节命中率下界的解析推导路径：在全量驻留（K_cap >> N）且无更新失效的理想情况下，H_byte = 1.0。当引入更新率 u=0.01/day 时，下界由最坏情况（所有对象同时失效）决定，即 H_lower_bound = 1 - P_any_inval。但在稳态下，更紧的下界基于期望失效概率：H_lower_bound ≈ 1 - u * E[T_residence]。由于 T_residence ≈ 1/u = 100 days，该公式退化为 1 - 1 = 0，表明简单的线性模型失效。正确的下界推导需使用生灭过程（Birth-Death Process）：对象进入缓存（Birth rate = R_i）和失效（Death rate = u）。稳态下对象 i 在缓存中的概率 P_in_i = R_i / (R_i + u)。由于 R_i >> u 对于大多数对象（头部对象 R_i ~ 10^4-10^5 req/day >> 0.01/day），P_in_i ≈ 1。因此，LRU 字节命中率下界主要由尾部对象（R_i ~ u）决定，H_lower_bound ≈ 1 - (Σ_{R_i < u} R_i S_i) / TotalBytes。

## Corrected Claim

LRU 稳态字节命中率下界的解析推导路径：在全量驻留（K_cap >> N）且无更新失效的理想情况下，H_byte = 1.0。当引入更新率 u=0.01/day 时，下界由最坏情况（所有对象同时失效）决定，即 H_lower_bound = 1 - P_any_inval。但在稳态下，更紧的下界基于期望失效概率：H_lower_bound ≈ 1 - u * E[T_residence]。由于 T_residence ≈ 1/u = 100 days，该公式退化为 1 - 1 = 0，表明简单的线性模型失效。正确的下界推导需使用生灭过程（Birth-Death Process）：对象进入缓存（Birth rate = R_i）和失效（Death rate = u）。稳态下对象 i 在缓存中的概率 P_in_i = R_i / (R_i + u)。由于 R_i >> u 对于大多数对象（头部对象 R_i ~ 10^4-10^5 req/day >> 0.01/day），P_in_i ≈ 1。因此，LRU 字节命中率下界主要由尾部对象（R_i ~ u）决定，H_lower_bound ≈ 1 - (Σ_{R_i < u} R_i S_i) / TotalBytes。

## Evidence

检索失败: no sources from any channel (all 5 failed)
