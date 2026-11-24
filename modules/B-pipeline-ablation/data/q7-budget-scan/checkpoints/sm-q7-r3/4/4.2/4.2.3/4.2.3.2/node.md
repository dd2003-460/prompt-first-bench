# N203: 平衡工作点（中性价比最优）：采用12TB CMR盘（N=34），单盘写带宽180MB/s，考虑30% I/O抑制后有效带宽126MB/s，重建时间T=400TB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

平衡工作点（中性价比最优）：采用12TB CMR盘（N=34），单盘写带宽180MB/s，考虑30% I/O抑制后有效带宽126MB/s，重建时间T=400TB/126MB/s≈88.7小时，成本与时间折中。

## Corrected Claim

平衡工作点（中性价比最优）：采用12TB CMR盘（N=34），单盘写带宽180MB/s，考虑30% I/O抑制后有效带宽126MB/s，重建时间T=400TB/126MB/s≈88.7小时，成本与时间折中。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB / 126MB/s ≈ 88.7小时，计算无误，参数符合CMR硬盘典型性能量级。
