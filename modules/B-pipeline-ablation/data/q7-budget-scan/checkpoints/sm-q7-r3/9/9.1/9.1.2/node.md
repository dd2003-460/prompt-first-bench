# N275: SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD_cache = 14 * 4.45W (N92 修正值) ≈ 62W。N130 原估 1.425kW 严重高估，因误用了 95 块盘和 15W 单盘功耗

## Corrected Claim

SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD_cache = 14 * 4.45W (N92 修正值) ≈ 62W。N130 原估 1.425kW 严重高估，因误用了 95 块盘和 15W 单盘功耗

## Evidence

先验知识/题面给定，逻辑校验通过：100TB/7.68TB≈13.02，考虑RAID6冗余取14块合理；14*4.45W=62.3W≈62W，计算无误；原估1.425kW确为高估。

## Search Query

ssd cache layer power consumption small capacity tier
