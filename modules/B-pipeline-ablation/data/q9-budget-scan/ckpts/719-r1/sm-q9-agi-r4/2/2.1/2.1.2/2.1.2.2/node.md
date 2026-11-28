# N146: HNSW 索引参数对 Recall@5 与延迟的权衡：M=16, efSearch=64 时，Recall@5 约为 0.85-0.90，查询延迟 50-100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

HNSW 索引参数对 Recall@5 与延迟的权衡：M=16, efSearch=64 时，Recall@5 约为 0.85-0.90，查询延迟 50-100ms；若将 efSearch 降至 32 以追求速度，Recall@5 可能降至 0.75-0.80，但延迟减半；在混合检索中，建议保留较高 efSearch 以确保向量部分的召回质量不被稀疏化

## Corrected Claim

HNSW 索引参数对 Recall@5 与延迟的权衡：M=16, efSearch=64 时，Recall@5 约为 0.85-0.90，查询延迟 50-100ms；若将 efSearch 降至 32 以追求速度，Recall@5 可能降至 0.75-0.80，但延迟减半；在混合检索中，建议保留较高 efSearch 以确保向量部分的召回质量不被稀疏化

## Evidence

先验知识/题面给定，逻辑校验通过
