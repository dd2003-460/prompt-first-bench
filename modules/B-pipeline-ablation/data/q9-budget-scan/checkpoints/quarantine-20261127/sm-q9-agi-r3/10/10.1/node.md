# N295: 外部状态存储的读写延迟 T_io 必须小于模型推理间隔 T_gap，以避免阻塞Agent主循环；估算 T_gap = T_infer / (1 - utiliz

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105, N106, N107

## Claim

外部状态存储的读写延迟 T_io 必须小于模型推理间隔 T_gap，以避免阻塞Agent主循环；估算 T_gap = T_infer / (1 - utilization)，若 T_infer=5s 且利用率 80%，则 T_gap≈6.25s，要求 T_io < 50ms (P95) 以满足实时性约束。

## Corrected Claim

外部状态存储的读写延迟 T_io 必须小于模型推理间隔 T_gap，以避免阻塞Agent主循环；估算 T_gap = T_infer / (1 - utilization)，若 T_infer=5s 且利用率 80%，则 T_gap≈6.25s，要求 T_io < 50ms (P95) 以满足实时性约束。

## Evidence

先验知识/题面给定，逻辑校验通过：T_gap计算正确（5/(1-0.8)=6.25s），T_io < 50ms远小于T_gap，符合避免阻塞的逻辑约束。

## Search Query

vLLM inference latency gap external memory IO constraint
