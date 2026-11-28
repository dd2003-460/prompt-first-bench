# N67: t_indexing 的计算模型：假设向量数据库为 FAISS-HNSW，索引构建时间 t_indexing ≈ O(N * log(N)) * t_compa

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

t_indexing 的计算模型：假设向量数据库为 FAISS-HNSW，索引构建时间 t_indexing ≈ O(N * log(N)) * t_compare，其中 N 为现有向量总数，t_compare 为单次向量比较耗时（M1 Max CPU 上约为 1μs/1024-dim vector），需根据当前知识库规模 N_current 计算具体秒数。

## Corrected Claim

t_indexing 的计算模型：假设向量数据库为 FAISS-HNSW，索引构建时间 t_indexing ≈ O(N * log(N)) * t_compare，其中 N 为现有向量总数，t_compare 为单次向量比较耗时（M1 Max CPU 上约为 1μs/1024-dim vector），需根据当前知识库规模 N_current 计算具体秒数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

FAISS HNSW indexing time complexity CPU
