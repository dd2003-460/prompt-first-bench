# N27: 外部记忆检索噪声比：向量数据库 Top-K 检索中，相关文档占比（Precision@K）在科研文献库中通常低于 40%，导致上下文窗口污染，影响推理可靠性

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

外部记忆检索噪声比：向量数据库 Top-K 检索中，相关文档占比（Precision@K）在科研文献库中通常低于 40%，导致上下文窗口污染，影响推理可靠性

## Corrected Claim

在科研文献库的向量检索中，Top-K 结果的相关文档占比（Precision@K）往往较低，可能导致上下文窗口污染并影响推理可靠性。

## Evidence

[质询]「通常低于 40%」这一具体数值阈值缺乏普适性，高度依赖于检索策略、嵌入模型质量及文献库的领域特异性，将其作为通用经验事实过于绝对。 | 先验知识/题面给定，逻辑校验通过；但具体数值阈值属于经验事实，缺乏来源直接支持，故降级。

## Search Query

RAG precision at K scientific literature vector database noise ratio
