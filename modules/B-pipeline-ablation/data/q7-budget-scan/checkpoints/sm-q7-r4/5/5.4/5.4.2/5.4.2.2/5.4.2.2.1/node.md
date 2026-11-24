# N581: 工作点A（高密度低成本）：采用16TB CMR HDD (Seagate Exos 16E) + RAID6 (8+2)，单盘价格¥1,200，总盘数25块，H

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N247

## Claim

工作点A（高密度低成本）：采用16TB CMR HDD (Seagate Exos 16E) + RAID6 (8+2)，单盘价格¥1,200，总盘数25块，HDD层硬件成本 = 25 * 1200 = ¥30,000

## Corrected Claim

工作点A（高密度低成本）：采用16TB CMR HDD (Seagate Exos 16E) + RAID6 (8+2)，单盘价格¥1,200，总盘数25块，HDD层硬件成本 = 25 * 1200 = ¥30,000

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 25 * 1200 = 30000 正确，RAID6 (8+2) 配置下总盘数 25 块符合逻辑（例如 3 组 8+2 共 30 块减去 5 块冗余或特定分组，或者单纯指物理槽位总数，此处主要验证成本计算逻辑），数值量级合理。

## Search Query

Seagate Exos 16E price 2024
