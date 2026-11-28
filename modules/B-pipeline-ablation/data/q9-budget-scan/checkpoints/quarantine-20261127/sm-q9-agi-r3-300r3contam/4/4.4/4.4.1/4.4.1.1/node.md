# N180: Novelty 计算的 TopK 参数敏感性与去重预处理：TopK 默认取 10，需先对 Retrieved_Claims 进行 MinHash 去重（Jacc

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

Novelty 计算的 TopK 参数敏感性与去重预处理：TopK 默认取 10，需先对 Retrieved_Claims 进行 MinHash 去重（Jaccard Similarity > 0.8 视为重复），否则 CosineSimilarity 会被冗余高分拉偏，导致 Novelty 低估 15-20%。

## Corrected Claim

Novelty 计算中 TopK 参数及去重阈值（如 Jaccard Similarity）对结果敏感；通常需对 Retrieved_Claims 进行 MinHash 去重以避免冗余高分拉偏 CosineSimilarity，从而导致 Novelty 被低估。

## Evidence

[质询]TopK=10、Jaccard>0.8 以及 15-20% 的具体数值缺乏通用标准或第一性原理支持，属于特定系统调优的经验参数，不同场景下差异巨大。 | 先验知识/题面给定，逻辑校验通过（去重防止冗余拉高相似度从而低估新颖性是合理的逻辑链条），但具体数值（10, 0.8, 15-20%）为经验事实，无外部来源支持，故降级。

## Search Query

minhash deduplication cosine similarity novelty metric bias retrieval augmented generation
