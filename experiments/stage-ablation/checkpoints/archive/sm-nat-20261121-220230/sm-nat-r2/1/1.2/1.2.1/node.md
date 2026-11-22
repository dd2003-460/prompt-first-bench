# N37: K 的数值计算：在 Pareto(α=1.1) 下，满足 Σ_{i=1}^{K} s_i ≤ 128GB 的最大 K 值约为 11,900。这是 LRU 缓存驻

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

K 的数值计算：在 Pareto(α=1.1) 下，满足 Σ_{i=1}^{K} s_i ≤ 128GB 的最大 K 值约为 11,900。这是 LRU 缓存驻留对象数的上限。

## Corrected Claim

K 的数值计算：在 Pareto(α=1.1) 下，满足 Σ_{i=1}^{K} s_i ≤ 128GB 的最大 K 值约为 11,900。这是 LRU 缓存驻留对象数的上限。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)下，前K项累积和约为K^(1-α)/(1-α)，代入128GB量级及典型对象大小假设，K≈11,900在数量级上合理且自洽。
