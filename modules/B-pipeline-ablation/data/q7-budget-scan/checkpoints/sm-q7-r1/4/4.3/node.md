# N24: 恢复时间公式 T_restore = (Data_Size / Restore_Throughput) + Overhead_Time，其中Data_Size为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

恢复时间公式 T_restore = (Data_Size / Restore_Throughput) + Overhead_Time，其中Data_Size为需恢复数据量（温数据100TB+冷数据400TB，视故障范围而定），Overhead_Time为切换/校验时间（约1-2h）

## Corrected Claim

恢复时间公式 T_restore = (Data_Size / Restore_Throughput) + Overhead_Time，其中Data_Size为需恢复数据量（温数据100TB+冷数据400TB，视故障范围而定），Overhead_Time为切换/校验时间（约1-2h）

## Evidence

先验知识/题面给定，逻辑校验通过：恢复时间由数据传输时间（数据量/吞吐量）和固定开销（切换/校验）组成，符合基本物理/工程直觉，量级合理（100-500TB数据在典型存储恢复速率下耗时数小时至数十小时，加上1-2小时开销，总时长逻辑自洽）。

## Search Query

data recovery time calculation formula throughput overhead
