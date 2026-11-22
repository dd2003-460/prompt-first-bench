# N274: 似然比检验的边界条件：当样本量 n < 30 时，LR 统计量不服从卡方分布，p 值计算失效；此时需改用 Bootstrap 方法估计 p 值，置信度修正幅度应

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N84, N85, N86

## Claim

似然比检验的边界条件：当样本量 n < 30 时，LR 统计量不服从卡方分布，p 值计算失效；此时需改用 Bootstrap 方法估计 p 值，置信度修正幅度应额外乘以折扣因子 0.8。

## Corrected Claim

当样本量较小时（如 n < 30），似然比统计量可能不服从渐近卡方分布，导致基于卡方分布的 p 值不准确；此时建议改用精确检验、参数 Bootstrap 或非参数 Bootstrap 方法估计 p 值，而非简单应用固定的折扣因子。

## Evidence

[质询]陈述中关于“置信度修正幅度应额外乘以折扣因子 0.8”的说法缺乏统计学理论依据，属于无中生有的经验规则或错误表述；此外，n<30 并非 LR 统计量服从卡方分布的绝对硬性边界，大样本渐近性质在 n 较小时可能近似成立，具体取决于模型和数据分布，而非简单的 n<30 阈值。 | 逻辑校验发现内部矛盾：似然比检验的 p 值计算失效时，通常改用精确检验或 Bootstrap，但“置信度修正幅度乘以 0.8”这一具体操作在标准统计推断中不存在，违背基本统计原理。

## Search Query

likelihood ratio test small sample bootstrap correction chi-square invalid
