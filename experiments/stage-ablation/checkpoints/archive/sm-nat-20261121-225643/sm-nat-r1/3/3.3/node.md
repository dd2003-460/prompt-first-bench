# N13: 更新率与缓存时间交互：若T_resident随负载变化，P_stale = u * T_resident，T_resident = M / (R * E[S_h

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

更新率与缓存时间交互：若T_resident随负载变化，P_stale = u * T_resident，T_resident = M / (R * E[S_hit])，其中E[S_hit]为命中对象平均大小，形成非线性耦合，需迭代求解

## Corrected Claim

更新率与缓存时间交互：若T_resident随负载变化，P_stale = u * T_resident，T_resident = M / (R * E[S_hit])，其中E[S_hit]为命中对象平均大小，形成非线性耦合，需迭代求解

## Evidence

先验知识/题面给定，逻辑校验通过
