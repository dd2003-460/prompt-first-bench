# N86: 显存约束量化：VRAM_Required = (Model_Size_bytes + KV_Cache_bytes + Activation_bytes) * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

显存约束量化：VRAM_Required = (Model_Size_bytes + KV_Cache_bytes + Activation_bytes) * Safety_Factor (1.1)，需计算每种候选硬件在 BF16/FP8/INT8 精度下的 VRAM_Required，并与 VRAM_Available 对比，排除不满足显存下限的方案，形成可行解集 S_feasible。

## Corrected Claim

显存约束量化：VRAM_Required = (Model_Size_bytes + KV_Cache_bytes + Activation_bytes) * Safety_Factor (1.1)，需计算每种候选硬件在 BF16/FP8/INT8 精度下的 VRAM_Required，并与 VRAM_Available 对比，排除不满足显存下限的方案，形成可行解集 S_feasible。

## Evidence

先验知识/题面给定，逻辑校验通过
