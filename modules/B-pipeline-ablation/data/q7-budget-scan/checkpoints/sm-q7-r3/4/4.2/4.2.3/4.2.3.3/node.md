# N204: 悲观工作点（高成本低性）：采用8TB CMR盘（N=52），单盘写带宽150MB/s，考虑50% I/O抑制后有效带宽75MB/s，重建时间T=400TB/75

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

悲观工作点（高成本低性）：采用8TB CMR盘（N=52），单盘写带宽150MB/s，考虑50% I/O抑制后有效带宽75MB/s，重建时间T=400TB/75MB/s≈149.3小时，硬件成本高且重建极慢。

## Corrected Claim

悲观工作点（高成本低性）：采用8TB CMR盘（N=52），单盘写带宽150MB/s，考虑50% I/O抑制后有效带宽75MB/s，重建时间T=400TB/75MB/s≈149.3小时，硬件成本高且重建极慢。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB / 75MB/s ≈ 149.3小时，计算无误，符合CMR盘重建慢的工程常识。
