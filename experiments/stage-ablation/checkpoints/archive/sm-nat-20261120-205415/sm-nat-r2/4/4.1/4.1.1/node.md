# N56: H_base 的解析推导路径：首先计算缓存容量 C=128GB 在 Pareto(α=1.1) 大小分布下能容纳的对象数量 K，即 K = ∫_0^C s f_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

H_base 的解析推导路径：首先计算缓存容量 C=128GB 在 Pareto(α=1.1) 大小分布下能容纳的对象数量 K，即 K = ∫_0^C s f_S(s) ds 的反函数或数值解，K 决定了缓存覆盖的头部对象比例

## Corrected Claim

H_base 的解析推导路径：首先计算缓存容量 C=128GB 在 Pareto(α=1.1) 大小分布下能容纳的对象数量 K，即 K = ∫_0^C s f_S(s) ds 的反函数或数值解，K 决定了缓存覆盖的头部对象比例

## Evidence

先验知识/题面给定，逻辑校验通过
