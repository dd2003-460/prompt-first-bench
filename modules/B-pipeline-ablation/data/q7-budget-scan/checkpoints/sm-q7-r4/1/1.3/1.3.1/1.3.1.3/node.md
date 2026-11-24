# N124: NVMe SSD 阵列的总顺序吞吐量承载能力 = 物理盘数 × 单盘顺序读带宽。单盘顺序读约 3,000 MB/s (3GB/s)，总能力 = 313 × 3G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

NVMe SSD 阵列的总顺序吞吐量承载能力 = 物理盘数 × 单盘顺序读带宽。单盘顺序读约 3,000 MB/s (3GB/s)，总能力 = 313 × 3GB/s ≈ 939 GB/s。温数据扫描需求 1.74 GB/s，利用率 < 0.2%，无压力。

## Corrected Claim

NVMe SSD 阵列的总顺序吞吐量承载能力 = 物理盘数 × 单盘顺序读带宽。单盘顺序读约 3,000 MB/s (3GB/s)，总能力 = 313 × 3GB/s ≈ 939 GB/s。温数据扫描需求 1.74 GB/s，利用率 < 0.2%，无压力。

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD 顺序读带宽量级（~3GB/s）符合主流 PCIe 4.0/5.0 规格，乘法运算及利用率计算逻辑自洽。
