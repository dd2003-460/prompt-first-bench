# N6: 对象大小分布的截断阈值 S_max 计算：求解 Pareto(α=1.1) 在 128GB 容量约束下的最大可缓存对象大小，公式 S_max = (128 * 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

对象大小分布的截断阈值 S_max 计算：求解 Pareto(α=1.1) 在 128GB 容量约束下的最大可缓存对象大小，公式 S_max = (128 * 10^9 bytes) / (100,000 * (S_min)^(α-1) * (1 - (S_min/S_max)^(α-1))) 的迭代解，其中 S_min 为最小对象大小 [待核验]，通常设为 1KB。

## Corrected Claim

对象大小分布的截断阈值 S_max 计算：求解 Pareto(α=1.1) 在 128GB 容量约束下的最大可缓存对象大小，通常通过积分 ∫_{S_min}^{S_max} x * f(x) dx = 128GB 来迭代求解 S_max，其中 S_min 为最小对象大小，通常设为 1KB。

## Evidence

[质询]公式中的分母项 (1 - (S_min/S_max)^(α-1)) 在 S_max 远大于 S_min 时趋近于 1，导致 S_max 近似为常数，这与 Pareto 分布尾部无界、需通过截断阈值控制总容量的直觉不符；通常截断阈值是通过积分求总容量等于约束值来解 S_max，而非这种代数形式。 | 经验事实，逻辑自洽但缺来源支持
