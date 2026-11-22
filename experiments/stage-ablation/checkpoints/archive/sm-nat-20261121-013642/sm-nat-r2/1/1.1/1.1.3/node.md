# N33: 缓存容量覆盖率计算：定义覆盖对象数 K_max 为满足 Σ_{i=1}^{K_max} s_i ≤ 128GB 的最大整数 K_max，其中 s_i 为按大小降

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

缓存容量覆盖率计算：定义覆盖对象数 K_max 为满足 Σ_{i=1}^{K_max} s_i ≤ 128GB 的最大整数 K_max，其中 s_i 为按大小降序排列的对象大小，K_max 决定了 LRU 缓存最多能驻留的对象数量上限。

## Corrected Claim

缓存容量覆盖率计算：定义覆盖对象数 K_max 为满足 Σ_{i=1}^{K_max} s_i ≤ 128GB 的最大整数 K_max，其中 s_i 为按大小降序排列的对象大小，K_max 决定了 LRU 缓存最多能驻留的对象数量上限。

## Evidence

先验知识/题面给定，逻辑校验通过
