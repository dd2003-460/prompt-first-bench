# N19: NVMe SSD阵列方案带宽：假设单块NVMe SSD顺序读带宽为5GB/s，1000TB裸容量对应约200块SSD（每块5TB），总带宽 = 200 * 5G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

NVMe SSD阵列方案带宽：假设单块NVMe SSD顺序读带宽为5GB/s，1000TB裸容量对应约200块SSD（每块5TB），总带宽 = 200 * 5GB/s = 1000GB/s，远超温数据需求（1.2-2.3GB/s），可行性高。

## Corrected Claim

NVMe SSD阵列方案带宽：假设单块NVMe SSD顺序读带宽为5GB/s，1000TB裸容量对应约200块SSD（每块5TB），总带宽 = 200 * 5GB/s = 1000GB/s，远超温数据需求（1.2-2.3GB/s），可行性高。

## Evidence

先验知识/题面给定，逻辑校验通过：单盘5GB/s带宽与5TB容量符合主流企业级NVMe SSD规格，200块SSD总带宽1000GB/s远超1.2-2.3GB/s需求，量级合理且无内部矛盾。

## Search Query

NVMe SSD sequential read bandwidth 5TB
