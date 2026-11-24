# N664: RAID-Z2/Z3 (ZFS) 相比传统 RAID-6 的额外空间开销量化：ZFS 元数据（zpool label, txg logs, free space

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N229

## Claim

RAID-Z2/Z3 (ZFS) 相比传统 RAID-6 的额外空间开销量化：ZFS 元数据（zpool label, txg logs, free space maps）通常占用物理容量的 5%-10%。若基础 RAID-6 开销为 20% (2/10)，ZFS RAID-Z2 总空间开销约为 25%-30%。假设单盘 16TB，ZFS 有效容量比传统 RAID-6 低约 5-10TB/组，导致单位有效容量成本进一步增加 5%-10%。

## Corrected Claim

RAID-Z2/Z3 (ZFS) 相比传统 RAID-6 的额外空间开销量化：ZFS 元数据（zpool label, txg logs, free space maps）通常占用物理容量的 5%-10%。若基础 RAID-6 开销为 20% (2/10)，ZFS RAID-Z2 总空间开销约为 25%-30%。假设单盘 16TB，ZFS 有效容量比传统 RAID-6 低约 5-10TB/组，导致单位有效容量成本进一步增加 5%-10%。

## Evidence

先验知识/题面给定，逻辑校验通过
