# N220: 自建实际出网流量 Traffic_out_self = 2,000,000 MB/day * (1 - 0.80) = 400,000 MB/day = 400

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

自建实际出网流量 Traffic_out_self = 2,000,000 MB/day * (1 - 0.80) = 400,000 MB/day = 400 GB/day，是公有云出网流量的 2 倍，直接导致自建回源带宽需求翻倍。

## Corrected Claim

自建实际出网流量 Traffic_out_self = 2,000,000 MB/day * (1 - 0.80) = 400,000 MB/day = 400 GB/day，是公有云出网流量的 2 倍，直接导致自建回源带宽需求翻倍。

## Evidence

先验知识/题面给定，逻辑校验通过：2,000,000 * 0.2 = 400,000 MB，400,000 MB = 400 GB，且 400 GB 是 200 GB 的 2 倍，数值与逻辑均自洽。
