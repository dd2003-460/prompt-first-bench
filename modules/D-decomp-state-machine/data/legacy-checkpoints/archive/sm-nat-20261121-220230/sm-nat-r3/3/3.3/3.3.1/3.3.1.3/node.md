# N179: LFU 与 LRU 在更新场景下的折损差异 ΔDiscount 的量化：ΔDiscount = D_LRU - D_LFU，若 D_LRU = 0.9851 且

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

LFU 与 LRU 在更新场景下的折损差异 ΔDiscount 的量化：ΔDiscount = D_LRU - D_LFU，若 D_LRU = 0.9851 且 D_LFU = 0.933，则 ΔDiscount ≈ 0.0521，即 LFU 比 LRU 多折损 5.21%，需通过 T_resident 的准确值验证该差异。

## Corrected Claim

LFU 与 LRU 在更新场景下的折损差异 ΔDiscount 的量化：ΔDiscount = D_LRU - D_LFU，若 D_LRU = 0.9851 且 D_LFU = 0.933，则 ΔDiscount ≈ 0.0521，即 LFU 比 LRU 多折损 5.21%，需通过 T_resident 的准确值验证该差异。

## Evidence

先验知识/题面给定，逻辑校验通过：0.9851 - 0.933 = 0.0521，计算准确，量级合理。

## Search Query

LFU vs LRU discount factor difference update scenario
