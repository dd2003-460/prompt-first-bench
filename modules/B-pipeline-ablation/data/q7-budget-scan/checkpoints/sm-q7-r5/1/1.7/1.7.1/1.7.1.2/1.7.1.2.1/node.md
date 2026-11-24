# N412: 冷数据纯空闲工作点：I/O占比为0%，Idle占比100%，此时HDD平均功耗 W_HDD_idle ≈ 0.75W (Spin-down) 或 4.5W (A

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N180

## Claim

冷数据纯空闲工作点：I/O占比为0%，Idle占比100%，此时HDD平均功耗 W_HDD_idle ≈ 0.75W (Spin-down) 或 4.5W (Active Idle)，SSD平均功耗 W_SSD_idle ≈ 1.0-1.5W，该点是功耗成本下界

## Corrected Claim

冷数据纯空闲工作点：I/O占比为0%，Idle占比100%，此时HDD平均功耗 W_HDD_idle ≈ 0.75W (Spin-down) 或 4.5W (Active Idle)，SSD平均功耗 W_SSD_idle ≈ 1.0-1.5W，该点是功耗成本下界

## Evidence

先验知识/题面给定，逻辑校验通过：HDD Spin-down (~0.75W) 和 Active Idle (~4.5W) 以及 SSD Idle (~1.0-1.5W) 的功耗数值符合主流硬件工程常识，且作为冷数据空闲状态下的功耗下界在逻辑上自洽。
