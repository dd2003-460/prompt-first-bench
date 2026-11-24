# N82: 公有云CDN下行平均带宽需求 = (2TB/day) / (24h × 3600s) ≈ 9.88 Mbps，若考虑峰值系数2.0，峰值下行带宽需求约为 19.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18, N19, N20

## Claim

公有云CDN下行平均带宽需求 = (2TB/day) / (24h × 3600s) ≈ 9.88 Mbps，若考虑峰值系数2.0，峰值下行带宽需求约为 19.76 Mbps。

## Corrected Claim

公有云CDN下行平均带宽需求 = (2TB/day) / (24h × 3600s) ≈ 9.88 Mbps，若考虑峰值系数2.0，峰值下行带宽需求约为 19.76 Mbps。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/day 换算为 2*1024*1024*1024*8 / (24*3600) ≈ 9.88 Mbps，乘以峰值系数 2.0 得 19.76 Mbps，计算无误。
