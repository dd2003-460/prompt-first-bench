# N19: 量化工作点 2（基准更新率 u=0.01）：δ ≈ 1 - 0.01 * (T_residence / L_object)；若 T_residence/L_ob

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

量化工作点 2（基准更新率 u=0.01）：δ ≈ 1 - 0.01 * (T_residence / L_object)；若 T_residence/L_object ≈ 0.5（典型 CDN 场景），则 δ ≈ 0.995，折损约 0.5%；若头部对象 T_residence/L_object ≈ 2，则头部折损约 2%，整体加权折损约 1-2%。

## Corrected Claim

量化工作点 2（基准更新率 u=0.01）：δ ≈ 1 - 0.01 * (T_residence / L_object)；若 T_residence/L_object ≈ 0.5（典型 CDN 场景），则 δ ≈ 0.995，折损约 0.5%；若头部对象 T_residence/L_object ≈ 2，则头部折损约 2%，整体加权折损约 1-2%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 δ = 1 - u * (T_res/L_obj) 在 u=0.01 时，若比值为0.5则δ=0.995（折损0.5%），若比值为2则δ=0.98（折损2%），数值推导自洽且符合CDN缓存更新的一般量级直觉。
