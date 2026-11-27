# N197: 在 W_LRU >> T_update 工作点下，对象 i 的更新失效概率 P_invalid(i) 的精确积分表达式为 P_invalid(i) = 1 - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

在 W_LRU >> T_update 工作点下，对象 i 的更新失效概率 P_invalid(i) 的精确积分表达式为 P_invalid(i) = 1 - exp(-W_LRU(i) / E[T_update])，其中 E[T_update] = 24h，当 W_LRU(i) = 240h (10 * E[T_update]) 时，P_invalid ≈ 1 - exp(-10) ≈ 99.995%，量化了长驻留对象几乎必然失效的边界条件。

## Corrected Claim

在 W_LRU >> T_update 工作点下，对象 i 的更新失效概率 P_invalid(i) 的精确积分表达式为 P_invalid(i) = 1 - exp(-W_LRU(i) / E[T_update])，其中 E[T_update] = 24h，当 W_LRU(i) = 240h (10 * E[T_update]) 时，P_invalid ≈ 1 - exp(-10) ≈ 99.995%，量化了长驻留对象几乎必然失效的边界条件。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布失效概率公式 P=1-exp(-t/λ) 在 t=10λ 时数值计算正确（1-e^-10≈0.99995），量纲与逻辑自洽。
