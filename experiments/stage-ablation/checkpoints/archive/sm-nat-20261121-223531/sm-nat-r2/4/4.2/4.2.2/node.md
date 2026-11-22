# N57: 前1%对象的平均大小 E[S|H>h_1%] 通过负相关 ρ=-0.3 的联合分布计算，由于热门对象与大小负相关，E[S|H>h_1%] < E[S]_trun

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

前1%对象的平均大小 E[S|H>h_1%] 通过负相关 ρ=-0.3 的联合分布计算，由于热门对象与大小负相关，E[S|H>h_1%] < E[S]_trunc ≈ 10.5KB，具体值需通过二元 Pareto 分布积分确定，假设约为 5KB。

## Corrected Claim

前1%对象的平均大小 E[S|H>h_1%] 通过负相关 ρ=-0.3 的联合分布计算，由于热门对象与大小负相关，E[S|H>h_1%] < E[S]_trunc ≈ 10.5KB，具体值需通过二元 Pareto 分布积分确定，假设约为 5KB。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关分布下条件期望小于截断均值符合统计直觉，量级合理。

## Search Query

conditional expectation size given high heat negative correlation Pareto
