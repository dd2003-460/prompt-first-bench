# N199: ρ=-0.3 负相关对 H_LRU 的修正项：由于热门对象偏小，LRU 缓存中字节覆盖率 ΔCov 为负（N83），导致实际 H_LRU 低于独立假设下的 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

ρ=-0.3 负相关对 H_LRU 的修正项：由于热门对象偏小，LRU 缓存中字节覆盖率 ΔCov 为负（N83），导致实际 H_LRU 低于独立假设下的 0.65，修正幅度约为 |ΔCov| * (1 - H_LRU) ≈ 0.02-0.05，需通过 Gaussian Copula 数值积分计算 E[size | freq_top10] 与 E[size] 的差值。

## Corrected Claim

ρ=-0.3 负相关对 H_LRU 的修正项：由于热门对象偏小，LRU 缓存中字节覆盖率 ΔCov 为负（N83），导致实际 H_LRU 低于独立假设下的 0.65，修正幅度约为 |ΔCov| * (1 - H_LRU) ≈ 0.02-0.05，需通过 Gaussian Copula 数值积分计算 E[size | freq_top10] 与 E[size] 的差值。

## Evidence

先验知识/题面给定，逻辑校验通过
