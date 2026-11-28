# N62: FAISS HNSW 索引在 100k 文档、1024 维向量下的内存占用约为 1.2GB (Index + Vectors)，加上元数据约 2GB，完全适配 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

FAISS HNSW 索引在 100k 文档、1024 维向量下的内存占用约为 1.2GB (Index + Vectors)，加上元数据约 2GB，完全适配 M1 Max 16GB 内存限制；查询延迟 T_query 随 efSearch 参数变化：efSearch=32 时 T_query≈30ms 但 Recall@10 降至 0.85；efSearch=128 时 T_query≈80ms 但 Recall@10 提升至 0.95。推荐 efSearch=64 作为精度/速度平衡点。

## Corrected Claim

FAISS HNSW 索引在 100k 文档、1024 维向量下的内存占用通常在 1-2GB 量级，适配 16GB 内存；查询延迟与 Recall@10 随 efSearch 增加呈正相关（延迟升高，召回提升），具体数值需根据实际硬件和数据集基准测试确定，通常 efSearch=64 可作为平衡点参考。

## Evidence

[质询]具体数值（1.2GB内存、30ms/80ms延迟、0.85/0.95召回率）属于高度依赖硬件环境（M1 Max CPU/GPU加速情况）、数据集分布及FAISS版本的具体经验测量值，无法从第一性原理推导，且参考来源仅为通用教程，未提供该特定配置下的精确基准测试数据，存在数值不准确的风险。 | 逻辑自洽（HNSW内存估算符合向量大小+图结构开销，efSearch与Recall/Latency权衡符合HNSW算法特性），但参考来源[1][2][3]仅涉及HNSW原理及参数调优方法论，未提供100k/1024维在M1 Max上的具体性能基准数据，属于经验事实且缺乏直接来源支持。

## Search Query

FAISS HNSW memory usage 100k vectors 1024 dimensions query latency efSearch recall tradeoff

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00968/article/details/151502951&rut=b2b1ec8e24a58c0b55f89644b56ec908014b66b96705399d421a3a4073143ae0', 'type': 'ddg', 'title': '从90%到99%：Faiss HNSW索引精度优化实战指南 - CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00291/article/details/156022439&rut=60855c8290a5f427bbffbc644a694ec34b25b58d67b3003bbf81554c33a87ccb', 'type': 'ddg', 'title': '从90%到99%：Faiss HNSW索引精度优化实战指南 - CSDN博客'}
- {'url': 'https://longfei.space/posts/2025-10-22-hnsw-in-faiss/&rut=e44736a64ff6e71d7c7745933159d6aebd300d3ba175b133a4d43ce601cdea1a', 'type': 'ddg', 'title': "HNSW 索引实现（faiss） - Longfei's Miniblog"}
