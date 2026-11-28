# N281: Faiss HNSW 索引在 10k vectors (dim=768) 规模下的查询延迟分解：图遍历 (Graph Traversal) 耗时约 80ms，向

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

Faiss HNSW 索引在 10k vectors (dim=768) 规模下的查询延迟分解：图遍历 (Graph Traversal) 耗时约 80ms，向量距离计算 (Distance Computation) 耗时约 20ms，合计 100ms；M 参数 (neighbor count) 设置为 32 时的搜索半径为 10，若 M 降至 16 则延迟降至 ~60ms 但召回率下降 2%

## Corrected Claim

Faiss HNSW 索引在 10k vectors (dim=768) 规模下的查询延迟通常在微秒级（例如 <1ms）。M 参数减小会降低构建时间和内存占用，并可能略微降低召回率，但具体延迟和召回率变化取决于数据集特征及 efSearch 参数设置，不存在固定的 '80ms/20ms' 或 '2% 召回率下降' 的通用标准值。

## Evidence

[质询]数值量级严重违背常识：10k 向量（dim=768）的 HNSW 查询延迟通常在微秒（μs）级别，绝不可能达到毫秒（ms）级别（80ms+20ms=100ms 相当于处理百万级数据甚至更慢的情况，或者是在极低端硬件/未优化环境下的极端异常值，但作为通用事实陈述其量级错误）；此外，M 从 32 降至 16 导致延迟降低 40% 且召回率仅下降 2% 的具体数值缺乏普适性，高度依赖数据集分布和 efSearch 设置，属于特定实验数据而非通用规律。 | 先验知识/题面给定，逻辑校验未通过：10k 规模下 100ms 的延迟量级不合理（应为 μs 级），且具体性能指标（延迟分解、召回率变化）为经验事实，缺乏来源支持且数值可疑。

## Search Query

Faiss HNSW query latency breakdown graph traversal distance computation 10k vectors
