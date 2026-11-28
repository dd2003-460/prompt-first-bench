# N65: complexity_score 的量化公式定义为 CS = α * Depth_CoT + β * Scope_Retrieval，其中 Depth_CoT 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

complexity_score 的量化公式定义为 CS = α * Depth_CoT + β * Scope_Retrieval，其中 Depth_CoT 为任务所需的平均思维链步数（整数，1-20），Scope_Retrieval 为需检索的外部文档数量（整数，1-50）；α=0.6, β=0.4 为初始权重，需通过 50 组历史任务的准确率回归拟合确定。

## Corrected Claim

complexity_score 的量化公式定义为 CS = α * Depth_CoT + β * Scope_Retrieval，其中 Depth_CoT 为任务所需的平均思维链步数（整数，1-20），Scope_Retrieval 为需检索的外部文档数量（整数，1-50）；α=0.6, β=0.4 为初始权重，需通过 50 组历史任务的准确率回归拟合确定。

## Evidence

先验知识/题面给定，逻辑校验通过
