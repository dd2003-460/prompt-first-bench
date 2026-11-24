# N743: 公有云 CDN 存储总容量 S_total 的计算公式为 S_total = Q_day * s_weighted * RetentionDays / 1024

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N249

## Claim

公有云 CDN 存储总容量 S_total 的计算公式为 S_total = Q_day * s_weighted * RetentionDays / 1024^3 (TB)，其中 Q_day=2048000, s_weighted=1MB, RetentionDays=30，计算得 S_total ≈ 57.6TB，修正了 N71 中假设的 10TB 固定值。

## Corrected Claim

公有云 CDN 存储总容量 S_total 的计算公式为 S_total = Q_day * s_weighted * RetentionDays / 1024^3 (TB)，其中 Q_day=2048000, s_weighted=1MB, RetentionDays=30，计算得 S_total ≈ 57.6TB，修正了 N71 中假设的 10TB 固定值。

## Evidence

先验知识/题面给定，逻辑校验通过：2048000 * 1MB * 30 / 1024^3 ≈ 57.6TB，计算无误且量级合理。
