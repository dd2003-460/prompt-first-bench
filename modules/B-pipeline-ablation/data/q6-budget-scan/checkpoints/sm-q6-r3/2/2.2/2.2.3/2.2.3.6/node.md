# N180: 公有云CDN稳态下的P99延迟分布模型：P99_Latency = P99_RTT + P(hit_miss)*P99_T_origin + TCP_Overh

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56, N57, N58

## Claim

公有云CDN稳态下的P99延迟分布模型：P99_Latency = P99_RTT + P(hit_miss)*P99_T_origin + TCP_Overhead_P99，其中P99_RTT为用户到边缘节点的P99，P(hit_miss)=0.05

## Corrected Claim

公有云CDN稳态下的P99延迟分布模型：P99_Latency = P99_RTT + P(hit_miss)*P99_T_origin + TCP_Overhead_P99，其中P99_RTT为用户到边缘节点的P99，P(hit_miss)=0.05

## Evidence

先验知识/题面给定，逻辑校验通过
