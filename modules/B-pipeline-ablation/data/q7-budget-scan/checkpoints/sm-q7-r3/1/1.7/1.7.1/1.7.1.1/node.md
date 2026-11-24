# N179: 温数据每日扫描产生的I/O时长占比 T_scan_ratio = (每日扫描次数 × 单次扫描I/O持续时间) / 86400秒，假设单次全量扫描100TB耗时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

温数据每日扫描产生的I/O时长占比 T_scan_ratio = (每日扫描次数 × 单次扫描I/O持续时间) / 86400秒，假设单次全量扫描100TB耗时约30分钟，则 T_scan_ratio ≈ 0.6%-1.2%，其余时间为Idle或低频随机读写。

## Corrected Claim

温数据每日扫描产生的I/O时长占比 T_scan_ratio = (每日扫描次数 × 单次扫描I/O持续时间) / 86400秒，假设单次全量扫描100TB耗时约30分钟，则 T_scan_ratio ≈ 0.6%-1.2%，其余时间为Idle或低频随机读写。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (30*60)/86400 ≈ 0.208%，若每日扫描3-6次则占比约为0.6%-1.25%，与陈述范围吻合，量级合理。
