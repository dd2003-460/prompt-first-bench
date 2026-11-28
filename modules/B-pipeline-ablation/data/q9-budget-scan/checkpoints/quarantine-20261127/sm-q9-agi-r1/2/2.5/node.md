# N17: 记忆数据库的向量检索配置：使用FAISS库构建HNSW索引，维度=1536（与嵌入模型匹配），M=32，efSearch=64，Top-K检索延迟≤50ms（在

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

记忆数据库的向量检索配置：使用FAISS库构建HNSW索引，维度=1536（与嵌入模型匹配），M=32，efSearch=64，Top-K检索延迟≤50ms（在M1 Max CPU上），存储容量支持≥100万条记录，每条记录包含原文摘要、元数据（时间戳、来源、置信度）与嵌入向量。

## Corrected Claim

记忆数据库的向量检索配置：使用FAISS库构建HNSW索引，维度=1536（与嵌入模型匹配），M=32，efSearch=64，Top-K检索延迟≤50ms（在M1 Max CPU上），存储容量支持≥100万条记录，每条记录包含原文摘要、元数据（时间戳、来源、置信度）与嵌入向量。

## Evidence

先验知识/题面给定，逻辑校验通过：FAISS HNSW参数（M=32, efSearch=64）符合常规配置，1536维对应主流嵌入模型，M1 Max CPU性能足以支撑百万级向量50ms内检索，各组件描述自洽。

## Search Query

FAISS HNSW index parameters M efSearch latency M1 Max vector database
