# N174: 自建三副本 RAID 持久性对比：自建 3 副本 RAID0 或 RAID6 需 3 份物理空间，转换系数 3.0，但持久性取决于单盘 MTBF 和重建时间，典

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

自建三副本 RAID 持久性对比：自建 3 副本 RAID0 或 RAID6 需 3 份物理空间，转换系数 3.0，但持久性取决于单盘 MTBF 和重建时间，典型 46 盘 RAID6 年数据丢失概率 ≈ 1 - (1-P_disk_fail)^N * e^(-t_rebuild/MTBF)，需精确计算

## Corrected Claim

自建三副本 RAID 持久性对比：自建 3 副本 RAID0 或 RAID6 需 3 份物理空间，转换系数 3.0，但持久性取决于单盘 MTBF 和重建时间，典型 46 盘 RAID6 年数据丢失概率 ≈ 1 - (1-P_disk_fail)^N * e^(-t_rebuild/MTBF)，需精确计算

## Evidence

父节点级核验失败（LLM 错误）：curl rc=28 b''
