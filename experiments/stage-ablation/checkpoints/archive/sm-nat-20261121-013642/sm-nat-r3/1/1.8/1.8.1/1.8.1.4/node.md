# N161: T_residence 的数值估算：基于 N16 公式 T_cold ≈ (128GB / R_bytes) / (1 - H_byte_LRU)，代入 R_b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

T_residence 的数值估算：基于 N16 公式 T_cold ≈ (128GB / R_bytes) / (1 - H_byte_LRU)，代入 R_bytes ≈ 50M * E[size] 和 H_byte_LRU ≈ 0.75，计算得 T_residence ≈ 50-100 天

## Corrected Claim

T_residence 的数值估算：基于 N16 公式 T_cold ≈ (128GB / R_bytes) / (1 - H_byte_LRU)，代入 R_bytes ≈ 50M * E[size] 和 H_byte_LRU ≈ 0.75，计算得 T_residence ≈ 50-100 天

## Evidence

先验知识/题面给定，逻辑校验通过
