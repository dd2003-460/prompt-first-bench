# N222: 当对象大小方差系数 Var(s)/E[s]^2 > 10 时，Mattson 堆栈算法的命中率误差为 O(ρ^2)，在 ρ=-0.3 下修正项量级为 0.09，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75, N76, N77

## Claim

当对象大小方差系数 Var(s)/E[s]^2 > 10 时，Mattson 堆栈算法的命中率误差为 O(ρ^2)，在 ρ=-0.3 下修正项量级为 0.09，导致 LRU 命中率估算偏差达 9%，需引入相关系数修正

## Corrected Claim

当对象大小方差系数较大时，Mattson 堆栈算法的命中率估算可能产生显著偏差，需引入相关系数修正以减小误差。

## Evidence

[质询]该陈述包含具体的经验性阈值（方差系数>10）和特定的误差量级（9%），属于经验事实而非第一性原理可推导的数学恒等式；且缺乏来源支持，无法确认该特定阈值和误差量级的普适性或准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Mattson stack algorithm error heavy-tailed distribution correlation correction
