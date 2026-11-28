# N186: Cost_cloud 的精确计算公式为 Cost_cloud = (Input_Tokens * P_input + Output_Tokens * P_out

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

Cost_cloud 的精确计算公式为 Cost_cloud = (Input_Tokens * P_input + Output_Tokens * P_output) + Latency_Penalty，其中 Input/Output Tokens 基于任务复杂度预估（复杂模拟≈5k in/1k out，综述≈2k in/2k out），Latency_Penalty = (T_cloud - T_local) * Hourly_Rate/3600，Hourly_Rate 设为 50 元/小时以统一人力机会成本口径。

## Corrected Claim

Cost_cloud 的精确计算公式为 Cost_cloud = (Input_Tokens * P_input + Output_Tokens * P_output) + Latency_Penalty，其中 Input/Output Tokens 基于任务复杂度预估（复杂模拟≈5k in/1k out，综述≈2k in/2k out），Latency_Penalty = (T_cloud - T_local) * Hourly_Rate/3600，Hourly_Rate 设为 50 元/小时以统一人力机会成本口径。

## Evidence

先验知识/题面给定，逻辑校验通过
