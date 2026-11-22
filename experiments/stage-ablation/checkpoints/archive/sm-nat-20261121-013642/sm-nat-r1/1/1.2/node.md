# N7: 请求热度分布归一化：Pareto(β=0.9) 的累积分布函数 F(r) = 1 - (r_min/r)^β，需定义最小请求率 r_min 或归一化使得总请求率

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

请求热度分布归一化：Pareto(β=0.9) 的累积分布函数 F(r) = 1 - (r_min/r)^β，需定义最小请求率 r_min 或归一化使得总请求率 Σr_i = 50,000,000/天，从而确定第 k 热对象的请求频率 r_k。

## Corrected Claim

请求热度分布归一化：Pareto(β=0.9) 的累积分布函数 F(r) = 1 - (r_min/r)^β，需定义最小请求率 r_min 或归一化使得总请求率 Σr_i = 50,000,000/天，从而确定第 k 热对象的请求频率 r_k。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式正确，归一化条件定义清晰，量纲与逻辑自洽。
