# N56: Qwen3-27B 采用 W4A16 (INT4) 精度时，权重文件大小精确值为 27e9 * 0.5 bytes / 1024^3 ≈ 12.6 GB，若使用

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Qwen3-27B 采用 W4A16 (INT4) 精度时，权重文件大小精确值为 27e9 * 0.5 bytes / 1024^3 ≈ 12.6 GB，若使用 group-wise quantization (group_size=128)，scale 因子开销约为 (27e9/128) * 2 bytes / 1024^3 ≈ 0.4 GB，总占用约 13.0 GB。

## Corrected Claim

Qwen3-27B 采用 W4A16 (INT4) 精度时，权重文件大小精确值为 27e9 * 0.5 bytes / 1024^3 ≈ 12.6 GB，若使用 group-wise quantization (group_size=128)，scale 因子开销约为 (27e9/128) * 2 bytes / 1024^3 ≈ 0.4 GB，总占用约 13.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 0.5 / 1024^3 ≈ 12.64 GB，(27e9/128) * 2 / 1024^3 ≈ 0.40 GB，总和约 13.04 GB，计算准确且符合量化存储原理。

## Search Query

W4A16 INT4 weight size group quantization scale overhead 27B
