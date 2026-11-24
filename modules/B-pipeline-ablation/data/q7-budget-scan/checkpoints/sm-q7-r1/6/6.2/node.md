# N41: SSD写入寿命：NVMe SSD TBW(总写入字节)为1,000TB/盘，假设每日写入量为温数据扫描产生的缓存更新1TB/日，则寿命=1000TB/1TB*日

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

SSD写入寿命：NVMe SSD TBW(总写入字节)为1,000TB/盘，假设每日写入量为温数据扫描产生的缓存更新1TB/日，则寿命=1000TB/1TB*日=1000日≈2.7年，需考虑更换成本

## Corrected Claim

SSD写入寿命：NVMe SSD TBW(总写入字节)为1,000TB/盘，假设每日写入量为温数据扫描产生的缓存更新1TB/日，则寿命=1000TB/1TB*日=1000日≈2.7年，需考虑更换成本

## Evidence

先验知识/题面给定，逻辑校验通过：1000TB / 1TB/日 = 1000日，1000/365 ≈ 2.74年，计算无误且符合SSD寿命估算的基本逻辑。
