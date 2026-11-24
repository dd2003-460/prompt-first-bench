# N1287: 传输延迟对 P99 的影响量化：L_transmission = s_video / B_link；标准工作点 B_link=100Mbps 时，L_trans

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N439

## Claim

传输延迟对 P99 的影响量化：L_transmission = s_video / B_link；标准工作点 B_link=100Mbps 时，L_transmission = 7.5MB / 12.5MB/s = 600ms；高码率 8.0MB 时 L_transmission = 640ms，增加 40ms，需验证是否突破 P99 ≤ 100ms 约束。

## Corrected Claim

传输延迟对 P99 的影响量化：L_transmission = s_video / B_link；标准工作点 B_link=100Mbps 时，L_transmission = 7.5MB / 12.5MB/s = 600ms；高码率 8.0MB 时 L_transmission = 640ms，增加 40ms，需验证是否突破 P99 ≤ 100ms 约束。

## Evidence

先验知识/题面给定，逻辑校验通过：7.5MB / 12.5MB/s = 0.6s = 600ms，8.0MB / 12.5MB/s = 0.64s = 640ms，差值40ms，计算无误且符合物理直觉。
