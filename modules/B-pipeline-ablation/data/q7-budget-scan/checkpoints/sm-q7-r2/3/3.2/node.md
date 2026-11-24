# N18: 温数据I/O模式量化：每天扫描1-2次，假设每次扫描顺序读取100TB数据，单次扫描耗时 = 100TB / 平均吞吐量；NVMe SSD随机读IOPS>100

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

温数据I/O模式量化：每天扫描1-2次，假设每次扫描顺序读取100TB数据，单次扫描耗时 = 100TB / 平均吞吐量；NVMe SSD随机读IOPS>100K，顺序吞吐>10GB/s；HDD顺序吞吐约200-500MB/s；云对象存储并发GET请求吞吐取决于网络带宽和并发数

## Corrected Claim

温数据I/O模式量化：每天扫描1-2次，假设每次扫描顺序读取100TB数据，单次扫描耗时 = 100TB / 平均吞吐量；NVMe SSD随机读IOPS>100K，顺序吞吐>10GB/s；HDD顺序吞吐约200-500MB/s；云对象存储并发GET请求吞吐取决于网络带宽和并发数

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD顺序吞吐>10GB/s及HDD顺序吞吐200-500MB/s符合当前主流硬件性能量级，计算逻辑自洽。
