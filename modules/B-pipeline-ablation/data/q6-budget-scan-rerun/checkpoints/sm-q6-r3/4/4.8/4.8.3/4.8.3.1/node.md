# N296: 回源带宽限制阈值 B_limit_pop 的设定与源站最大承载能力 B_origin_max 的约束关系：B_limit_pop ≤ B_origin_max 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

回源带宽限制阈值 B_limit_pop 的设定与源站最大承载能力 B_origin_max 的约束关系：B_limit_pop ≤ B_origin_max / N_POPS，若源站总带宽为 100Gbps，则单POP点 B_limit_pop ≤ 10Gbps；若 B_limit_pop 超过此值，将导致源站过载，P99延迟增加 ΔP99_source ≈ 100-200ms

## Corrected Claim

回源带宽限制阈值 B_limit_pop 的设定与源站最大承载能力 B_origin_max 的约束关系：B_limit_pop ≤ B_origin_max / N_POPS，若源站总带宽为 100Gbps，则单POP点 B_limit_pop ≤ 10Gbps；若 B_limit_pop 超过此值，将导致源站过载，P99延迟增加 ΔP99_source ≈ 100-200ms

## Evidence

先验知识/题面给定，逻辑校验通过
