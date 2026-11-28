# N18: Qwen3-27B 在 INT8 精度下的理论最小显存占用为 27GB (27B * 1 byte) + 量化校准常数开销 (~0.5GB) + KV Cach

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B 在 INT8 精度下的理论最小显存占用为 27GB (27B * 1 byte) + 量化校准常数开销 (~0.5GB) + KV Cache 开销，总显存需求约 28.5-29.5GB

## Corrected Claim

Qwen3-27B 在 INT8 精度下的理论最小显存占用为 27GB (27B * 1 byte) + 量化校准常数开销 (~0.5GB) + KV Cache 开销，总显存需求约 28.5-29.5GB

## Evidence

先验知识/题面给定，逻辑校验通过：INT8下27B参数占27GB，加上少量校准常数和KV Cache开销，总量级估算合理。

## Search Query

Qwen3-27B INT8 quantization memory overhead
