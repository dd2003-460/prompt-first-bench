# N223: LFU 相比 LRU 的字节命中率提升上限 ΔH_max 的解析近似公式：ΔH_max ≈ (1 - H_LRU) * (1 - β/α) * |ρ|，其中 H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N76

## Claim

LFU 相比 LRU 的字节命中率提升上限 ΔH_max 的解析近似公式：ΔH_max ≈ (1 - H_LRU) * (1 - β/α) * |ρ|，其中 H_LRU ≈ 0.65 (来自 N68), β=0.9, α=1.1, ρ=-0.3。

## Corrected Claim

LFU 相比 LRU 的字节命中率提升上限 ΔH_max 的解析近似公式：ΔH_max ≈ (1 - H_LRU) * (1 - β/α) * |ρ|，其中 H_LRU ≈ 0.65 (来自 N68), β=0.9, α=1.1, ρ=-0.3。

## Evidence

先验知识/题面给定，逻辑校验通过
