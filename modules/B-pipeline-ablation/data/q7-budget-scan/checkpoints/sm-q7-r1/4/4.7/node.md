# N27: 本地NVMe SSD阵列恢复500TB数据的RTO瓶颈在于网络带宽与磁盘重建速度，假设10GbE网络(1.25GB/s)及SSD重建带宽(2GB/s/盘)，最小

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

本地NVMe SSD阵列恢复500TB数据的RTO瓶颈在于网络带宽与磁盘重建速度，假设10GbE网络(1.25GB/s)及SSD重建带宽(2GB/s/盘)，最小重建时间为max(500TB/1.25GB/s, 500TB/2GB/s) ≈ 103小时(网络瓶颈)

## Corrected Claim

本地NVMe SSD阵列恢复500TB数据的RTO瓶颈在于网络带宽与磁盘重建速度，假设10GbE网络(1.25GB/s)及SSD重建带宽(2GB/s/盘)，最小重建时间为max(500TB/1.25GB/s, 500TB/2GB/s) ≈ 103小时(网络瓶颈)

## Evidence

先验知识/题面给定，逻辑校验通过：500TB/1.25GB/s ≈ 103小时，计算正确且符合网络瓶颈逻辑
