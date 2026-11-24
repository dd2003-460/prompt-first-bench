# N19: NVMe SSD 阵列在单盘故障下的 RTO 取决于 RAID 级别重建时间与容量，公式：T_RTO_NVMe = T_detect + T_rebuild(R

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

NVMe SSD 阵列在单盘故障下的 RTO 取决于 RAID 级别重建时间与容量，公式：T_RTO_NVMe = T_detect + T_rebuild(RAID_level, C_used_TB, IOPS_rebuild)，其中 RAID5/6 重建时间随容量线性增加，典型 500TB 规模下 RAID6 重建需 12-24 小时 [待核验]

## Corrected Claim

NVMe SSD 阵列在单盘故障下的 RTO 取决于 RAID 级别重建时间与容量，公式：T_RTO_NVMe = T_detect + T_rebuild(RAID_level, C_used_TB, IOPS_rebuild)，其中 RAID5/6 重建时间随容量线性增加，具体时长需根据实际 IOPS 和带宽实测确定。

## Evidence

父节点级核验未通过：不完备（子节点分别关注‘业务性能影响’（I/O抑制）和‘硬件物理瓶颈’（重建带宽），二者维度不同，具备正交性且无冗余。但在完备性上存在明显缺失：父节点公式明确包含 T_detect（检测时间）和 RAID_level（RAID级别对重建逻辑的影响，如RAID5 vs RAID6差异），但子节点仅聚焦于RAID6的重建过程细节，完全未覆盖故障检测机制及不同RAID级别间的结构性差异。）

## Search Query

NVMe SSD RAID6 rebuild time 500TB hours performance degradation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/721396458&rut=6840234b243512f61ddcb52b3751f0a66d74941fd85aacfd80a9e371781e3e0d', 'type': 'ddg', 'title': 'ODCC NVMe SSD RAID 性能测试技术报告 (附批注) - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/551278264&rut=abd6708b162c75ded5705630b43adc15079d0dea107dac65f88f18c48f7a5565', 'type': 'ddg', 'title': '技术实践 | 如何给NVMe做RAID - 知乎'}
- {'url': 'https://www.toutiao.com/article/7417285156521722379/&rut=9c4b3754d647bd90cd55055983241f20cd3f513c6332b1362caf76e011caee2a', 'type': 'ddg', 'title': 'ODCC NVMe SSD RAID 性能测试技术报告 (附批注) - 今日头条'}
