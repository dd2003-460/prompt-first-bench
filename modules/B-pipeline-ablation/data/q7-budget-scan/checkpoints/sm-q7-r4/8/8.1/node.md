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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个独立组成部分（P_drives 和 P_infra），职责划分清晰，无重叠或矛盾。子节点1明确了驱动盘功耗的计算逻辑与数值，子节点2详细展开了基础设施功耗的构成比例及估算方法，两者共同完整覆盖了父节点定义的总功耗模型，且未出现将同一参数在不同子节点中重复定义的情况。）

## Search Query

data center storage array power consumption breakdown drives infrastructure overhead
