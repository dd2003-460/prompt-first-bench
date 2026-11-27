# N70: 多卡 TP 方案的实际吞吐率 T_actual 受通信同步阻塞影响，其上限为 T_single / (1 + T_comm / T_compute_per_la

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

多卡 TP 方案的实际吞吐率 T_actual 受通信同步阻塞影响，其上限为 T_single / (1 + T_comm / T_compute_per_layer)，其中 T_compute_per_layer 为单层前向+反向计算时间，需通过实测获取

## Corrected Claim

多卡 TP 方案的实际吞吐率 T_actual 受通信同步阻塞影响，其上限为 T_single / (1 + T_comm / T_compute_per_layer)，其中 T_compute_per_layer 为单层前向+反向计算时间，需通过实测获取

## Evidence

先验知识/题面给定，逻辑校验通过
