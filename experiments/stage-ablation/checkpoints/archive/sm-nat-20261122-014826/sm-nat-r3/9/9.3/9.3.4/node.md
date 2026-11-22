# N176: 边界条件约束：LFU 提升上限仅在 LRU 污染率 (P[hot but cold]) 显著大于 LFU 噪声率 (P[LFU_error]) 时成立。在 β=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

边界条件约束：LFU 提升上限仅在 LRU 污染率 (P[hot but cold]) 显著大于 LFU 噪声率 (P[LFU_error]) 时成立。在 β=0.9 且 C/S=14% 的条件下，若 P[hot but cold] < 2 * P[LFU_error]，则 ΔH_net ≤ 0，LFU 性能不优于 LRU。需验证当前参数下是否满足 P[hot but cold] > 2 * P[LFU_error] 这一不等式，若不满足，则需修正上限为 0 或负值，并指出需调整的参数（如增大时间窗口以降低 σ_F）。

## Corrected Claim

边界条件约束：LFU 提升上限仅在 LRU 污染率 (P[hot but cold]) 显著大于 LFU 噪声率 (P[LFU_error]) 时成立。在 β=0.9 且 C/S=14% 的条件下，若 P[hot but cold] < 2 * P[LFU_error]，则 ΔH_net ≤ 0，LFU 性能不优于 LRU。需验证当前参数下是否满足 P[hot but cold] > 2 * P[LFU_error] 这一不等式，若不满足，则需修正上限为 0 或负值，并指出需调整的参数（如增大时间窗口以降低 σ_F）。

## Evidence

先验知识/题面给定，逻辑校验通过
