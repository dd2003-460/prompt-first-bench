# N28: h_max 的归一化定义：h_max = Total_Requests / N = 50,000,000 / 100,000 = 500 req/day/obj

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

h_max 的归一化定义：h_max = Total_Requests / N = 50,000,000 / 100,000 = 500 req/day/object，用于将相对热度 h 转换为绝对请求率 R_i = h_i * h_max。

## Corrected Claim

h_max 的归一化定义：h_max = Total_Requests / N = 50,000,000 / 100,000 = 500 req/day/object，用于将相对热度 h 转换为绝对请求率 R_i = h_i * h_max。

## Evidence

先验知识/题面给定，逻辑校验通过：50,000,000 / 100,000 = 500，量纲与定义自洽。
