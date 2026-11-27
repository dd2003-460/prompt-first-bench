# N266: 工作点 C (中间校准点): 假设 H_byte_LRU = 0.75, R_bytes = 2000 GB/day, 则 R_bytes_miss = 500

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

工作点 C (中间校准点): 假设 H_byte_LRU = 0.75, R_bytes = 2000 GB/day, 则 R_bytes_miss = 500 GB/day, T_residence = (128 * 0.75) / 500 ≈ 0.192 天。此点用于对比 N93 中提到的 100 天阈值，揭示平均驻留时间与更新惩罚的敏感性差异。

## Corrected Claim

工作点 C (中间校准点): 假设 H_byte_LRU = 0.75, R_bytes = 2000 GB/day, 则 R_bytes_miss = 500 GB/day, T_residence = (128 * 0.75) / 500 ≈ 0.192 天。此点用于对比 N93 中提到的 100 天阈值，揭示平均驻留时间与更新惩罚的敏感性差异。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (128 * 0.75) / 500 = 96 / 500 = 0.192 正确，量纲一致（GB / (GB/day) = day），数值量级合理。
