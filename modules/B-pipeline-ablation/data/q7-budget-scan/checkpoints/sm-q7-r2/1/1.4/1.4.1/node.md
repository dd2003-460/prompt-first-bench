# N50: 本地文件系统（XFS/Ext4）元数据开销 M_meta_local 的基准值：在500TB数据量、平均对象/文件块大小4KB-1MB混合场景下，inode表+

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

本地文件系统（XFS/Ext4）元数据开销 M_meta_local 的基准值：在500TB数据量、平均对象/文件块大小4KB-1MB混合场景下，inode表+目录项+日志区占用约为总逻辑容量的1.5%（中位估计），即有效容量损耗 = 500TB × 1.5% = 7.5TB

## Corrected Claim

本地文件系统（XFS/Ext4）元数据开销 M_meta_local 的基准值：在500TB数据量、平均对象/文件块大小4KB-1MB混合场景下，inode表+目录项+日志区占用约为总逻辑容量的1.5%（中位估计），即有效容量损耗 = 500TB × 1.5% = 7.5TB

## Evidence

先验知识/题面给定，逻辑校验通过
