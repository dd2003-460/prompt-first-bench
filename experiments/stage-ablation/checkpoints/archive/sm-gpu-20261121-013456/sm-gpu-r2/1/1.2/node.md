# N8: Qwen3-27B 在 FP8 精度下的基础权重显存占用为 27 GB (27B * 1 byte/token)，较 BF16 减少 50%。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B 在 FP8 精度下的基础权重显存占用为 27 GB (27B * 1 byte/token)，较 BF16 减少 50%。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的基础权重显存占用为 27 GB (27B * 1 byte/token)，较 BF16 减少 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 1字节/参数 = 27GB，BF16为2字节/参数，故减少50%，计算无误。
