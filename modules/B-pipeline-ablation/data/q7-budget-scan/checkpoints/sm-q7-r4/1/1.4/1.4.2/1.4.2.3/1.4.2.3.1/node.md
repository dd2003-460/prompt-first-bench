# N464: inode 驻留内存的实际比例系数 P_resident：并非所有 5 亿 inode 同时驻留，受 LRU 淘汰策略影响。P_resident = Worki

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

inode 驻留内存的实际比例系数 P_resident：并非所有 5 亿 inode 同时驻留，受 LRU 淘汰策略影响。P_resident = Working_Set_Size / Total_Inodes。对于 80% 冷数据，假设工作集仅为活跃温数据（100TB）及近期访问冷数据，若平均对象大小 1MB，活跃对象数 ≈ 1 亿，则 P_resident ≈ 100M / 500M = 20%，实际占用内存 = 500M * 20% * 256B = 25.6 GB，而非 128 GB。

## Corrected Claim

inode 驻留内存的实际比例系数 P_resident：并非所有 5 亿 inode 同时驻留，受 LRU 淘汰策略影响。P_resident = Working_Set_Size / Total_Inodes。对于 80% 冷数据，假设工作集仅为活跃温数据（100TB）及近期访问冷数据，若平均对象大小 1MB，活跃对象数 ≈ 1 亿，则 P_resident ≈ 100M / 500M = 20%，实际占用内存 = 500M * 20% * 256B = 25.6 GB，而非 128 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（100M/500M=20%，500M*0.2*256B=25.6GB），符合LRU缓存机制的基本逻辑。
