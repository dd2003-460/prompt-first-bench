# N498: 基础参数修正：单盘有效写带宽 W_eff_drive = 150 MB/s（N69修正值） * 0.6（效率折损，N216引用） = 90 MB/s。目标聚合带

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N218

## Claim

基础参数修正：单盘有效写带宽 W_eff_drive = 150 MB/s（N69修正值） * 0.6（效率折损，N216引用） = 90 MB/s。目标聚合带宽 W_target = 27,000 MB/s（4小时RTO要求）。所需总盘数 N_total = W_target / W_eff_drive = 27,000 / 90 = 300块。

## Corrected Claim

基础参数修正：单盘有效写带宽 W_eff_drive = 150 MB/s（N69修正值） * 0.6（效率折损，N216引用） = 90 MB/s。目标聚合带宽 W_target = 27,000 MB/s（4小时RTO要求）。所需总盘数 N_total = W_target / W_eff_drive = 27,000 / 90 = 300块。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 150*0.6=90 及 27000/90=300 正确，量纲一致（MB/s 除以 MB/s 得到无量纲数量），符合存储容量规划的基本逻辑。
