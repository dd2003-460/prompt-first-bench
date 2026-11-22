# N201: 在 vLLM 或 PyTorch 后端中，FP8 (E4M3) 量化权重通常采用 Block-wise 量化策略（如每 128 个元素共享一个 FP32 sca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

在 vLLM 或 PyTorch 后端中，FP8 (E4M3) 量化权重通常采用 Block-wise 量化策略（如每 128 个元素共享一个 FP32 scale factor），导致每 128 个参数字节增加 4 字节 overhead（scale factor），实际存储密度为 (128 × 1 + 4) / 128 ≈ 1.031 bytes/param。

## Corrected Claim

在 vLLM 或 PyTorch 后端中，FP8 (E4M3) 量化权重通常采用 Block-wise 量化策略（如每 128 个元素共享一个 FP32 scale factor），导致每 128 个参数字节增加 4 字节 overhead（scale factor），实际存储密度为 (128 × 1 + 4) / 128 ≈ 1.031 bytes/param。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 E4M3 为 1 字节，Block-wise 128 元素共享 1 个 FP32 scale (4 字节)，计算 (128*1 + 4)/128 = 1.03125 bytes/param，数值与逻辑均正确。
