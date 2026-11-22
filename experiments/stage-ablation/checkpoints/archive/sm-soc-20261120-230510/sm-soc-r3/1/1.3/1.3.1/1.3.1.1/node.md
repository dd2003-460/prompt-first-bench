# N129: 共享随机源 ε_buyer 的方差 Var(ε_buyer) 量化：基于买家估值噪声中随机偏好噪声占比 30-50%（来自N113），且总估值噪声标准差 σ_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

共享随机源 ε_buyer 的方差 Var(ε_buyer) 量化：基于买家估值噪声中随机偏好噪声占比 30-50%（来自N113），且总估值噪声标准差 σ_total ≈ 0.1 * V_true，则 Var(ε_buyer) ∈ [0.0009, 0.0025]，对应标准差 σ_buyer ∈ [0.03, 0.05]。

## Corrected Claim

共享随机源 ε_buyer 的方差 Var(ε_buyer) 量化：基于买家估值噪声中随机偏好噪声占比 30-50%（来自N113），且总估值噪声标准差 σ_total ≈ 0.1 * V_true，则 Var(ε_buyer) ∈ [0.0009, 0.0025]，对应标准差 σ_buyer ∈ [0.03, 0.05]。

## Evidence

先验知识/题面给定，逻辑校验通过：基于总噪声标准差0.1及占比30%-50%推导，方差区间[0.0009, 0.0025]与标准差区间[0.03, 0.05]数学上完全自洽。
