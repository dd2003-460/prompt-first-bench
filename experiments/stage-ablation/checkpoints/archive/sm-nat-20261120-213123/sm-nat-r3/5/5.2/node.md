# N21: LRU有效命中率折损量化（工作点：稳态高命中）：在稳态下，LRU缓存中对象平均驻留时间 T_avg_res 可通过 Little's Law 或模拟估算。有效命

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LRU有效命中率折损量化（工作点：稳态高命中）：在稳态下，LRU缓存中对象平均驻留时间 T_avg_res 可通过 Little's Law 或模拟估算。有效命中率 H_eff = H_static * (1 - P_invalidate * S_hot/S_total)，其中 S_hot/S_total 为热门对象在缓存中的字节占比。若 T_avg_res ≈ 1天（高周转），P_invalidate ≈ 1%，折损极小；若 T_avg_res ≈ 10天（大对象），P_invalidate ≈ 9%，折损显著。

## Corrected Claim

LRU有效命中率折损量化（工作点：稳态高命中）：在稳态下，LRU缓存中对象平均驻留时间 T_avg_res 可通过 Little's Law 或模拟估算。有效命中率 H_eff = H_static * (1 - P_invalidate * S_hot/S_total)，其中 S_hot/S_total 为热门对象在缓存中的字节占比。若 T_avg_res ≈ 1天（高周转），P_invalidate ≈ 1%，折损极小；若 T_avg_res ≈ 10天（大对象），P_invalidate ≈ 9%，折损显著。

## Evidence

父节点级核验未通过：有冗余（子节点之间基于对象特征（高周转/混合/大对象）和驻留时间进行了正交划分，覆盖了父节点中提到的不同量级场景，逻辑上完备。然而，这三个子节点本质上是同一公式 H_eff = H_static * (1 - P_invalidate * S_hot/S_total) 在不同参数（T_avg_res, H_static, P_invalidate, S_hot/S_total）下的具体数值实例化。它们并非独立的理论维度或子问题，而是同一量化模型在不同工作点下的计算结果。因此，存在结构上的冗余，即多个子节点实为单一参数化模型的多个取值。）

## Search Query

LRU effective hit rate degradation object update rate steady state
