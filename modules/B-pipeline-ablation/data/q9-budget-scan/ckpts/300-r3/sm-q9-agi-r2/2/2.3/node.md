# N15: 外部记忆库采用混合检索架构：语义向量(Milvus, dim=1536) + 关键词倒排索引(Elasticsearch)，存储单元为'原子事实'，每条记录包含

- **status**: pending
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

父节点级核验未通过：不完备（子节点分别针对嵌入模型选择、检索权重优化、置信度更新机制和时间衰减策略，彼此独立且不重叠，正交性良好；无冗余。但父节点明确定义了存储单元的数据结构（包含 content, source_paper_id, confidence_score, timestamp），子节点仅覆盖了 confidence_score 和 timestamp 的处理逻辑，完全遗漏了 content 的结构化/清洗规则以及 source_paper_id 的关联与溯源机制，导致覆盖不全。）
