# N115: Pareto(β=0.9) 分布的期望 E[R] 在 β < 1 时发散（∞），因此 N31 中使用的 E[R] 无定义，不能通过归一化条件 ∫ r f(r) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

Pareto(β=0.9) 分布的期望 E[R] 在 β < 1 时发散（∞），因此 N31 中使用的 E[R] 无定义，不能通过归一化条件 ∫ r f(r) dr = Total_R 直接求解 r_min，因为该积分本身发散。

## Corrected Claim

Pareto(β=0.9) 分布的期望 E[R] 在 β < 1 时发散（∞），因此 N31 中使用的 E[R] 无定义，不能通过归一化条件 ∫ r f(r) dr = Total_R 直接求解 r_min，因为该积分本身发散。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的期望公式为 E[R] = αβ/(α-1)，当 α=β=0.9 < 1 时，分母为负且积分 ∫ r f(r) dr 在无穷远处发散，数学上期望值确实不存在（发散至无穷），因此无法通过归一化条件求解。
