# N95: Z_rank 在 Copula 模型中的有效性边界：Z_rank 假设排名服从均匀分布，但在 Pareto 热度分布下，排名与频率呈幂律关系。直接使用均匀分布的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Z_rank 在 Copula 模型中的有效性边界：Z_rank 假设排名服从均匀分布，但在 Pareto 热度分布下，排名与频率呈幂律关系。直接使用均匀分布的 Z_rank 会低估头部对象的相关性强度。需引入变换 Z_rank_transformed = Φ^{-1}(F_rank(k))，其中 F_rank 为排名分布的 CDF，以校正非线性相关结构。

## Corrected Claim

Z_rank 在 Copula 模型中的有效性边界：Z_rank 假设排名服从均匀分布，但在 Pareto 热度分布下，排名与频率呈幂律关系。直接使用均匀分布的 Z_rank 会低估头部对象的相关性强度。需引入变换 Z_rank_transformed = Φ^{-1}(F_rank(k))，其中 F_rank 为排名分布的 CDF，以校正非线性相关结构。

## Evidence

先验知识/题面给定，逻辑校验通过：Z-score 标准化隐含均匀分布假设，在幂律分布下直接使用会导致尾部相关性估计偏差，引入基于经验 CDF 的变换（如 Rank-based Copula 或 Gaussian Copula 的逆 CDF 变换）是统计学中校正非线性相关结构的标准方法，逻辑自洽且符合统计原理。
