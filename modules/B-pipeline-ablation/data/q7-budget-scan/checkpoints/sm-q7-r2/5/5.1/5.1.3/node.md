# N119: HDD+SSD 分层聚合 IOPS 供给 = SSD 层 IOPS (100,000 × 42) + HDD 层 IOPS (200 × 40 × 并行度修正)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

HDD+SSD 分层聚合 IOPS 供给 = SSD 层 IOPS (100,000 × 42) + HDD 层 IOPS (200 × 40 × 并行度修正) ≈ 4,200,000 + 8,000 = 4,208,000 IOPS，满足 IOPS_peak 需求

## Corrected Claim

HDD+SSD 分层聚合 IOPS 供给 = SSD 层 IOPS (100,000 × 42) + HDD 层 IOPS (200 × 40 × 并行度修正) ≈ 4,200,000 + 8,000 = 4,208,000 IOPS，满足 IOPS_peak 需求

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 100,000*42 + 200*40 = 4,200,000 + 8,000 = 4,208,000 正确，且分层存储聚合IOPS逻辑自洽。
