# N87: 字节覆盖差异 ΔBytes 的量化计算：ΔBytes = |B_LRU - B_LFU|，在 M/C=1.0 的边界条件下，由于两者均覆盖几乎所有对象，ΔByt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

字节覆盖差异 ΔBytes 的量化计算：ΔBytes = |B_LRU - B_LFU|，在 M/C=1.0 的边界条件下，由于两者均覆盖几乎所有对象，ΔBytes ≈ 0；但在 M/C < 1.0 时，ΔBytes 可表示为 (Σ_{i∈LFU_set \ LRU_set} S_i F_i - Σ_{i∈LRU_set \ LFU_set} S_i F_i)，需通过蒙特卡洛模拟计算具体数值。

## Corrected Claim

字节覆盖差异 ΔBytes 的量化计算：ΔBytes = |B_LRU - B_LFU|，在 M/C=1.0 的边界条件下，由于两者均覆盖几乎所有对象，ΔBytes ≈ 0；但在 M/C < 1.0 时，ΔBytes 可表示为 (Σ_{i∈LFU_set \ LRU_set} S_i F_i - Σ_{i∈LRU_set \ LFU_set} S_i F_i)，需通过蒙特卡洛模拟计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过
