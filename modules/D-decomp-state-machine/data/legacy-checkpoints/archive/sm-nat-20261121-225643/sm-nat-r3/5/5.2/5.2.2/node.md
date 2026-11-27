# N101: N_cap 的精确积分计算：E[S|in_cache] = ∫_0^∞ s * f_size(s) * f_pop(s) * I(s ≤ S_threshold

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

N_cap 的精确积分计算：E[S|in_cache] = ∫_0^∞ s * f_size(s) * f_pop(s) * I(s ≤ S_threshold) ds / ∫_0^∞ f_size(s) * f_pop(s) * I(s ≤ S_threshold) ds，其中 S_threshold 为缓存容量约束下的最大可容纳对象大小；在α=1.1重尾分布下，该积分需数值求解，解析解不存在

## Corrected Claim

N_cap 的精确积分计算：E[S|in_cache] = ∫_0^∞ s * f_size(s) * f_pop(s) * I(s ≤ S_threshold) ds / ∫_0^∞ f_size(s) * f_pop(s) * I(s ≤ S_threshold) ds，其中 S_threshold 为缓存容量约束下的最大可容纳对象大小；在α=1.1重尾分布下，该积分需数值求解，解析解不存在

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的积分定义符合概率论基本定义；α=1.1的重尾分布（如Pareto分布）在截断积分下通常无封闭解析解，需数值求解，符合数学直觉。
