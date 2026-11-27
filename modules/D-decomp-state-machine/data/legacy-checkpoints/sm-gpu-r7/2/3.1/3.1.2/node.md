# N33: BF16 权重占用空间计算：27.8B * 2 bytes = 55.6 GB（若参数量为 27.8B），需与 N21 确认后的数值对齐

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

BF16 权重占用空间计算：27.8B * 2 bytes = 55.6 GB（若参数量为 27.8B），需与 N21 确认后的数值对齐

## Corrected Claim

BF16 权重占用空间计算：27.8B * 2 bytes = 55.6 GB（若参数量为 27.8B），需与 N21 确认后的数值对齐

## Evidence

先验知识/题面给定，逻辑校验通过：BF16 精度为 16 位（2 字节），27.8B 参数乘以 2 字节等于 55.6 GB，计算无误。
