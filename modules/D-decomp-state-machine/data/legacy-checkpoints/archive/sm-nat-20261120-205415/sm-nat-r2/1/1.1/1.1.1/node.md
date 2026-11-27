# N28: Pareto(α=1.1) 分布在截断点 B 处的累积分布函数 (CDF) 表达式为 F(B) = 1 - (x_min/B)^{α-1}，其中 x_min 为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

Pareto(α=1.1) 分布在截断点 B 处的累积分布函数 (CDF) 表达式为 F(B) = 1 - (x_min/B)^{α-1}，其中 x_min 为最小对象大小（题面未给，需设为 1KB 或 1B 以进行数值计算）

## Corrected Claim

Pareto(α=1.1) 分布在截断点 B 处的累积分布函数 (CDF) 表达式为 F(B) = 1 - (x_min/B)^{α-1}，其中 x_min 为最小对象大小（题面未给，需设为 1KB 或 1B 以进行数值计算）

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的标准CDF公式为 F(x) = 1 - (x_min/x)^{α-1}，代入截断点B即得 F(B) = 1 - (x_min/B)^{α-1}，公式推导正确且量纲一致。
