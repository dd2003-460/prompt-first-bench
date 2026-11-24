# N491: P99_miss_penalty 的构成公式：P99_miss_penalty = RTT_pop_origin + T_transfer_origin + T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N159, N160, N161

## Claim

P99_miss_penalty 的构成公式：P99_miss_penalty = RTT_pop_origin + T_transfer_origin + T_proc_origin，其中 RTT_pop_origin 约为 20-50ms（跨省骨干网），T_transfer_origin = s / B_origin（s 为对象大小，B_origin 为回源带宽），T_proc_origin 约为 5-10ms

## Corrected Claim

P99_miss_penalty 的构成公式：P99_miss_penalty = RTT_pop_origin + T_transfer_origin + T_proc_origin，其中 RTT_pop_origin 约为 20-50ms（跨省骨干网），T_transfer_origin = s / B_origin（s 为对象大小，B_origin 为回源带宽），T_proc_origin 约为 5-10ms

## Evidence

先验知识/题面给定，逻辑校验通过
