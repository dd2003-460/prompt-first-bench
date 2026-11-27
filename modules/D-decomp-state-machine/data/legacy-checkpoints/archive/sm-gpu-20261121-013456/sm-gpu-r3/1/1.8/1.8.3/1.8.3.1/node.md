# N183: FP8 权重显存占用计算：27B 参数 * 1 byte/param = 27 GB（假设无额外量化开销）

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

FP8 权重显存占用计算：27B 参数 * 1 byte/param = 27 GB（假设无额外量化开销）

## Corrected Claim

FP8 权重显存占用计算：27B 参数 * 1 byte/param = 27 GB（假设无额外量化开销）

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 格式每参数占 1 字节，27B 参数即 27GB，计算无误。
