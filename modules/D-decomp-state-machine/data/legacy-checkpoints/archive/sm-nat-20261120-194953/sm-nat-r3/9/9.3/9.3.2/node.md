# N170: 有效命中率 H_eff 的精确计算：在全量驻留下，H_eff = 1 - P_inval_weighted，其中 P_inval_weighted = Σ(R_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

有效命中率 H_eff 的精确计算：在全量驻留下，H_eff = 1 - P_inval_weighted，其中 P_inval_weighted = Σ(R_i S_i * [1 - e^{-u T_i}]) / Σ(R_i S_i)。由于 T_i = 1/u 对所有 i 相同（见 N90），P_inval_i = 1 - e^{-1} ≈ 0.632 对所有对象相同，故 P_inval_weighted = 0.632，H_eff = 1 - 0.632 = 0.368 = 36.8%。此结果与热度分布 β 和大小分布 α 无关，仅由更新率 u 决定。

## Corrected Claim

有效命中率 H_eff 的精确计算：在全量驻留下，H_eff = 1 - P_inval_weighted，其中 P_inval_weighted = Σ(R_i S_i * [1 - e^{-u T_i}]) / Σ(R_i S_i)。由于 T_i = 1/u 对所有 i 相同（见 N90），P_inval_i = 1 - e^{-1} ≈ 0.632 对所有对象相同，故 P_inval_weighted = 0.632，H_eff = 1 - 0.632 = 0.368 = 36.8%。此结果与热度分布 β 和大小分布 α 无关，仅由更新率 u 决定。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导自洽，若 T_i=1/u 则 1-e^{-uT_i} 恒为 1-e^{-1}，加权平均后与分布参数无关。
