# N211: 检索优先级降权函数：Effective_Retrieval_Score = Base_Relevance_Score * Priority_Multiplier

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

检索优先级降权函数：Effective_Retrieval_Score = Base_Relevance_Score * Priority_Multiplier(Confidence)，其中 Priority_Multiplier = 0.5 if Confidence < 0.3 else 1.0；这意味着低置信度知识的检索得分被减半，从而在混合检索排序中排后

## Corrected Claim

检索优先级降权函数：Effective_Retrieval_Score = Base_Relevance_Score * Priority_Multiplier(Confidence)，其中 Priority_Multiplier = 0.5 if Confidence < 0.3 else 1.0；这意味着低置信度知识的检索得分被减半，从而在混合检索排序中排后

## Evidence

先验知识/题面给定，逻辑校验通过
