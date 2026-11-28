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

父节点级核验未通过：不完备（子节点分别针对嵌入模型、检索权重、置信度机制和时间戳衰减进行了独立定义，彼此之间无逻辑重叠或矛盾，正交性良好。然而，父节点明确提到了“关键词倒排索引(Elasticsearch)”作为混合检索的一部分，但四个子节点中没有任何一个涉及关键词索引的具体配置、分词策略或匹配规则（如BM25参数），导致对“关键词”这一核心组件的实现细节缺失，因此不完备。）
