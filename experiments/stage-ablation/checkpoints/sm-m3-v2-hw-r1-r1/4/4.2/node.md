# N27: 长期知识向量嵌入使用 BGE-M3 模型（1024维），单条记录存储开销为 1024*4 bytes = 4KB 向量 + 512 tokens * 2 byt

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

长期知识向量嵌入使用 BGE-M3 模型（1024维），单条记录存储开销为 1024*4 bytes = 4KB 向量 + 512 tokens * 2 bytes/token ≈ 1KB 元数据，总计 ~5KB/entry；V100 集群内存上限 64GB 可容纳约 12.8M 条独立知识单元

## Corrected Claim

长期知识向量嵌入使用 BGE-M3 模型（1024维），单条记录存储开销为 1024*4 bytes = 4KB 向量 + 512 tokens * 2 bytes/token ≈ 1KB 元数据，总计 ~5KB/entry；V100 集群内存上限 64GB 可容纳约 12.8M 条独立知识单元

## Evidence

先验知识/题面给定，逻辑校验通过：BGE-M3 维度确为 1024，float32 存储 4KB 正确；64GB / 5KB ≈ 12.8M 计算无误，量级合理。

## Search Query

BGE-M3 embedding dimensionality storage size vector database capacity
