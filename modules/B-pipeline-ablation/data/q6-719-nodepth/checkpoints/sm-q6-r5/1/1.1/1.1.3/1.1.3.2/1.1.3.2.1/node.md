# N452: 平衡工作点下的有效出网流量 Traffic_out_bal = 2,000,000 MB/day * (1 - 0.85) = 300,000 MB/day (

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

平衡工作点下的有效出网流量 Traffic_out_bal = 2,000,000 MB/day * (1 - 0.85) = 300,000 MB/day (300 GB/day)，基于 N70 修正公式及 N144 给定的 H=85%。

## Corrected Claim

平衡工作点下的有效出网流量 Traffic_out_bal = 2,000,000 MB/day * (1 - 0.85) = 300,000 MB/day (300 GB/day)，基于 N70 修正公式及 N144 给定的 H=85%。

## Evidence

先验知识/题面给定，逻辑校验通过：2,000,000 * (1 - 0.85) = 300,000，单位换算 300,000 MB = 300 GB 正确，计算与逻辑自洽。
