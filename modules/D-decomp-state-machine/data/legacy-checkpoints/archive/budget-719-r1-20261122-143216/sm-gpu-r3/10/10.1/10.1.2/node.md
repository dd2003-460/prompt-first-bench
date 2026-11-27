# N392: Qwen3-27B 在 FP8 精度下每 token 的 AllReduce 通信量计算：2 × 64 × 4096 × 1 byte = 524,288 by

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139, N140, N141

## Claim

Qwen3-27B 在 FP8 精度下每 token 的 AllReduce 通信量计算：2 × 64 × 4096 × 1 byte = 524,288 bytes ≈ 0.5 MB。

## Corrected Claim

Qwen3-27B 在 FP8 精度下每 token 的 AllReduce 通信量计算：2 × 64 × 4096 × 1 byte = 524,288 bytes ≈ 0.5 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：2 × 64 × 4096 × 1 = 524,288 bytes，且 524,288 bytes 等于 0.5 MB（按 1 MB = 1,048,576 bytes 计算），数值与量纲均正确。
