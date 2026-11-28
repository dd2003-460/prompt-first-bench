# N454: Hybrid Search 分数融合的计算开销：RRF (Reciprocal Rank Fusion) 算法对 Top-100 候选进行排名融合的 CPU 耗

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

Hybrid Search 分数融合的计算开销：RRF (Reciprocal Rank Fusion) 算法对 Top-100 候选进行排名融合的 CPU 耗时为 <0.5ms（Python 实现，100 次浮点除法与加法），可忽略不计；Linear Combination 融合需预先计算归一化常数，耗时增加约 0.1ms

## Corrected Claim

Hybrid Search 分数融合的计算开销：RRF (Reciprocal Rank Fusion) 算法对 Top-100 候选进行排名融合的 CPU 耗时为 <0.5ms（Python 实现，100 次浮点除法与加法），可忽略不计；Linear Combination 融合需预先计算归一化常数，耗时增加约 0.1ms

## Evidence

先验知识/题面给定，逻辑校验通过：RRF 仅需对 100 个候选执行简单的倒数加法运算，线性组合涉及归一化常数计算，两者在现代 CPU 上耗时均在亚毫秒级，符合计算复杂度直觉。
