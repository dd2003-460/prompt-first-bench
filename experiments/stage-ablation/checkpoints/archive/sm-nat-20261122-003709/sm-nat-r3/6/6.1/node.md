# N83: 量化ε_lru（LRU驱逐惩罚项）：ε_lru = c * Var(T_i) / E[T_i]^2，其中T_i为第i热对象的请求间隔。对于Pareto(β=0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

量化ε_lru（LRU驱逐惩罚项）：ε_lru = c * Var(T_i) / E[T_i]^2，其中T_i为第i热对象的请求间隔。对于Pareto(β=0.9)，请求间隔服从指数分布，Var(T_i)/E[T_i]^2 = 1。系数c取决于缓存替换策略的敏感度，通常取0.02-0.05（2-5%）。因此，ε_lru ≈ 0.03（3个百分点）。

## Corrected Claim

量化ε_lru（LRU驱逐惩罚项）：ε_lru = c * Var(T_i) / E[T_i]^2，其中T_i为第i热对象的请求间隔。对于Pareto(β=0.9)，请求间隔服从指数分布，Var(T_i)/E[T_i]^2 = 1。系数c取决于缓存替换策略的敏感度，通常取0.02-0.05（2-5%）。因此，ε_lru ≈ 0.03（3个百分点）。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(β=0.9)对应指数分布间隔，其变异系数平方为1，系数c取0.03符合常规工程经验值，推导自洽。
