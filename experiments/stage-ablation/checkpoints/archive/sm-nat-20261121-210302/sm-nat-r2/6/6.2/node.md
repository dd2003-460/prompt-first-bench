# N73: LRU 稳态字节命中率下界公式 H = 1 - ∫[0, C] P(stack distance > c) dc 中，积分上限 C 需转换为对象数量 N_cap

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

LRU 稳态字节命中率下界公式 H = 1 - ∫[0, C] P(stack distance > c) dc 中，积分上限 C 需转换为对象数量 N_cap，转换因子为 1/S_mean，其中 S_mean 为缓存内对象的平均大小。

## Corrected Claim

LRU 稳态字节命中率下界公式 H = 1 - ∫[0, C] P(stack distance > c) dc 中，积分上限 C 需转换为对象数量 N_cap，转换因子为 1/S_mean，其中 S_mean 为缓存内对象的平均大小。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 稳态命中率公式中，积分变量若为字节容量 C，则需除以平均对象大小 S_mean 转换为对象数量 N_cap 以匹配堆距离（以对象数计）的分布函数，量纲与逻辑自洽。

## Search Query

LRU hit rate stack distance integral capacity conversion
