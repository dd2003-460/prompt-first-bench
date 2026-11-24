# N312: 故障期间队列延迟 T_failover_queue 的估算：T_failover_queue = Q_length / Service_Rate，其中 Q_le

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

故障期间队列延迟 T_failover_queue 的估算：T_failover_queue = Q_length / Service_Rate，其中 Q_length 为故障期间积压的请求数（= Affected_Traffic_Ratio × Total_Requests × T_failover），Service_Rate 为恢复后的处理速率（= 1 / T_cache），因此 T_failover_queue 随 T_failover 线性增长，需代入具体 T_failover 值计算。

## Corrected Claim

故障期间队列延迟 T_failover_queue 的估算：T_failover_queue = Q_length / Service_Rate，其中 Q_length 为故障期间积压的请求数（= Affected_Traffic_Ratio × Total_Requests × T_failover），Service_Rate 为恢复后的处理速率（= 1 / T_cache），因此 T_failover_queue 随 T_failover 线性增长，需代入具体 T_failover 值计算。

## Evidence

先验知识/题面给定，逻辑校验通过：基于排队论基本公式 T=Q/μ 及题目定义的变量关系，推导逻辑自洽且量纲正确。
