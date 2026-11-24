# N127: NVMe SSD 阵列总功耗 P_total_NVMe = P_drives + P_infra，其中 P_drives = N_disks * W_drive

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

NVMe SSD 阵列总功耗 P_total_NVMe = P_drives + P_infra，其中 P_drives = N_disks * W_drive_avg，P_infra = (P_controller + P_backplane + P_cooling_fan + P_PDU_loss)。

## Corrected Claim

NVMe SSD 阵列总功耗 P_total_NVMe = P_drives + P_infra，其中 P_drives = N_disks * W_drive_avg，P_infra = (P_controller + P_backplane + P_cooling_fan + P_PDU_loss)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data center storage array power consumption breakdown drives infrastructure overhead
