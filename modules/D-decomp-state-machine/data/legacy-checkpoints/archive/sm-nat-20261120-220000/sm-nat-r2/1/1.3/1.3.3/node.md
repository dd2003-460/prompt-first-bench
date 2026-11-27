# N26: Pareto(β=0.9) 的热度变异系数 CV_freq = sqrt((β-1)/(β-3)) 在 β<3 时同样发散，需数值积分计算：CV_freq = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Pareto(β=0.9) 的热度变异系数 CV_freq = sqrt((β-1)/(β-3)) 在 β<3 时同样发散，需数值积分计算：CV_freq = sqrt(∫ f^2 g(f) df / (∫ f g(f) df)^2 - 1)，对于 β=0.9，CV_freq 极大，表明热度分布极度倾斜，少数热门对象主导请求量。

## Corrected Claim

Pareto(β=0.9) 的热度变异系数 CV_freq = sqrt((β-1)/(β-3)) 在 β<3 时同样发散，需数值积分计算：CV_freq = sqrt(∫ f^2 g(f) df / (∫ f g(f) df)^2 - 1)，对于 β=0.9，CV_freq 极大，表明热度分布极度倾斜，少数热门对象主导请求量。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布（指数β）的矩存在条件为 k < β。当 β=0.9 时，二阶矩（k=2）不存在，导致方差和变异系数在解析上发散（无穷大），陈述中关于发散及需数值积分（截断）的描述符合数学原理。
