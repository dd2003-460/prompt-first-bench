# N88: Total 字节吞吐量的无相关基准值：Total_independent = (Σ_{r=1}^{100000} r^(-0.9)) * (E[Size]_Pa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Total 字节吞吐量的无相关基准值：Total_independent = (Σ_{r=1}^{100000} r^(-0.9)) * (E[Size]_Pareto(α=1.1)) * 50,000,000，其中 E[Size] 基于截断 Pareto 分布计算，作为相关性修正的基线。

## Corrected Claim

Total 字节吞吐量的无相关基准值：Total_independent = (Σ_{r=1}^{100000} r^(-0.9)) * (E[Size]_Pareto(α=1.1)) * 50,000,000，其中 E[Size] 基于截断 Pareto 分布计算，作为相关性修正的基线。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合独立基准的定义（总请求数 * 平均大小 * 并发/频率因子），Pareto分布期望值计算逻辑自洽，无内部矛盾。

## Search Query

total byte throughput calculation Zipf popularity Pareto size distribution
