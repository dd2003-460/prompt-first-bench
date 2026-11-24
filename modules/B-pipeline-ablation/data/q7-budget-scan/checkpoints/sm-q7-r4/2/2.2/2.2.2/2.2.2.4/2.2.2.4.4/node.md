# N533: 文件系统开销（Filesystem Overhead）扣除：ext4/XFS等在创建inode、journal区时占用约2%-5%空间。假设3%开销，SSD有效

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N175

## Claim

文件系统开销（Filesystem Overhead）扣除：ext4/XFS等在创建inode、journal区时占用约2%-5%空间。假设3%开销，SSD有效数据容量 = 92TB * 0.97 = 89.24TB；HDD有效数据容量 = 368TB * 0.97 = 356.96TB；总有效数据容量 = 446.2TB。

## Corrected Claim

文件系统开销（Filesystem Overhead）扣除：ext4/XFS等在创建inode、journal区时占用约2%-5%空间。假设3%开销，SSD有效数据容量 = 92TB * 0.97 = 89.24TB；HDD有效数据容量 = 368TB * 0.97 = 356.96TB；总有效数据容量 = 446.2TB。

## Evidence

先验知识/题面给定，逻辑校验通过
