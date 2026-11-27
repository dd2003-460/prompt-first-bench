# N65: ρ=-0.3耦合修正项：缓存优先容纳的小对象在字节命中率计算中的权重调整因子w = 1 + ρ·(log(k/N))/log(N)，当ρ=-0.3且k/N=0.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

ρ=-0.3耦合修正项：缓存优先容纳的小对象在字节命中率计算中的权重调整因子w = 1 + ρ·(log(k/N))/log(N)，当ρ=-0.3且k/N=0.1时，w = 1 - 0.3·(log(0.1)/log(10^5)) ≈ 1 - 0.3·(-2.303/11.51) ≈ 1.06，即小对象的字节权重需上调6%以反映热度-大小负相关。

## Corrected Claim

在特定缓存热度-大小负相关模型中，若设定耦合修正系数ρ=-0.3，则当k/N=0.1时，小对象的字节权重调整因子w计算约为1.06。

## Evidence

[质询]该公式属于特定模型假设下的经验性修正项，并非通用物理或数学定律，缺乏通用标准支持，且具体系数ρ=-0.3的选取依据不明。 | 经验事实/模型参数，逻辑自洽但缺来源支持

## Search Query

Pareto size popularity correlation negative rho CDN cache byte hit rate adjustment
