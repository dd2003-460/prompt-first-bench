# N18: 根据Holland衰减模型，风速衰减速率 dV/dt 与当前风速 V 成正比（dV/dt = -k * V），其中衰减系数 k 随初始强度增加而减小，导致高风速

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

根据Holland衰减模型，风速衰减速率 dV/dt 与当前风速 V 成正比（dV/dt = -k * V），其中衰减系数 k 随初始强度增加而减小，导致高风速气旋的相对衰减百分比（%/h）低于低风速气旋。

## Corrected Claim

根据Holland衰减模型，风速衰减速率 dV/dt 与当前风速 V 成正比（dV/dt = -k * V），其中衰减系数 k 随初始强度增加而减小，导致高风速气旋的相对衰减百分比（%/h）低于低风速气旋。

## Evidence

先验知识/题面给定，逻辑校验通过：Holland衰减模型基于指数衰减原理（dV/dt = -kV），其相对衰减速率即为常数k，若k随初始强度增加而减小，则高风速气旋的相对衰减百分比必然低于低风速气旋，逻辑自洽且符合气象学常识。
