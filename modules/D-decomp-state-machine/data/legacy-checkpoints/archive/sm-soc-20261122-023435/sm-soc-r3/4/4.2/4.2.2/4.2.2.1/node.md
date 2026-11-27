# N165: 最优降价触发时间 t* 的一阶条件（FOC）推导：对 t* = argmin_t [C_delay(t) + C_w(t) - E[Margin|t]] 求导并

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

最优降价触发时间 t* 的一阶条件（FOC）推导：对 t* = argmin_t [C_delay(t) + C_w(t) - E[Margin|t]] 求导并令导数为零，得到 C_delay'(t*) + C_w'(t*) = E[Margin]'(t*)，其中 E[Margin]'(t*) 为负值，表示边际收益随时间递减。

## Corrected Claim

最优降价触发时间 t* 的一阶条件（FOC）推导：对 t* = argmin_t [C_delay(t) + C_w(t) - E[Margin|t]] 求导并令导数为零，得到 C_delay'(t*) + C_w'(t*) = E[Margin]'(t*)，其中 E[Margin]'(t*) 为负值，表示边际收益随时间递减。

## Evidence

先验知识/题面给定，逻辑校验通过：对目标函数求导并令其为零的数学推导过程正确，符号逻辑自洽。
