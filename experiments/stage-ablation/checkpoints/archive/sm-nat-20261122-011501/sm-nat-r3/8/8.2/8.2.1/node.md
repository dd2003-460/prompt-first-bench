# N166: 独立假设下 Top-K 对象平均大小的解析近似：E[S|TopK]_indep ≈ s_min * (K/N)^{1/α} * (1 + 1/(α-1))，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N72

## Claim

独立假设下 Top-K 对象平均大小的解析近似：E[S|TopK]_indep ≈ s_min * (K/N)^{1/α} * (1 + 1/(α-1))，其中 α=1.1，K/N 为 Top 比例（如 0.05-0.10），用于建立负相关修正的基准线。

## Corrected Claim

独立假设下 Top-K 对象平均大小的解析近似：E[S|TopK]_indep ≈ s_min * (K/N)^{1/α} * (1 + 1/(α-1))，其中 α=1.1，K/N 为 Top 比例（如 0.05-0.10），用于建立负相关修正的基准线。

## Evidence

先验知识/题面给定，逻辑校验通过
