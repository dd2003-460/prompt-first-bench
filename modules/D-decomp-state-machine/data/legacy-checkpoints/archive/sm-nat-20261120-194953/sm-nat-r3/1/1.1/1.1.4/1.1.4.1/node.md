# N91: 在 Pareto(β=0.9) 分布下，热度 CDF 逆函数 F_R^{-1}(p) 的解析表达式为 x_min * (1-p)^{-1/β}（假设 x_min

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

在 Pareto(β=0.9) 分布下，热度 CDF 逆函数 F_R^{-1}(p) 的解析表达式为 x_min * (1-p)^{-1/β}（假设 x_min=1），用于计算 Z^{-1}(F_R(r)) 中的标准化热度值，需验证该公式在 p→1 时的数值稳定性。

## Corrected Claim

在 Pareto(β=0.9) 分布下，热度 CDF 逆函数 F_R^{-1}(p) 的解析表达式为 x_min * (1-p)^{-1/β}（假设 x_min=1），用于计算 Z^{-1}(F_R(r)) 中的标准化热度值，需验证该公式在 p→1 时的数值稳定性。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF为F(x)=(x_min/x)^β，逆函数推导正确，量纲与极限行为符合数学定义
