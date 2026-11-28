# N196: S_task (任务复杂度评分) 的计算公式：S_task = 0.4 * Norm(ContextLen) + 0.3 * (1 - Avg_F1_Score

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

S_task (任务复杂度评分) 的计算公式：S_task = 0.4 * Norm(ContextLen) + 0.3 * (1 - Avg_F1_Score_Benchmark) + 0.3 * Tool_Call_Density，其中 Norm(ContextLen) = min(1, ContextLen/262144)，Tool_Call_Density 为每千字调用的工具次数，该分数需归一化至 [0,1] 后映射到 [6,9] 区间以匹配网格搜索范围。

## Corrected Claim

S_task (任务复杂度评分) 的计算公式：S_task = 0.4 * Norm(ContextLen) + 0.3 * (1 - Avg_F1_Score_Benchmark) + 0.3 * Tool_Call_Density，其中 Norm(ContextLen) = min(1, ContextLen/262144)，Tool_Call_Density 为每千字调用的工具次数，该分数需归一化至 [0,1] 后映射到 [6,9] 区间以匹配网格搜索范围。

## Evidence

先验知识/题面给定，逻辑校验通过
