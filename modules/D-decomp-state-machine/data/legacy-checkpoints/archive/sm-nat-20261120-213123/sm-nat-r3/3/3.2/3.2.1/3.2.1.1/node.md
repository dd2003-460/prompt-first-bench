# N107: Pareto(β=0.9) 分布的均值 E[H] 解析解为 β*h_min/(β-1) = 9*h_min，其中 h_min 为归一化最小热度；若按总请求数 R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Pareto(β=0.9) 分布的均值 E[H] 解析解为 β*h_min/(β-1) = 9*h_min，其中 h_min 为归一化最小热度；若按总请求数 R=5×10^7 归一化，h_min = R / Σ(1/h_i^β) 需通过数值积分或近似求和确定，以完成 CV_H 的绝对值标定。

## Corrected Claim

Pareto(β=0.9) 分布的均值 E[H] 解析解为 β*h_min/(β-1) = 9*h_min，其中 h_min 为归一化最小热度；若按总请求数 R=5×10^7 归一化，h_min = R / Σ(1/h_i^β) 需通过数值积分或近似求和确定，以完成 CV_H 的绝对值标定。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布均值公式正确，归一化逻辑自洽

## Search Query

normalization of Pareto distribution mean for request frequency
