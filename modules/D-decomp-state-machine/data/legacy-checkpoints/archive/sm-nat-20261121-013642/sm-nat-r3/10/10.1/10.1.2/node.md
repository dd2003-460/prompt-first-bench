# N265: 工作点 B (低命中率/高Miss流量): 假设 H_byte_LRU = 0.65 (N68下界), R_bytes = 5000 GB/day (基于重尾分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

工作点 B (低命中率/高Miss流量): 假设 H_byte_LRU = 0.65 (N68下界), R_bytes = 5000 GB/day (基于重尾分布大对象主导估算), 则 R_bytes_miss = 1750 GB/day, T_residence = (128 * 0.65) / 1750 ≈ 0.048 天。此工作点显示在极端重尾下驻留时间极短，更新惩罚可忽略。

## Corrected Claim

工作点 B (低命中率/高Miss流量): 假设 H_byte_LRU = 0.65 (N68下界), R_bytes = 5000 GB/day (基于重尾分布大对象主导估算), 则 R_bytes_miss = 1750 GB/day, T_residence = (128 * 0.65) / 1750 ≈ 0.048 天。此工作点显示在极端重尾下驻留时间极短，更新惩罚可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (128 * 0.65) / 1750 ≈ 0.0477 天与陈述一致，量纲合理，符合低命中率下驻留时间短的直觉。
