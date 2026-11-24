# N499: 增量需求计算：现有HDD数量 N_existing = 145块（基于400TB冷数据 + RAID6冗余）。需新增盘数 ΔN = N_total - N_ex

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N218

## Claim

增量需求计算：现有HDD数量 N_existing = 145块（基于400TB冷数据 + RAID6冗余）。需新增盘数 ΔN = N_total - N_existing = 300 - 145 = 155块。新增容量 C_add = 155 * 16TB = 2,480TB（物理），有效容量增加约 155 * 16 * 0.8 = 1,984TB（考虑RAID6开销）。

## Corrected Claim

增量需求计算：现有HDD数量 N_existing = 145块（基于400TB冷数据 + RAID6冗余）。需新增盘数 ΔN = N_total - N_existing = 300 - 145 = 155块。新增容量 C_add = 155 * 16TB = 2,480TB（物理），有效容量增加约 155 * 16 * 0.8 = 1,984TB（考虑RAID6开销）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（300-145=155, 155*16=2480, 2480*0.8=1984），RAID6效率系数0.8符合常见配置假设，量纲与逻辑自洽。
