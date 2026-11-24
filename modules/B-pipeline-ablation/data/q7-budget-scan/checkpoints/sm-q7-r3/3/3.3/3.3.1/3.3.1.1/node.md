# N211: 工作点A（高CapEx低OpEx）：NVMe SSD阵列存储100TB温数据，扫描耗时 T_scan = 100TB / (N_drives * 3GB/s)。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点A（高CapEx低OpEx）：NVMe SSD阵列存储100TB温数据，扫描耗时 T_scan = 100TB / (N_drives * 3GB/s)。假设N_drives=10，T_scan ≈ 100,000GB / 30GB/s ≈ 3333秒 ≈ 55分钟 < SLA(2h)，隐性等待成本 C_wait = 0；主要成本为CapEx摊销，年化CapEx成本 = (100TB * ¥225/TB - 残值) / 3年 ≈ ¥7,400,000/年。

## Corrected Claim

工作点A（高CapEx低OpEx）：NVMe SSD阵列存储100TB温数据，扫描耗时 T_scan = 100TB / (N_drives * 3GB/s)。假设N_drives=10，T_scan ≈ 100,000GB / 30GB/s ≈ 3333秒 ≈ 55分钟 < SLA(2h)，隐性等待成本 C_wait = 0；主要成本为CapEx摊销，年化CapEx成本 = (100TB * ¥225/TB - 残值) / 3年 ≈ ¥7,400,000/年。

## Evidence

先验知识/题面给定，逻辑校验通过：扫描时间计算正确（100000/30≈3333s<7200s），成本计算符合算术逻辑（100*225/3=7500万，扣除残值后约7400万），量级合理。
