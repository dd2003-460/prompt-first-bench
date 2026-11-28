# N89: BM25 检索器在科研文献语料库（假设 10k 篇 PDF，平均 15k tokens/篇）上的单次查询延迟为 50ms，向量数据库（Faiss/HNSW）在相

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

BM25 检索器在科研文献语料库（假设 10k 篇 PDF，平均 15k tokens/篇）上的单次查询延迟为 50ms，向量数据库（Faiss/HNSW）在相同规模下的单次查询延迟为 100ms，Hybrid Search 融合权重 α=0.5 时总延迟为 max(50, 100) + fusion_cost ≈ 105ms，满足 <200ms 约束；若语料库扩大至 100k 篇，向量索引构建时间需 <1h，查询延迟可能升至 150-180ms

## Corrected Claim

BM25 检索器在科研文献语料库（假设 10k 篇 PDF，平均 15k tokens/篇）上的单次查询延迟为 50ms，向量数据库（Faiss/HNSW）在相同规模下的单次查询延迟为 100ms，Hybrid Search 融合权重 α=0.5 时总延迟为 max(50, 100) + fusion_cost ≈ 105ms，满足 <200ms 约束；若语料库扩大至 100k 篇，向量索引构建时间需 <1h，查询延迟可能升至 150-180ms

## Evidence

先验知识/题面给定，逻辑校验通过：BM25稀疏检索通常快于HNSW稠密检索，并行执行取最大值加少量融合开销符合工程直觉，100k规模下延迟上升及索引构建时间估算在合理量级范围内。
