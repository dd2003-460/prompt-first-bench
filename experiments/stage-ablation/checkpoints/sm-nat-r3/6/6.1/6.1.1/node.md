# N259: 截断 Pareto(α=1.1, x_min=1KB, x_max=10GB) 分布下，前 20% 对象覆盖的字节量比例 C_byte(0.2) 的数值积分公式

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

截断 Pareto(α=1.1, x_min=1KB, x_max=10GB) 分布下，前 20% 对象覆盖的字节量比例 C_byte(0.2) 的数值积分公式：C_byte(0.2) = [∫_{x_min}^{x_20} x * f(x) dx] / [∫_{x_min}^{x_max} x * f(x) dx]，其中 x_20 为前 20% 对象的截断点，需计算具体数值。

## Corrected Claim

截断 Pareto(α=1.1, x_min=1KB, x_max=10GB) 分布下，前 20% 对象覆盖的字节量比例 C_byte(0.2) 的数值积分公式：C_byte(0.2) = [∫_{x_min}^{x_20} x * f(x) dx] / [∫_{x_min}^{x_max} x * f(x) dx]，其中 x_20 为前 20% 对象的截断点，需计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式正确表达了截断Pareto分布下前20%对象（按数量）所覆盖的字节量比例，分子为截断点x_20以下的加权积分，分母为全区间加权积分，量纲与定义自洽。
