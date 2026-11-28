# N14: 本地/云端任务分配的决策函数为 Cost_Benefit(R) = (T_local - T_cloud) * Value(Iteration_Speed) -

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

本地/云端任务分配的决策函数为 Cost_Benefit(R) = (T_local - T_cloud) * Value(Iteration_Speed) - C_cloud(API_Cost)，其中 T_local 为本地推理延迟，T_cloud 为云端延迟+网络开销，C_cloud 为 API 费用。当任务复杂度评分（基于 token 数与逻辑深度）> 阈值 K 时，切换至云端，K 值需通过 A/B 测试确定，初始建议 K=1000 tokens/step。

## Corrected Claim

本地/云端任务分配的决策函数为 Cost_Benefit(R) = (T_local - T_cloud) * Value(Iteration_Speed) - C_cloud(API_Cost)，其中 T_local 为本地推理延迟，T_cloud 为云端延迟+网络开销，C_cloud 为 API 费用。当任务复杂度评分（基于 token 数与逻辑深度）> 阈值 K 时，切换至云端，K 值需通过 A/B 测试确定，初始建议 K=1000 tokens/step。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 933)
