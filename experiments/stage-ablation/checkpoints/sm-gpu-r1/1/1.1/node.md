# N7: Qwen3-27B 在 BF16 精度下的权重占用显存为 54 GB (27B × 2 bytes)，FP8 为 27 GB，INT8 为 27 GB，W4 为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 BF16 精度下的权重占用显存为 54 GB (27B × 2 bytes)，FP8 为 27 GB，INT8 为 27 GB，W4 为 13.5 GB。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重占用显存为 54 GB (27B × 2 bytes)，FP8 为 27 GB，INT8 为 27 GB，W4 为 13.5 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)下为54GB，FP8/INT8(1字节)下为27GB，W4(0.5字节)下为13.5GB，计算完全自洽。
