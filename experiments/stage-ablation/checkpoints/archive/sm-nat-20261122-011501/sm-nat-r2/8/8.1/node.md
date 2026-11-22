# N68: Pareto(β=0.9) 热度分布下，Top-K 对象覆盖的请求比例精确公式为 P_access(K) = (Σ_{i=1}^{K} i^{-0.9}) / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

Pareto(β=0.9) 热度分布下，Top-K 对象覆盖的请求比例精确公式为 P_access(K) = (Σ_{i=1}^{K} i^{-0.9}) / (Σ_{j=1}^{N} j^{-0.9})；由于 β<1，分母近似为 N^{0.1}/0.1，分子近似为 K^{0.1}/0.1，因此 P_access(K) ≈ (K/N)^{0.1}，但需加上截断误差项 O(1/K^{0.1})。

## Corrected Claim

Pareto(β=0.9) 热度分布下，Top-K 对象覆盖的请求比例精确公式为 P_access(K) = (Σ_{i=1}^{K} i^{-0.9}) / (Σ_{j=1}^{N} j^{-0.9})；由于 β<1，分母近似为 N^{0.1}/0.1，分子近似为 K^{0.1}/0.1，因此 P_access(K) ≈ (K/N)^{0.1}，但需加上截断误差项 O(1/K^{0.1})。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布定义及积分近似推导符合数学原理，量级与误差项分析自洽。
