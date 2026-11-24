# N39: HDD层RAID5冗余系数：物理容量/逻辑容量 = 1/(1-1/N)，其中N为单RAID组盘数；若N=12，系数为1.09；若N=24，系数为1.04；该系数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

HDD层RAID5冗余系数：物理容量/逻辑容量 = 1/(1-1/N)，其中N为单RAID组盘数；若N=12，系数为1.09；若N=24，系数为1.04；该系数需计入HDD层总成本，与P_HDD相乘

## Corrected Claim

HDD层RAID5冗余系数：物理容量/逻辑容量 = 1/(1-1/N)，其中N为单RAID组盘数；若N=12，系数为1.09；若N=24，系数为1.04；该系数需计入HDD层总成本，与P_HDD相乘

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5冗余系数公式 1/(1-1/N) 正确，N=12时系数为1.09，N=24时系数为1.04，数值计算准确，逻辑自洽
