# N14: 外部记忆模块采用向量数据库 (如 ChromaDB/Faiss) 存储研究文献，针对 27B 模型的 Embedding 维度 (1024-dim)，索引 10

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

外部记忆模块采用向量数据库 (如 ChromaDB/Faiss) 存储研究文献，针对 27B 模型的 Embedding 维度 (1024-dim)，索引 100 万篇论文所需的内存约为 100M × 1024 × 4 bytes ≈ 409 GB，超出 MacBook M1 Max 32GB 内存限制；因此，必须采用分片加载策略或 HNSW 索引优化，将查询延迟控制在 <50ms，并通过 Rerank 模型 (Cross-Encoder) 提升 Top-K 召回率至 85% 以上。

## Corrected Claim

外部记忆模块采用向量数据库 (如 ChromaDB/Faiss) 存储研究文献，针对 27B 模型的 Embedding 维度 (1024-dim)，索引 100 万篇论文所需的原始向量内存约为 409 GB，超出 MacBook M1 Max 32GB 内存限制；因此，必须采用分片加载策略或 HNSW 索引优化以控制内存与查询延迟，并通过 Rerank 模型 (Cross-Encoder) 提升检索精度。

## Evidence

[质询]陈述中关于“Top-K 召回率提升至 85% 以上”的具体数值缺乏通用基准支持，召回率高度依赖于数据集分布、K 值大小及具体任务定义，并非 Cross-Encoder 的固有属性或固定指标；此外，HNSW 索引本身会显著增加内存占用（通常比原始向量多 20%-50%），直接断言 409GB 为总需求而未计入索引开销，可能导致内存估算偏低。 | 先验知识/题面给定，逻辑校验通过：内存计算量级正确（100M*1024*4B=409.6GB），确实远超 32GB 限制，需分片或优化；但召回率具体数值属经验性指标，非第一性原理可推导，且无外部来源支持，故降级。

## Search Query

Vector database HNSW index memory footprint 1M documents embedding dimension
