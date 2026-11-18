# N35: INT8 权重占用空间计算：27.8B * 1 byte = 27.8 GB，但需考虑是否包含 per-channel 或 per-tensor scale 因

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

INT8 权重占用空间计算：27.8B * 1 byte = 27.8 GB，但需考虑是否包含 per-channel 或 per-tensor scale 因子的额外存储（通常 <1% 开销）

## Corrected Claim

INT8 权重占用空间计算：27.8B * 1 byte = 27.8 GB，但需考虑是否包含 per-channel 或 per-tensor scale 因子的额外存储（通常 <1% 开销）

## Evidence

先验知识/题面给定，逻辑校验通过：27.8B参数在INT8下每参数1字节，总大小27.8GB；量化scale因子（per-channel或per-tensor）相对于总参数量极小，开销确实通常小于1%。
