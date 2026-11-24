# N78: NVMe SSD RAID-6 阵列的单盘重建速率 Rebuild_Rate_NVMe 典型值为 80-120 GB/h，受限于 NVMe 盘的随机写 IOPS

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

NVMe SSD RAID-6 阵列的单盘重建速率 Rebuild_Rate_NVMe 典型值为 80-120 GB/h，受限于 NVMe 盘的随机写 IOPS 和 RAID 控制器算力，需根据具体型号实测确定

## Corrected Claim

NVMe SSD RAID-6 阵列的单盘重建速率受限于 NVMe 盘的随机写 IOPS 和 RAID 控制器算力，典型值需根据具体型号实测确定，常见范围可能在数十至数百 GB/h 之间。

## Evidence

[质询]参考来源仅提供了测试规范的背景介绍，未包含具体的重建速率数值数据，无法直接验证 80-120 GB/h 这一具体经验参数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅涉及测试范围，未提供具体数值）

## Search Query

NVMe SSD RAID 6 rebuild rate GB per hour typical values

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/721396458&rut=6840234b243512f61ddcb52b3751f0a66d74941fd85aacfd80a9e371781e3e0d', 'type': 'ddg', 'title': 'ODCC NVMe SSD RAID 性能测试技术报告 (附批注) - 知乎'}
