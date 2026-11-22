# N21: LRU有效命中率折损量化（工作点：稳态高命中）：在稳态下，LRU缓存中对象平均驻留时间 T_avg_res 可通过 Little's Law 或模拟估算。有效命

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LRU有效命中率折损量化（工作点：稳态高命中）：在稳态下，LRU缓存中对象平均驻留时间 T_avg_res 可通过 Little's Law 或模拟估算。有效命中率 H_eff = H_static * (1 - P_invalidate * S_hot/S_total)，其中 S_hot/S_total 为热门对象在缓存中的字节占比。若 T_avg_res ≈ 1天（高周转），P_invalidate ≈ 1%，折损极小；若 T_avg_res ≈ 10天（大对象），P_invalidate ≈ 9%，折损显著。

## Corrected Claim

LRU有效命中率折损量化（工作点：稳态高命中）：在稳态下，LRU缓存中对象平均驻留时间 T_avg_res 可通过 Little's Law 或模拟估算。有效命中率 H_eff = H_static * (1 - P_invalidate * S_hot/S_total)，其中 S_hot/S_total 为热门对象在缓存中的字节占比。若 T_avg_res ≈ 1天（高周转），P_invalidate ≈ 1%，折损极小；若 T_avg_res ≈ 10天（大对象），P_invalidate ≈ 9%，折损显著。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU effective hit rate degradation object update rate steady state
