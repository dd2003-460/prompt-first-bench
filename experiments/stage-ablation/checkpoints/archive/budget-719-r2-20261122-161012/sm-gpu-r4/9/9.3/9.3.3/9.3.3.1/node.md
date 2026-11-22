# N699: RTX 5090 在 FP8 精度下的权重文件大小为 27 GB (27B * 1 byte)，显存占用 27 GB，剩余 5 GB (32GB - 27GB)

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N289, N290, N291

## Claim

RTX 5090 在 FP8 精度下的权重文件大小为 27 GB (27B * 1 byte)，显存占用 27 GB，剩余 5 GB (32GB - 27GB) 用于 KV Cache 和系统开销

## Corrected Claim

RTX 5090 在 FP8 精度下的权重文件大小为 27 GB (27B * 1 byte)，显存占用 27 GB，剩余 5 GB (32GB - 27GB) 用于 KV Cache 和系统开销

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8（1字节/参数）下权重占用27GB，RTX 5090显存32GB，剩余5GB用于KV Cache及开销，计算与硬件规格一致。
