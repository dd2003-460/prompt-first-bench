# N134: Pareto 分布常数项修正：对于连续 Pareto 分布，累积分布函数 F(x) = 1 - (x_min/x)^α。命中率计算涉及 ∫_{x_min}^{x

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Pareto 分布常数项修正：对于连续 Pareto 分布，累积分布函数 F(x) = 1 - (x_min/x)^α。命中率计算涉及 ∫_{x_min}^{x_max} x * f(x) * P(hit|x) dx。与 Zipf 不同，Pareto 的尾部更厚，导致低频大对象对字节命中率的影响更大。修正因子应基于 ∫_{x_min}^{∞} x^(-α) dx 的收敛性（α>1）和字节加权分布 ∫ x * f(x) dx 的收敛性（α>2，此处不满足）来确定。

## Corrected Claim

Pareto 分布常数项修正：对于连续 Pareto 分布，累积分布函数 F(x) = 1 - (x_min/x)^α。命中率计算涉及 ∫_{x_min}^{x_max} x * f(x) * P(hit|x) dx。与 Zipf 不同，Pareto 的尾部更厚，导致低频大对象对字节命中率的影响更大。修正因子应基于 ∫_{x_min}^{∞} x^(-α) dx 的收敛性（α>1）和字节加权分布 ∫ x * f(x) dx 的收敛性（α>2，此处不满足）来确定。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式正确，积分收敛性条件（α>1, α>2）符合数学定义，尾部特性描述准确。
