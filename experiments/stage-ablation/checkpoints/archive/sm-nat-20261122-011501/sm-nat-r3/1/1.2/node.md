# N7: 请求热度分布的累积分布函数 CDF_H(h) = 1 - (h/h_max)^(-0.9)，其中 h 为相对热度（归一化请求率），用于确定 Top-K 热点对象

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

请求热度分布的累积分布函数 CDF_H(h) = 1 - (h/h_max)^(-0.9)，其中 h 为相对热度（归一化请求率），用于确定 Top-K 热点对象覆盖的总请求比例。

## Corrected Claim

请求热度分布的累积分布函数 CDF_H(h) = 1 - (h/h_max)^(-0.9)，其中 h 为相对热度（归一化请求率），用于确定 Top-K 热点对象覆盖的总请求比例。

## Evidence

先验知识/题面给定，逻辑校验通过
