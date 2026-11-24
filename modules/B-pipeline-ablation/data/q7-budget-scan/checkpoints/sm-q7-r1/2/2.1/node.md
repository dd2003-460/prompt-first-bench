# N12: 硬件折旧成本：本地NVMe SSD阵列年折旧 = 硬件采购成本 / 折旧年限（典型3-5年），NVMe SSD单价约为¥3000-5000/TB，500TB需1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

硬件折旧成本：本地NVMe SSD阵列年折旧 = 硬件采购成本 / 折旧年限（典型3-5年），NVMe SSD单价约为¥3000-5000/TB，500TB需1000TB物理容量（RAID-10），年折旧 ≈ ¥600,000-1,000,000

## Corrected Claim

硬件折旧成本：本地NVMe SSD阵列年折旧 = 硬件采购成本 / 折旧年限（典型3-5年），NVMe SSD单价约为¥3000-5000/TB，500TB需1000TB物理容量（RAID-10），年折旧 ≈ ¥600,000-1,000,000

## Evidence

先验知识/题面给定，逻辑校验通过：500TB逻辑容量在RAID-10下需1000TB物理容量，单价¥3000-5000/TB对应总成本¥3,000,000-5,000,000，按3-5年折旧计算年折旧约为¥600,000-1,000,000，数值量级与逻辑自洽。

## Search Query

NVMe SSD price per TB 2024
