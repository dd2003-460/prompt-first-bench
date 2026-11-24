# N478: NVMe SSD阵列静态功耗修正：40块2.5" NVMe SSD在Idle状态下的典型功耗为6-8W/盘，取中值7W，总静态功耗 P_idle_total =

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N161

## Claim

NVMe SSD阵列静态功耗修正：40块2.5" NVMe SSD在Idle状态下的典型功耗为6-8W/盘，取中值7W，总静态功耗 P_idle_total = 40 * 7W = 280W；若包含RAID卡及背板静态功耗(约50W)，系统级静态功耗基线为330W。

## Corrected Claim

NVMe SSD阵列静态功耗修正：40块2.5" NVMe SSD在Idle状态下的典型功耗为6-8W/盘，取中值7W，总静态功耗 P_idle_total = 40 * 7W = 280W；若包含RAID卡及背板静态功耗(约50W)，系统级静态功耗基线为330W。

## Evidence

先验知识/题面给定，逻辑校验通过
