# N57: 在 u=0.01 基准场景下，整体加权折损系数 δ 的计算需对热度分布加权：δ_weighted = ∫ (1 - u * (T_res(r)/L_object

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

在 u=0.01 基准场景下，整体加权折损系数 δ 的计算需对热度分布加权：δ_weighted = ∫ (1 - u * (T_res(r)/L_object)) f_R(r) dr，其中 T_res(r) 是热度为 r 的对象在 LRU 下的平均驻留时间

## Corrected Claim

在 u=0.01 基准场景下，整体加权折损系数 δ 的计算需对热度分布加权：δ_weighted = ∫ (1 - u * (T_res(r)/L_object)) f_R(r) dr，其中 T_res(r) 是热度为 r 的对象在 LRU 下的平均驻留时间

## Evidence

先验知识/题面给定，逻辑校验通过
