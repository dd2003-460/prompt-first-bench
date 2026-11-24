# N28: 温数据吞吐需求：每日扫描1-2次，假设在4h内完成，吞吐 ≈ 100TB / 4h = 25TB/h ≈ 7GB/s；冷数据无实时吞吐要求，仅批量恢复时需10T

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

温数据吞吐需求：每日扫描1-2次，假设在4h内完成，吞吐 ≈ 100TB / 4h = 25TB/h ≈ 7GB/s；冷数据无实时吞吐要求，仅批量恢复时需10TB/h

## Corrected Claim

温数据吞吐需求：每日扫描1-2次，假设在4h内完成，吞吐 ≈ 100TB / 4h = 25TB/h ≈ 7GB/s；冷数据无实时吞吐要求，仅批量恢复时需10TB/h

## Evidence

先验知识/题面给定，逻辑校验通过：100TB/4h = 25TB/h，25TB/h ≈ 7.08GB/s，数值量级与单位换算正确，符合工程估算逻辑。

## Search Query

data lake scan throughput requirement GB/s batch processing
