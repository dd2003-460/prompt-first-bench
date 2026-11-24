# N668: HDD+SSD 分层总功耗 P_total_Hybrid_Final 重算：基于 N274 (HDD 117W)、N249 (SSD 137.7W, 采用 7.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N277

## Claim

HDD+SSD 分层总功耗 P_total_Hybrid_Final 重算：基于 N274 (HDD 117W)、N249 (SSD 137.7W, 采用 7.68TB 拓扑)、N253 (Infra 80W)。P_total_Hybrid_Final = 117 + 137.7 + 80 = 334.7W ≈ 335W。若采用 N281 的 55 块 1.92TB SSD 拓扑 (SSD 165W)，则 P_total = 117 + 165 + 80 = 362W。

## Corrected Claim

HDD+SSD 分层总功耗 P_total_Hybrid_Final 重算：基于 N274 (HDD 117W)、N249 (SSD 137.7W, 采用 7.68TB 拓扑)、N253 (Infra 80W)。P_total_Hybrid_Final = 117 + 137.7 + 80 = 334.7W ≈ 335W。若采用 N281 的 55 块 1.92TB SSD 拓扑 (SSD 165W)，则 P_total = 117 + 165 + 80 = 362W。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 117+137.7+80=334.7 及 117+165+80=362 正确，量级符合数据中心存储设备功耗常识。
