# N259: 对照组（Control）的高溢价幅度基线 ΔP_high_old 的置信区间：基于近30天全量数据计算，若样本量 n_control < 1000，则需使用 t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

对照组（Control）的高溢价幅度基线 ΔP_high_old 的置信区间：基于近30天全量数据计算，若样本量 n_control < 1000，则需使用 t 分布而非正态分布计算 95% CI，公式为 μ_old ± t_{0.975, n-1} * (σ_old/√n)。

## Corrected Claim

对照组（Control）的高溢价幅度基线 ΔP_high_old 的置信区间：基于近30天全量数据计算，若样本量 n_control < 1000，则需使用 t 分布而非正态分布计算 95% CI，公式为 μ_old ± t_{0.975, n-1} * (σ_old/√n)。

## Evidence

先验知识/题面给定，逻辑校验通过：当样本量 n < 30（或通常认为 n < 1000 且总体方差未知时）且总体服从正态分布或近似正态时，使用 t 分布计算置信区间是统计学标准做法；公式 μ ± t * (s/√n) 量纲正确，逻辑自洽。

## Search Query

confidence interval calculation for small sample price data t-distribution vs normal
