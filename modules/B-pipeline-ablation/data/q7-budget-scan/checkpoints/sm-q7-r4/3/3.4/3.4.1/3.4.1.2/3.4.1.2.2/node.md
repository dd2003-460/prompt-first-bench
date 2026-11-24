# N639: 从备份服务器恢复 500TB 数据的耗时 T_restore_backup：T_restore = V_data / Restore_Bandwidth；假设备

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N221

## Claim

从备份服务器恢复 500TB 数据的耗时 T_restore_backup：T_restore = V_data / Restore_Bandwidth；假设备份服务器通过 10Gbps 网络连接，有效传输带宽为 1GB/s (10Gbps/8 * 0.8 效率)，则 T_restore = 500,000 GB / 1 GB/s = 500,000 秒 ≈ 138.9 小时；若使用 25Gbps 链路，则 T_restore ≈ 55.6 小时。

## Corrected Claim

从备份服务器恢复 500TB 数据的耗时 T_restore_backup：T_restore = V_data / Restore_Bandwidth；假设备份服务器通过 10Gbps 网络连接，有效传输带宽为 1GB/s (10Gbps/8 * 0.8 效率)，则 T_restore = 500,000 GB / 1 GB/s = 500,000 秒 ≈ 138.9 小时；若使用 25Gbps 链路，则 T_restore ≈ 55.6 小时。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算（10Gbps≈1.25GB/s，80%效率后为1GB/s）及时间计算（500,000秒≈138.9小时，25Gbps对应55.6小时）均符合物理与数学逻辑。
