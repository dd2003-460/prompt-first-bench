# N555: 3.84TB NVMe SSD 方案下的驱动总功耗 P_drives_3.84TB = N_disks_3.84TB * W_drive_avg_3.84TB，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N239

## Claim

3.84TB NVMe SSD 方案下的驱动总功耗 P_drives_3.84TB = N_disks_3.84TB * W_drive_avg_3.84TB，其中 N_disks_3.84TB = 236，W_drive_avg_3.84TB 基于 3.84TB 企业级 NVMe SSD 典型功耗（Active 25W, Idle 1.5W，加权 50% Active/50% Idle 得 13.25W，参考 N282 修正逻辑），故 P_drives_3.84TB = 236 * 13.25W ≈ 3,127W

## Corrected Claim

3.84TB NVMe SSD 方案下的驱动总功耗 P_drives_3.84TB = N_disks_3.84TB * W_drive_avg_3.84TB，其中 N_disks_3.84TB = 236，W_drive_avg_3.84TB 基于 3.84TB 企业级 NVMe SSD 典型功耗（Active 25W, Idle 1.5W，加权 50% Active/50% Idle 得 13.25W，参考 N282 修正逻辑），故 P_drives_3.84TB = 236 * 13.25W ≈ 3,127W

## Evidence

先验知识/题面给定，逻辑校验通过：236 * 13.25 = 3127，计算无误；3.84TB企业级NVMe SSD典型功耗范围（Active ~25W, Idle ~1.5W）符合行业常识，加权平均逻辑自洽。
