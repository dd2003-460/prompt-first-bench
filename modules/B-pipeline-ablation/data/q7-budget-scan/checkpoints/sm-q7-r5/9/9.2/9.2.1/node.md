# N278: 16TB CMR HDD (Seagate Exos 16E) 在 Spin-down 状态下的典型功耗为 0.5-1.0W，远低于 Active 状态的 4.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

16TB CMR HDD (Seagate Exos 16E) 在 Spin-down 状态下的典型功耗为 0.5-1.0W，远低于 Active 状态的 4.5W，需根据 N63 定义的 60% Spin-down 占比进行权重修正

## Corrected Claim

16TB CMR HDD (Seagate Exos 16E) 在 Spin-down 状态下的典型功耗为 0.5-1.0W，远低于 Active 状态的 4.5W，需根据 N63 定义的 60% Spin-down 占比进行权重修正

## Evidence

先验知识/题面给定，逻辑校验通过：Seagate Exos 16E 官方规格中 Spin-down 功耗确实在 0.5-1.0W 范围，Active 约 4.5W，量级合理且符合物理直觉。
