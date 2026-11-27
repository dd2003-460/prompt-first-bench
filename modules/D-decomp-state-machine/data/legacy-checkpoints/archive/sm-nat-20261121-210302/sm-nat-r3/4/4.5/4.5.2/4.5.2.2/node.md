# N164: 在 ρ=-0.3 实际耦合下，S_avg_hot = E[S | P > F_th] 显著小于 E[S]，需通过 Clayton Copula 联合分布积分计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N54

## Claim

在 ρ=-0.3 实际耦合下，S_avg_hot = E[S | P > F_th] 显著小于 E[S]，需通过 Clayton Copula 联合分布积分计算，量化'热门即小'导致的缓存空间效率增益，该值直接决定 LFU 相比 LRU 的字节命中率提升上限。

## Corrected Claim

在 ρ=-0.3 实际耦合下，S_avg_hot = E[S | P > F_th] 显著小于 E[S]，需通过 Clayton Copula 联合分布积分计算，量化'热门即小'导致的缓存空间效率增益，该值直接决定 LFU 相比 LRU 的字节命中率提升上限。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关（ρ=-0.3）意味着高流行度（P）对应低大小（S），条件期望 E[S|P>F_th] 必然小于无条件期望 E[S]，Copula 积分是处理非高斯依赖关系的正确数学工具，逻辑自洽。
