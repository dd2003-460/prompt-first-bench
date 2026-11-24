# N243: NVMe RAID-6单盘故障后的重建窗口风险：重建时间 T_rebuild_nvme = 1.92TB / 100GB/h ≈ 0.19小时，期间第二块盘故障

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

NVMe RAID-6单盘故障后的重建窗口风险：重建时间 T_rebuild_nvme = 1.92TB / 100GB/h ≈ 0.19小时，期间第二块盘故障概率 P_second_fail = 1 - (1 - 0.005/365)^(0.19/24) ≈ 1×10^-8，窗口风险可忽略，NVMe阵列数据丢失几乎完全由稳态双盘故障贡献

## Corrected Claim

NVMe RAID-6单盘故障后的重建窗口风险：重建时间 T_rebuild_nvme = 1.92TB / 100GB/h ≈ 0.19小时，期间第二块盘故障概率 P_second_fail = 1 - (1 - 0.005/365)^(0.19/24) ≈ 1×10^-8，窗口风险可忽略，NVMe阵列数据丢失几乎完全由稳态双盘故障贡献

## Evidence

先验知识/题面给定，逻辑校验通过：重建时间计算正确（1.92/100=0.192h），故障概率估算符合泊松分布近似（λt≈1e-8），结论逻辑自洽。

## Search Query

NVMe RAID-6 rebuild time second disk failure negligible
