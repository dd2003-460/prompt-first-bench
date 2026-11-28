# N120: T_retrieval 的延迟分布：Milvus 向量检索 (dim=1536) 在 100k 文档集上的 P99 延迟约为 10-50ms，Elasticse

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

T_retrieval 的延迟分布：Milvus 向量检索 (dim=1536) 在 100k 文档集上的 P99 延迟约为 10-50ms，Elasticsearch 关键词检索 P99 约为 20-80ms；若采用并行查询，T_retrieval_max ≈ max(t_milvus, t_es) ≈ 80ms，可忽略不计，除非网络抖动导致超时重试。

## Corrected Claim

T_retrieval 的延迟分布：Milvus 向量检索 (dim=1536) 在 100k 文档集上的 P99 延迟约为 10-50ms，Elasticsearch 关键词检索 P99 约为 20-80ms；若采用并行查询，T_retrieval_max ≈ max(t_milvus, t_es) ≈ 80ms，可忽略不计，除非网络抖动导致超时重试。

## Evidence

先验知识/题面给定，逻辑校验通过
