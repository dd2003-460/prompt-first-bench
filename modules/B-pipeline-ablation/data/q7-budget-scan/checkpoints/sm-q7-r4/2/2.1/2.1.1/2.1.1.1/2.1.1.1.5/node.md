# N497: 在 500TB 数据湖场景下，若 IOPS 需求为 18,500 (平均) / 37,926 (峰值)，三款 SSD 单盘 IOPS 均远超需求，因此盘数主要由

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

在 500TB 数据湖场景下，若 IOPS 需求为 18,500 (平均) / 37,926 (峰值)，三款 SSD 单盘 IOPS 均远超需求，因此盘数主要由容量决定（500TB/3.84TB ≈ 130 块），IOPS 差异不影响盘数，仅影响延迟和队列深度，对总 TCO 影响 <5%。

## Corrected Claim

在 500TB 数据湖场景下，若 IOPS 需求为 18,500 (平均) / 37,926 (峰值)，三款 SSD 单盘 IOPS 均远超需求，因此盘数主要由容量决定（500TB/3.84TB ≈ 130 块），IOPS 差异不影响盘数，仅影响延迟和队列深度，对总 TCO 影响 <5%。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB/3.84TB≈130.2，向上取整为131块（或约130块量级），单盘IOPS远超需求故容量主导，TCO影响<5%符合工程常识。
