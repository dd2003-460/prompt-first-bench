# N108: LRU 稳态命中率下界的更新修正项：若对象更新率为 λ_update = 0.01/day，则有效命中率 H_LRU_eff = H_LRU_steady * 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

LRU 稳态命中率下界的更新修正项：若对象更新率为 λ_update = 0.01/day，则有效命中率 H_LRU_eff = H_LRU_steady * (1 - λ_update * T_residence_avg)，其中 T_residence_avg 为对象在 LRU 中的平均驻留时间；由于 K>N，T_residence_avg 趋于无穷大，该修正项在稳态下不适用，需考虑更新导致的缓存失效概率。

## Corrected Claim

LRU 稳态命中率受更新率影响，但不应使用 H_LRU_eff = H_LRU_steady * (1 - λ_update * T_residence_avg) 这一线性修正公式，因为该公式在 T_residence_avg 较大时会导致命中率超出 [0,1] 范围。正确的分析应基于 Markov 链或排队论模型，考虑更新操作对缓存状态转移概率的影响，而非简单的乘性修正。

## Evidence

[质询]公式 H_LRU_eff = H_LRU_steady * (1 - λ_update * T_residence_avg) 在物理/逻辑上不自洽：当 T_residence_avg 趋于无穷大时，修正项 (1 - λ_update * T_residence_avg) 将变为负无穷大，导致有效命中率为负，这违背了概率/命中率必须在 [0, 1] 区间的基本约束。此外，LRU 的稳态命中率本身已隐含了访问模式（包括更新）的影响，直接乘以一个基于驻留时间的线性修正项缺乏理论依据，属于生造的启发式公式。 | 先验知识/题面给定，但逻辑校验发现公式存在量纲/数值范围错误（命中率可能为负），且 T_residence_avg 趋于无穷大的前提与 LRU 缓存有限容量 K 的稳态行为矛盾（在有限缓存中，对象驻留时间受限于缓存大小和访问频率，不会单纯因 K>N 而趋于无穷，除非访问频率极低，但此时命中率本身已趋近于0，公式依然失效）。

## Search Query

LRU hit rate update invalidation steady state correction
