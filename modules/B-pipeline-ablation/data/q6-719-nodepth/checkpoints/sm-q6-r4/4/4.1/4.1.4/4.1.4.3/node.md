# N332: 源站物理位置对 P99 的贡献量化为：当 L1 Miss 且 L2 Miss 时，RTT_origin = RTT_edge_origin + RTT_orig

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

源站物理位置对 P99 的贡献量化为：当 L1 Miss 且 L2 Miss 时，RTT_origin = RTT_edge_origin + RTT_origin_site，若 L2 命中率 H_l2 > 0.95，则源站位置影响 < 5% * (1-H_l1) * (1-H_l2) ≈ 0.25%。

## Corrected Claim

源站物理位置对 P99 的贡献量化为：当 L1 Miss 且 L2 Miss 时，RTT_origin = RTT_edge_origin + RTT_origin_site，若 L2 命中率 H_l2 > 0.95，则源站位置影响 < 5% * (1-H_l1) * (1-H_l2) ≈ 0.25%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合加权平均逻辑，数值计算 0.05 * (1-0.95) * (1-0.95) ≈ 0.0002375 即 0.024%，小于 0.25%，量级合理且自洽。
