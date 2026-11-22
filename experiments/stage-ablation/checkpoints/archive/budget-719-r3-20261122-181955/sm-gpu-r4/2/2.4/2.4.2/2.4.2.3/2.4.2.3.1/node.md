# N725: FP8 E4M3 精度下 Qwen3-27B 权重占用内存为 27.0 GB (27B * 1 byte)，相比 BF16 (54 GB) 减少 50%，该数值

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N257

## Claim

FP8 E4M3 精度下 Qwen3-27B 权重占用内存为 27.0 GB (27B * 1 byte)，相比 BF16 (54 GB) 减少 50%，该数值为计算总内存需求的基础项。

## Corrected Claim

FP8 E4M3 精度下 Qwen3-27B 权重占用内存为 27.0 GB (27B * 1 byte)，相比 BF16 (54 GB) 减少 50%，该数值为计算总内存需求的基础项。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 E4M3 为 8 位格式（1 字节/参数），27B 参数对应 27GB 内存，BF16 为 16 位格式（2 字节/参数）对应 54GB，减半关系符合数学逻辑。
