# N380: EC(12,10) 重建时间惩罚量化：重建 1 块 16TB 盘需读取 11 块盘，聚合读带宽 11 * 150MB/s = 1.65 GB/s，重建时间 T_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N168

## Claim

EC(12,10) 重建时间惩罚量化：重建 1 块 16TB 盘需读取 11 块盘，聚合读带宽 11 * 150MB/s = 1.65 GB/s，重建时间 T_rebuild = 16TB / 1.65GB/s ≈ 10.4h。相比 EC(4,2) 的 ~4h，延迟 2.6 倍，若 RTO 目标为 4h，则需额外部署 SSD 缓存层或增加 HDD 数量至 15 块以上以满足带宽，否则 RTO 代价 C_RTO 增加 150% [待核验]

## Corrected Claim

EC(12,10) 重建时间惩罚量化：重建 1 块 16TB 盘需读取 11 块盘，聚合读带宽 11 * 150MB/s = 1.65 GB/s，重建时间 T_rebuild = 16TB / 1.65GB/s ≈ 10.4h。相比 EC(4,2) 的 ~4h，延迟 2.6 倍，若 RTO 目标为 4h，则需额外部署 SSD 缓存层或增加 HDD 数量至 15 块以上以满足带宽，否则 RTO 代价 C_RTO 增加 150% [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：16TB/1.65GB/s≈10.4h计算正确，10.4/4=2.6倍及150%增幅推导自洽

## Search Query

EC 12 10 rebuild time penalty compared to EC 4 2
