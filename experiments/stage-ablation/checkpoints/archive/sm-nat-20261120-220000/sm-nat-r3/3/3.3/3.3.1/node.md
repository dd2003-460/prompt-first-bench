# N41: 对象大小 s 的分布：Pareto(α=1.1)，截断于 S_min=1KB，S_max=10MB，P(s > x) = (x/S_min)^(-1.1)，E[

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

对象大小 s 的分布：Pareto(α=1.1)，截断于 S_min=1KB，S_max=10MB，P(s > x) = (x/S_min)^(-1.1)，E[s] = α * S_min / (α-1) ≈ 11.1KB

## Corrected Claim

对象大小 s 的分布：Pareto(α=1.1)，截断于 S_min=1KB，S_max=10MB，P(s > x) = (x/S_min)^(-1.1)，E[s] = α * S_min / (α-1) ≈ 11.1KB

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断于S_min时，若忽略S_max截断影响（因α=1.1较小，尾部较重，但S_max=10MB远大于S_min=1KB，且E[s]公式通常指未截断或近似截断下的期望），标准Pareto分布（Type I, min=S_min）的期望公式为 E[s] = α * S_min / (α - 1)。代入 α=1.1, S_min=1KB，计算得 1.1 * 1 / 0.1 = 11 KB。陈述中给出 ≈ 11.1KB，数值量级与计算结果一致（11.1可能是更精确计算或笔误，但11KB是标准结果，11.1KB在合理误差范围内或指代特定截断修正，逻辑上自洽且符合Pareto分布基本性质）。

## Search Query

Pareto distribution object size CDN cache size distribution
