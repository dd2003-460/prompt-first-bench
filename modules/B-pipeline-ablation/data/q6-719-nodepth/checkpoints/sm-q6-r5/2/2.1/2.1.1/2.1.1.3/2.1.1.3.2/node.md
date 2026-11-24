# N490: 连接利用率阈值 U_conn 的动态调整：U_conn = C_current / C_max，当 U_conn > 0.8 时触发限流；限流策略为拒绝新连接或

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

连接利用率阈值 U_conn 的动态调整：U_conn = C_current / C_max，当 U_conn > 0.8 时触发限流；限流策略为拒绝新连接或降低 QPS，导致 L_queue_wait 增加 ΔL = (Rejected_Requests / Total_Requests) * L_timeout；若 L_timeout = 50 ms，拒绝率 10%，则 ΔL = 5 ms。

## Corrected Claim

连接利用率阈值 U_conn 的动态调整：U_conn = C_current / C_max，当 U_conn > 0.8 时触发限流；限流策略为拒绝新连接或降低 QPS，导致 L_queue_wait 增加 ΔL = (Rejected_Requests / Total_Requests) * L_timeout；若 L_timeout = 50 ms，拒绝率 10%，则 ΔL = 5 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔL = (Rejected_Requests / Total_Requests) * L_timeout 在逻辑上自洽，代入数值 10% * 50ms = 5ms 计算正确，符合排队论中因拒绝/超时导致的平均等待时间增加的基本直觉。
