# N69: 温数据有效扫描时间窗口 T_scan_window = 24h - T_non_scan_tasks，假设非扫描任务占用20%时间，则 T_scan_windo

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

温数据有效扫描时间窗口 T_scan_window = 24h - T_non_scan_tasks，假设非扫描任务占用20%时间，则 T_scan_window ≈ 19.2h；在4h内完成扫描的约束下，安全系数 SF = 19.2h / 4h = 4.8，允许吞吐冗余倍数为4.8倍

## Corrected Claim

温数据有效扫描时间窗口 T_scan_window = 24h - T_non_scan_tasks，假设非扫描任务占用20%时间，则 T_scan_window ≈ 19.2h；在4h内完成扫描的约束下，安全系数 SF = 19.2h / 4h = 4.8，允许吞吐冗余倍数为4.8倍

## Evidence

先验知识/题面给定，逻辑校验通过：24h * (1 - 20%) = 19.2h，19.2h / 4h = 4.8，计算无误且定义自洽。
