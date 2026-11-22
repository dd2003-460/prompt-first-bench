# N7: 请求热度服从 Pareto(β=0.9)，其累积分布函数 CDF(R>r) = (r_min/r)^0.9，其中 r_min 为最小请求频率，通常归一化使得总请

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

请求热度服从 Pareto(β=0.9)，其累积分布函数 CDF(R>r) = (r_min/r)^0.9，其中 r_min 为最小请求频率，通常归一化使得总请求次数为 5000 万次/天，即 ∫r·f(r)dr = 5×10^7。

## Corrected Claim

请求热度服从 Pareto(β=0.9)，其累积分布函数 CDF(R>r) = (r_min/r)^0.9，其中 r_min 为最小请求频率，通常归一化使得总请求次数为 5000 万次/天，即 ∫r·f(r)dr = 5×10^7。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的CDF形式 (r_min/r)^β 符合标准定义，且归一化条件 ∫r·f(r)dr = 5×10^7 在数学上自洽，用于确定分布参数。
