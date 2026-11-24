# N24: 恢复时间公式 T_restore = (Data_Size / Restore_Throughput) + Overhead_Time，其中Data_Size为

- **status**: pending
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

父节点级核验失败（LLM 错误）：Expecting ',' delimiter: line 10 column 69 (char 980)

## Search Query

data recovery time calculation formula throughput overhead
