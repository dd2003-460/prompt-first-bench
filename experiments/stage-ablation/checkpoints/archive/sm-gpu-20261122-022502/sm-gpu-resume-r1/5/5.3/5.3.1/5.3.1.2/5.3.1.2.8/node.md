# N884: INT4 权重 + FP8 KV Cache 场景下的显存占用：Memory_Weights_INT4 ≈ 14.34 GB。Memory_KV_FP8 = 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276, N277, N278

## Claim

INT4 权重 + FP8 KV Cache 场景下的显存占用：Memory_Weights_INT4 ≈ 14.34 GB。Memory_KV_FP8 = 1.01 GB。Memory_Activations ≈ 0.54 GB。Memory_Overhead ≈ 1.0 GB。Total = 14.34 + 1.01 + 0.54 + 1.0 = 16.89 GB < 24 GB。显存余量更大，但 KV 精度损失略高于 BF16。

## Corrected Claim

INT4 权重 + FP8 KV Cache 场景下的显存占用：Memory_Weights_INT4 ≈ 14.34 GB。Memory_KV_FP8 = 1.01 GB。Memory_Activations ≈ 0.54 GB。Memory_Overhead ≈ 1.0 GB。Total = 14.34 + 1.01 + 0.54 + 1.0 = 16.89 GB < 24 GB。显存余量更大，但 KV 精度损失略高于 BF16。

## Evidence

先验知识/题面给定，逻辑校验通过：算术求和正确（14.34+1.01+0.54+1.0=16.89），且16.89<24符合显存约束逻辑；INT4权重与FP8 KV Cache的显存量级符合工程常识。
