# N212: 条件概率 P(size > s | freq > f) 的数值积分公式：P(size > s | freq > f) = ∫_s^∞ ∫_f^∞ c_θ(F_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

条件概率 P(size > s | freq > f) 的数值积分公式：P(size > s | freq > f) = ∫_s^∞ ∫_f^∞ c_θ(F_size(x), F_freq(y)) dx dy / P(freq > f)，其中 c_θ 为 Gaussian Copula 密度函数，分母 P(freq > f) = (f_min/f)^β 可通过 Pareto 尾部直接计算。

## Corrected Claim

条件概率 P(size > s | freq > f) 的数值积分公式：P(size > s | freq > f) = ∫_s^∞ ∫_f^∞ c_θ(F_size(x), F_freq(y)) dx dy / P(freq > f)，其中 c_θ 为 Gaussian Copula 密度函数，分母 P(freq > f) = (f_min/f)^β 可通过 Pareto 尾部直接计算。

## Evidence

先验知识/题面给定，逻辑校验通过：条件概率定义正确，Gaussian Copula 联合密度积分形式符合概率论基本定理，Pareto 尾部概率公式 (f_min/f)^β 在 f > f_min 时数学推导成立。
