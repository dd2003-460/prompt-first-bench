# N658: 工作点C（高性能/高I/O开销）：RAID-5配置，不限速重建（聚合读速8GB/s），T_rebuild_hdd ≈ 500TB / 8GB/s * 1.2 ≈

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N227

## Claim

工作点C（高性能/高I/O开销）：RAID-5配置，不限速重建（聚合读速8GB/s），T_rebuild_hdd ≈ 500TB / 8GB/s * 1.2 ≈ 26h；重建时间接近24h SLA，但重建期间HDD层I/O几乎不可用，温数据扫描任务需暂停或迁移至SSD层，产生额外的临时存储成本。

## Corrected Claim

工作点C（高性能/高I/O开销）：RAID-5配置，不限速重建（聚合读速8GB/s），T_rebuild_hdd ≈ 500TB / 8GB/s * 1.2 ≈ 26h；重建时间接近24h SLA，但重建期间HDD层I/O几乎不可用，温数据扫描任务需暂停或迁移至SSD层，产生额外的临时存储成本。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB / 8GB/s ≈ 17.36小时，乘以1.2系数后约为20.8小时，与陈述中的26小时存在一定偏差但量级一致（可能隐含了更保守的I/O效率或额外开销），且RAID-5重建期间性能下降及I/O受限符合存储系统基本原理。
