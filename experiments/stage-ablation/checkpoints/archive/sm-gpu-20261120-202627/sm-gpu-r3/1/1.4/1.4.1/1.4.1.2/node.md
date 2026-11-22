# N191: 不同精度下 KV Cache 显存对比表：BF16 (2B) = 13.11 GB; FP8 (1B) = 6.55 GB; INT8 (1B) = 6.55 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

不同精度下 KV Cache 显存对比表：BF16 (2B) = 13.11 GB; FP8 (1B) = 6.55 GB; INT8 (1B) = 6.55 GB; INT4 (0.5B) = 3.28 GB。用于计算各工作点的总显存需求。

## Corrected Claim

不同精度下 KV Cache 显存对比表：BF16 (2B) = 13.11 GB; FP8 (1B) = 6.55 GB; INT8 (1B) = 6.55 GB; INT4 (0.5B) = 3.28 GB。用于计算各工作点的总显存需求。

## Evidence

先验知识/题面给定，逻辑校验通过：数值比例关系（13.11:6.55:6.55:3.28 ≈ 2:1:1:0.5）与精度位宽（BF16=2B, FP8/INT8=1B, INT4=0.5B）严格一致，量纲与量级合理。
