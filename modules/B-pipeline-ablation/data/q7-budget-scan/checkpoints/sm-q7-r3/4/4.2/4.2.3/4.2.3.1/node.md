# N202: 乐观工作点（高性低成）：采用16TB CMR盘（N=26），单盘写带宽200MB/s，无I/O抑制，重建时间T=400TB/200MB/s=55.5小时，硬件成

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

乐观工作点（高性低成）：采用16TB CMR盘（N=26），单盘写带宽200MB/s，无I/O抑制，重建时间T=400TB/200MB/s=55.5小时，硬件成本最低但重建最慢。

## Corrected Claim

乐观工作点（高性低成）：采用16TB CMR盘（N=26），单盘写带宽200MB/s，无I/O抑制，重建时间T=400TB/200MB/s=55.5小时，硬件成本最低但重建最慢。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB / 200MB/s = 400 * 1024 GB / 0.2 GB/s ≈ 2048000 s ≈ 56.9 h，与55.5h量级一致（差异源于单位换算精度或有效数字处理），逻辑自洽。
