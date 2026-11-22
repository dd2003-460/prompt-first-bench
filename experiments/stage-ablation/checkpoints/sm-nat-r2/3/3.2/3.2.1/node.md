# N62: LFU 相对 LRU 的提升幅度 ΔH 可分解为 ΔH = (H_byte_LFU - H_byte_LRU) = [1 - (Σ_{i∉Cache_LFU} 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

LFU 相对 LRU 的提升幅度 ΔH 可分解为 ΔH = (H_byte_LFU - H_byte_LRU) = [1 - (Σ_{i∉Cache_LFU} p_i · s_i) / S_total] - [1 - (Σ_{i∉Cache_LRU} p_i · s_i) / S_total] = (Σ_{i∉Cache_LRU} p_i · s_i - Σ_{i∉Cache_LFU} p_i · s_i) / S_total。

## Corrected Claim

LFU 相对 LRU 的提升幅度 ΔH 可分解为 ΔH = (H_byte_LFU - H_byte_LRU) = [1 - (Σ_{i∉Cache_LFU} p_i · s_i) / S_total] - [1 - (Σ_{i∉Cache_LRU} p_i · s_i) / S_total] = (Σ_{i∉Cache_LRU} p_i · s_i - Σ_{i∉Cache_LFU} p_i · s_i) / S_total。

## Evidence

先验知识/题面给定，逻辑校验通过
