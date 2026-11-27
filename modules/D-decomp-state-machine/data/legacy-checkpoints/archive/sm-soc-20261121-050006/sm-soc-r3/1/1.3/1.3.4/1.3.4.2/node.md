# N149: P_threshold 与 σ_pref 的边界条件交互：当市场波动率 σ_pref > 0.25 * P_median 时，P_threshold 失效，因为

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

P_threshold 与 σ_pref 的边界条件交互：当市场波动率 σ_pref > 0.25 * P_median 时，P_threshold 失效，因为重尾分布的右尾延伸至无穷，理论上不存在绝对上限，此时 T_close 的分布呈现幂律尾部而非指数衰减，需改用 Pareto 分布拟合 T_close 而非正态分布

## Corrected Claim

当市场波动率显著升高导致收益分布呈现重尾特征时，基于正态分布假设的P_threshold可能不再适用，此时T_close的分布可能呈现幂律尾部，需考虑使用Pareto等重尾分布进行拟合。

## Evidence

[质询]该陈述将特定的经验性阈值（0.25 * P_median）和分布形态转换（正态转Pareto）作为绝对真理，缺乏普适的理论推导支持。在金融数学中，波动率与分布尾部的关系并非简单的线性阈值触发，且'P_threshold失效'的定义模糊，属于过度简化的经验规则而非第一性原理可推导的数学事实。 | source=knowledge，逻辑上重尾分布确实无绝对上限且需非正态拟合，但具体阈值0.25及'失效'机制属于特定模型假设或经验参数，非普适真理，故降级为定性表述。

## Search Query

heavy-tailed distribution transaction time threshold invalidity high volatility market
