# N46: Pareto(α=1.1)分布下，大小小于阈值 S_th 的对象所占总字节数的比例公式为 R_byte(S_th) = 1 - (x_min/S_th)^(α-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

Pareto(α=1.1)分布下，大小小于阈值 S_th 的对象所占总字节数的比例公式为 R_byte(S_th) = 1 - (x_min/S_th)^(α-1)，当 S_th 对应缓存能容纳的最大对象大小时，该值即为 LRU 理论上能覆盖的字节命中率上界。

## Corrected Claim

Pareto(α=1.1)分布下，大小小于阈值 S_th 的对象所占总字节数的比例公式为 R_byte(S_th) = 1 - (x_min/S_th)^(α-1)，当 S_th 对应缓存能容纳的最大对象大小时，该值即为 LRU 理论上能覆盖的字节命中率上界。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的累积分布函数推导正确，LRU字节命中率上界定义符合缓存理论第一性原理
