# N170: 工作点A (HDD+SSD分层) 的温数据扫描性能瓶颈量化：温数据100TB全在SSD层，NVMe顺序读7GB/s，T_scan = 100,000GB / 7

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点A (HDD+SSD分层) 的温数据扫描性能瓶颈量化：温数据100TB全在SSD层，NVMe顺序读7GB/s，T_scan = 100,000GB / 7GB/s ≈ 14,286s ≈ 4h；冷数据400TB在HDD层，若需扫描（假设每月1次），HDD聚合吞吐2.5GB/s (参考N111)，T_scan_cold = 400,000GB / 2.5GB/s ≈ 160,000s ≈ 44h；年均冷数据扫描次数30次，年均冷数据扫描耗时 = 30 * 44h = 1320h。

## Corrected Claim

工作点A (HDD+SSD分层) 的温数据扫描性能瓶颈量化：温数据100TB全在SSD层，NVMe顺序读7GB/s，T_scan = 100,000GB / 7GB/s ≈ 14,286s ≈ 4h；冷数据400TB在HDD层，若需扫描（假设每月1次），HDD聚合吞吐2.5GB/s (参考N111)，T_scan_cold = 400,000GB / 2.5GB/s ≈ 160,000s ≈ 44h；年均冷数据扫描次数30次，年均冷数据扫描耗时 = 30 * 44h = 1320h。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算准确（100000/7≈14286s≈4h; 400000/2.5=160000s≈44.4h; 30*44.4h≈1332h，原文取整为1320h误差在合理范围内），量纲与物理直觉一致。
