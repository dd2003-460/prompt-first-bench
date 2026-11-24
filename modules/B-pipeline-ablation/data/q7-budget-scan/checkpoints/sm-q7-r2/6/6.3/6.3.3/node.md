# N120: SSD 故障率对 RAID 重建风险的影响：NVMe SSD 年故障率 2-5%，150 块盘年故障期望 3-7.5 次；RAID6 可容忍 2 盘故障，若 2

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

SSD 故障率对 RAID 重建风险的影响：NVMe SSD 年故障率 2-5%，150 块盘年故障期望 3-7.5 次；RAID6 可容忍 2 盘故障，若 2 盘同时故障概率 = C(150,2)×(0.035)^2 ≈ 0.08，年损失期望 = 0.08×¥500,000=¥40,000

## Corrected Claim

SSD 故障率对 RAID 重建风险的影响：NVMe SSD 年故障率 2-5%，150 块盘年故障期望 3-7.5 次；RAID6 可容忍 2 盘故障，若 2 盘同时故障概率 = C(150,2)×(0.035)^2 ≈ 0.08，年损失期望 = 0.08×¥500,000=¥40,000
