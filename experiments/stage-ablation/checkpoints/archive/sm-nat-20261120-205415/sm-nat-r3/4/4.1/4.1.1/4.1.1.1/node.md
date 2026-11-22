# N155: Pareto(α=1.1) 分布下，对象大小 s 的累积分布函数为 F_S(s) = 1 - (x_min/s)^0.1，其中 x_min 设定为 1MB（最小

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Pareto(α=1.1) 分布下，对象大小 s 的累积分布函数为 F_S(s) = 1 - (x_min/s)^0.1，其中 x_min 设定为 1MB（最小对象大小约束），用于确定单对象大小概率。

## Corrected Claim

Pareto(α=1.1) 分布下，对象大小 s 的累积分布函数为 F_S(s) = 1 - (x_min/s)^0.1，其中 x_min 设定为 1MB（最小对象大小约束），用于确定单对象大小概率。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的标准CDF公式为 F(x) = 1 - (x_min/x)^α，代入 α=1.1 即得 1 - (x_min/s)^0.1，数学推导自洽。
