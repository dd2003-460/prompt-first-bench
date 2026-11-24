# N65: 工作点A（NVMe SSD）：扫描耗时 T_scan = 100TB / (N_drives × 3GB/s) ≈ 9分钟，因 T_scan < SLA(2h)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

工作点A（NVMe SSD）：扫描耗时 T_scan = 100TB / (N_drives × 3GB/s) ≈ 9分钟，因 T_scan < SLA(2h)，隐性等待成本 C_wait = 0；主要成本为高 CapEx 溢价

## Corrected Claim

工作点A（NVMe SSD）：扫描耗时 T_scan = 100TB / (N_drives × 3GB/s) ≈ 9分钟，因 T_scan < SLA(2h)，隐性等待成本 C_wait = 0；主要成本为高 CapEx 溢价

## Evidence

先验知识/题面给定，逻辑校验通过：100TB / (10 * 3GB/s) ≈ 555s ≈ 9.25min < 2h，推导自洽
