# N114: 总请求字节速率 R_total_bytes 的计算依赖于请求加权平均大小 E[S|Requested]，在 Pareto(α=1.1) 且截断上限 S_max=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

总请求字节速率 R_total_bytes 的计算依赖于请求加权平均大小 E[S|Requested]，在 Pareto(α=1.1) 且截断上限 S_max=100MB 的假设下，E[S|Requested] 需通过数值积分 ∫_{X_min}^{S_max} s * f(s) ds 计算，该值直接决定 R_evict 的绝对量级。

## Corrected Claim

总请求字节速率 R_total_bytes 的计算依赖于请求加权平均大小 E[S|Requested]，在 Pareto(α=1.1) 且截断上限 S_max=100MB 的假设下，E[S|Requested] 需通过数值积分 ∫_{X_min}^{S_max} s * f(s) ds 计算，该值直接决定 R_evict 的绝对量级。

## Evidence

先验知识/题面给定，逻辑校验通过：总字节速率确实等于请求速率乘以条件期望大小，且截断Pareto分布的期望需通过数值积分计算，逻辑自洽且量纲正确。
