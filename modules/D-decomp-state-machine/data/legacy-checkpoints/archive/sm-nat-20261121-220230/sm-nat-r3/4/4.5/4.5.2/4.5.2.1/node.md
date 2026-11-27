# N213: 折损差异计算：在 T_resident=1.0 天且 ρ_uH=-0.2 条件下，P_invalid_LRU ≈ 0.995%，P_invalid_LFU ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

折损差异计算：在 T_resident=1.0 天且 ρ_uH=-0.2 条件下，P_invalid_LRU ≈ 0.995%，P_invalid_LFU ≈ 0.846%，ΔDiscount = H_steady * (0.995% - 0.846%) ≈ H_steady * 0.149%，若 H_steady=12%，则 ΔDiscount ≈ 0.018 个百分点

## Corrected Claim

折损差异计算：在 T_resident=1.0 天且 ρ_uH=-0.2 条件下，P_invalid_LRU ≈ 0.995%，P_invalid_LFU ≈ 0.846%，ΔDiscount = H_steady * (0.995% - 0.846%) ≈ H_steady * 0.149%，若 H_steady=12%，则 ΔDiscount ≈ 0.018 个百分点

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 12% * (0.995% - 0.846%) = 0.12 * 0.00149 = 0.0001788，即 0.01788 个百分点，四舍五入为 0.018 个百分点，数值量级与计算逻辑自洽。
