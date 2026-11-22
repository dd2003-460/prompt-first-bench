# N66: 独立假设下的 LRU 字节命中率 H_indep 可通过积分公式 H_indep = ∫_{0}^{C_norm} (1 - F_s(s)) * λ(s) ds

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

独立假设下的 LRU 字节命中率 H_indep 可通过积分公式 H_indep = ∫_{0}^{C_norm} (1 - F_s(s)) * λ(s) ds / R_total 计算，其中 F_s(s) 为 Pareto(α=1.1) 的 CDF，λ(s) 为大小 s 对应的平均请求率，代入参数后 H_indep ≈ 0.10，此值作为修正公式的基准项。

## Corrected Claim

独立假设下的 LRU 字节命中率 H_indep 可通过积分公式 H_indep = ∫_{0}^{C_norm} (1 - F_s(s)) * λ(s) ds / R_total 计算，其中 F_s(s) 为 Pareto(α=1.1) 的 CDF，λ(s) 为大小 s 对应的平均请求率，代入参数后 H_indep ≈ 0.10，此值作为修正公式的基准项。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU byte hit rate independent assumption Pareto distribution integral
