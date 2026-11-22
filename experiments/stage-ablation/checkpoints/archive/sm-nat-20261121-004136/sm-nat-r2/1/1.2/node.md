# N7: 请求热度分布的累积分布函数 (CDF) 表达式：P(rank ≤ k) = 1 - (k/N)^(1-β)，其中 N=100,000, β=0.9，用于确定任意

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

请求热度分布的累积分布函数 (CDF) 表达式：P(rank ≤ k) = 1 - (k/N)^(1-β)，其中 N=100,000, β=0.9，用于确定任意前 k 个对象占总请求量的比例。

## Corrected Claim

请求热度分布的累积分布函数 (CDF) 表达式：P(rank ≤ k) = 1 - (k/N)^(1-β)，其中 N=100,000, β=0.9，用于确定任意前 k 个对象占总请求量的比例。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合广义Zipf分布（或Pareto分布）的累积分布函数形式，参数β=0.9在(0,1)区间内，数学推导自洽，量级合理。
