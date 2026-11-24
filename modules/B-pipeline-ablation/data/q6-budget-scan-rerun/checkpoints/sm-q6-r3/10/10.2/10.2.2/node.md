# N403: 单位成本公式的边界条件校验：Cost_per_1k_req = Total_Annual_Cost / (Total_Annual_Requests / 100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

单位成本公式的边界条件校验：Cost_per_1k_req = Total_Annual_Cost / (Total_Annual_Requests / 1000) 假设成本与请求量线性相关，但实际 CDN 成本包含固定成本（如自建基础设施折旧）和可变成本（带宽按量计费）；当请求量变化 ±20% 时，固定成本占比变化导致单位成本非线性变化，需计算成本弹性系数 E = ΔC% / ΔR%，若 E > 1 则规模效应显著，分母修正对高请求量策略影响更大。

## Corrected Claim

单位成本公式的边界条件校验：Cost_per_1k_req = Total_Annual_Cost / (Total_Annual_Requests / 1000) 假设成本与请求量线性相关，但实际 CDN 成本包含固定成本（如自建基础设施折旧）和可变成本（带宽按量计费）；当请求量变化 ±20% 时，固定成本占比变化导致单位成本非线性变化，需计算成本弹性系数 E = ΔC% / ΔR%，若 E > 1 则规模效应显著，分母修正对高请求量策略影响更大。

## Evidence

先验知识/题面给定，逻辑校验通过：成本结构分解（固定+可变）及弹性系数定义符合经济学基本原理，量纲与逻辑自洽。
