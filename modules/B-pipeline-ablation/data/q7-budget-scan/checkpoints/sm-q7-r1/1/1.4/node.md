# N10: 冷热数据分离布局下的容量分配：总数据量500TB，冷数据占80%即400TB，温数据占20%即100TB。在HDD+SSD分层中，SSD层需容纳100TB温数据

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

冷热数据分离布局下的容量分配：总数据量500TB，冷数据占80%即400TB，温数据占20%即100TB。在HDD+SSD分层中，SSD层需容纳100TB温数据，HDD层需容纳400TB冷数据。

## Corrected Claim

冷热数据分离布局下的容量分配：总数据量500TB，冷数据占80%即400TB，温数据占20%即100TB。在HDD+SSD分层中，SSD层需容纳100TB温数据，HDD层需容纳400TB冷数据。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB * 80% = 400TB，500TB * 20% = 100TB，数值计算准确且符合分层存储逻辑。
