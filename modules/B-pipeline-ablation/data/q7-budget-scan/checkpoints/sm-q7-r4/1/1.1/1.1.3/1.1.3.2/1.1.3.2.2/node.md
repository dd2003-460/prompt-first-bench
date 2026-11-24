# N423: 基于保守带宽的重建时间重算：若 T_sync_eff = 2GB/s，V_disk = 8TB = 8,000,000MB。T_rebuild_raw = 8,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

基于保守带宽的重建时间重算：若 T_sync_eff = 2GB/s，V_disk = 8TB = 8,000,000MB。T_rebuild_raw = 8,000,000 / 2,000 = 4,000秒 ≈ 1.11小时。加上系统开销（监控检测、校验、元数据更新）约0.5小时，总 T_rebuild ≈ 1.61小时。若带宽进一步降至1GB/s（高负载时），T_rebuild 可达 2.22小时 + 0.5小时 ≈ 2.72小时。

## Corrected Claim

基于保守带宽的重建时间重算：若 T_sync_eff = 2GB/s，V_disk = 8TB = 8,000,000MB。T_rebuild_raw = 8,000,000 / 2,000 = 4,000秒 ≈ 1.11小时。加上系统开销（监控检测、校验、元数据更新）约0.5小时，总 T_rebuild ≈ 1.61小时。若带宽进一步降至1GB/s（高负载时），T_rebuild 可达 2.22小时 + 0.5小时 ≈ 2.72小时。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算准确（8000000/2000=4000s≈1.11h; 8000000/1000=8000s≈2.22h），单位换算正确，总时间叠加逻辑自洽。
