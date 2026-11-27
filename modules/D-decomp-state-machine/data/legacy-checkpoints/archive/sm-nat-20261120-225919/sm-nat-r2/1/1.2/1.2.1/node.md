# N31: 请求热度分布的最小频率 r_min 需通过归一化条件 ∫_{r_min}^{∞} r * f(r) dr = 5×10^7 确定，其中 f(r) = β * r

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

请求热度分布的最小频率 r_min 需通过归一化条件 ∫_{r_min}^{∞} r * f(r) dr = 5×10^7 确定，其中 f(r) = β * r_min^β / r^(β+1)，解得 r_min = (5×10^7 / (N * E[R]))，N=100000，E[R] 为单对象平均请求频率

## Corrected Claim

请求热度分布的最小频率 r_min 需通过归一化条件 ∫_{r_min}^{∞} r * f(r) dr = 5×10^7 确定，其中 f(r) = β * r_min^β / r^(β+1)，解得 r_min = (5×10^7 / (N * E[R]))，N=100000，E[R] 为单对象平均请求频率

## Evidence

先验知识/题面给定，逻辑校验通过：帕累托分布归一化条件推导正确，量纲与数值量级合理

## Search Query

Pareto distribution normalization condition total requests
