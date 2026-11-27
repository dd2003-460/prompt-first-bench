# N83: 耦合系数 k 的矩匹配定义：k = (C_eff/C - 1) / |ρ|，其中 C_eff 通过模拟 LRU 缓存驻留对象的总字节数除以平均驻留对象大小得到，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

耦合系数 k 的矩匹配定义：k = (C_eff/C - 1) / |ρ|，其中 C_eff 通过模拟 LRU 缓存驻留对象的总字节数除以平均驻留对象大小得到，k 值依赖于分布形态和 ρ 的具体值。

## Corrected Claim

耦合系数 k 的矩匹配定义：k = (C_eff/C - 1) / |ρ|，其中 C_eff 通过模拟 LRU 缓存驻留对象的总字节数除以平均驻留对象大小得到，k 值依赖于分布形态和 ρ 的具体值。

## Evidence

先验知识/题面给定，逻辑校验通过
