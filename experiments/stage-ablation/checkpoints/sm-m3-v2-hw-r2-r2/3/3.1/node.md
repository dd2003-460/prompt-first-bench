# N17: 外部记忆库应采用混合索引策略：向量数据库（如 FAISS）存储语义相似的文献片段，结构化笔记（如 Markdown/JSON）存储实验参数与结论；两者通过 ID

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

外部记忆库应采用混合索引策略：向量数据库（如 FAISS）存储语义相似的文献片段，结构化笔记（如 Markdown/JSON）存储实验参数与结论；两者通过 ID 关联，查询时先向量检索再结构化过滤，提升召回精度至 >90%。

## Corrected Claim

外部记忆库可采用混合索引策略：向量数据库（如 FAISS）存储语义相似的文献片段，结构化笔记（如 Markdown/JSON）存储实验参数与结论；两者通过 ID 关联，查询时先向量检索再结构化过滤，以提升召回精度。

## Evidence

[质询]“提升召回精度至 >90%”是一个具体的经验性能指标，其实际数值高度依赖于数据集规模、文档质量、嵌入模型及具体业务场景，并非混合索引策略的固有属性或必然结果，属于缺乏普遍适用性的过度量化断言。 | 先验知识/题面给定，逻辑校验通过（架构设计合理），但具体数值指标缺乏普适性支撑，故降级为定性表述。

## Search Query

hybrid retrieval vector database structured notes scientific research memory
