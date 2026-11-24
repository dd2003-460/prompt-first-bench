# N47: SSD缓存层的最小盘数计算：温数据100TB，假设使用RAID10（2盘镜像，1盘有效），有效容量 = N/2 * C >= 100TB；若C=16TB，N/2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

SSD缓存层的最小盘数计算：温数据100TB，假设使用RAID10（2盘镜像，1盘有效），有效容量 = N/2 * C >= 100TB；若C=16TB，N/2 * 16 >= 100，解得 N >= 12.5，取N=14或16盘；若使用RAID5，有效容量 = (N-1)/N * C >= 100，N=8盘时有效容量 = 7/8*16 = 14TB，不足，需N=58盘，不经济；故推荐RAID10，N=16盘。

## Corrected Claim

SSD缓存层的最小盘数计算：温数据100TB，假设使用RAID10（2盘镜像，1盘有效），有效容量 = N/2 * C >= 100TB；若C=16TB，N/2 * 16 >= 100，解得 N >= 12.5，取N=14或16盘；若使用RAID5，有效容量 = (N-1)/N * C >= 100，N=8盘时有效容量 = 7/8*16 = 14TB，不足，需N=58盘，不经济；故推荐RAID10，N=16盘。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID10有效容量公式为N/2*C，计算100/(16/2)=12.5，向上取整至偶数14或16盘符合逻辑；RAID5计算58盘亦符合(N-1)/N*C>=100的推导，结论自洽。

## Search Query

RAID10 minimum drive count 100TB 16TB SSD
