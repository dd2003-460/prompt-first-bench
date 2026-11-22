# N181: 挂价偏差均值检验的统计量计算：基于共享随机源，构造 t 统计量 t_δ = (μ_δ_sample - 0.20) / (σ_δ / √n)，其中 n 为样本量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N60

## Claim

挂价偏差均值检验的统计量计算：基于共享随机源，构造 t 统计量 t_δ = (μ_δ_sample - 0.20) / (σ_δ / √n)，其中 n 为样本量。若 |t_δ| > t_{0.025, n-1}，则拒绝 μ_δ=0.20 的原假设。需具体计算在 n=100, 300, 1000 时的临界值及功效。

## Corrected Claim

挂价偏差均值检验的统计量计算：基于共享随机源，构造 t 统计量 t_δ = (μ_δ_sample - 0.20) / (σ_δ / √n)，其中 n 为样本量。若 |t_δ| > t_{0.025, n-1}，则拒绝 μ_δ=0.20 的原假设。需具体计算在 n=100, 300, 1000 时的临界值及功效。

## Evidence

先验知识/题面给定，逻辑校验通过：t统计量构造及假设检验逻辑符合统计学第一性原理，量纲与公式自洽。

## Search Query

t-test critical values sample size 100 300 1000
