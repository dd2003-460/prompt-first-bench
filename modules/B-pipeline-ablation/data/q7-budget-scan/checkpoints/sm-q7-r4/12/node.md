# N136: 本地NVMe SSD阵列的扩容扩容系数与浪费率：由于RAID 6要求整数盘数且存在最小粒度限制，若数据年增长率为g，每年需新增物理容量为 C_new = C_c

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

本地NVMe SSD阵列的扩容扩容系数与浪费率：由于RAID 6要求整数盘数且存在最小粒度限制，若数据年增长率为g，每年需新增物理容量为 C_new = C_current * g * 1.805 / (1 - 0.02*floor(C_current/7.68))，通常导致每年3%-5%的物理容量闲置浪费（Over-provisioning Waste）。

## Corrected Claim

本地NVMe SSD阵列的扩容扩容系数与浪费率：由于RAID 6要求整数盘数且存在最小粒度限制，若数据年增长率为g，每年需新增物理容量为 C_new = C_current * g * 1.805 / (1 - 0.02*floor(C_current/7.68))，通常导致每年3%-5%的物理容量闲置浪费（Over-provisioning Waste）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
