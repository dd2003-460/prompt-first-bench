# N326: 相关系数 r 的计算需使用 Spearman 秩相关而非 Pearson，因为 p% 和 k% 可能非正态分布；Spearman r = 1 - (6 * su

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

相关系数 r 的计算需使用 Spearman 秩相关而非 Pearson，因为 p% 和 k% 可能非正态分布；Spearman r = 1 - (6 * sum(d_i^2)) / (n(n^2-1))，其中 d_i 为秩差。

## Corrected Claim

相关系数 r 的计算需使用 Spearman 秩相关而非 Pearson，因为 p% 和 k% 可能非正态分布；Spearman r = 1 - (6 * sum(d_i^2)) / (n(n^2-1))，其中 d_i 为秩差。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Spearman rank correlation coefficient formula non-normal data
