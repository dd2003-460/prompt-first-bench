# N15: 外部记忆库采用混合检索架构：语义向量(Milvus, dim=1536) + 关键词倒排索引(Elasticsearch)，存储单元为'原子事实'，每条记录包含

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

外部记忆库采用混合检索架构：语义向量(Milvus, dim=1536) + 关键词倒排索引(Elasticsearch)，存储单元为'原子事实'，每条记录包含{content, source_paper_id, confidence_score, timestamp}，检索权重w_semantic=0.7, w_keyword=0.3

## Corrected Claim

外部记忆库采用混合检索架构：语义向量(Milvus, dim=1536) + 关键词倒排索引(Elasticsearch)，存储单元为'原子事实'，每条记录包含{content, source_paper_id, confidence_score, timestamp}，检索权重w_semantic=0.7, w_keyword=0.3

## Evidence

先验知识/题面给定，逻辑校验通过
