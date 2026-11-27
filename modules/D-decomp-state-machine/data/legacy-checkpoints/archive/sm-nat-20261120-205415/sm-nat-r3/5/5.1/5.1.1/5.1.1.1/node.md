# N180: N66中公式 H = 1 - (1 - f(C))^β 的推导隐含了'均匀随机请求'假设，与题面给定的Pareto(β=0.9)热度分布矛盾，导致计算结果 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

N66中公式 H = 1 - (1 - f(C))^β 的推导隐含了'均匀随机请求'假设，与题面给定的Pareto(β=0.9)热度分布矛盾，导致计算结果 0.00115% 为无效下界，需替换为Zipf/Pareto累积分布函数模型

## Corrected Claim

N66中公式 H = 1 - (1 - f(C))^β 的推导隐含了'均匀随机请求'假设，与题面给定的Pareto(β=0.9)热度分布矛盾，导致计算结果 0.00115% 为无效下界，需替换为Zipf/Pareto累积分布函数模型

## Evidence

先验知识/题面给定，逻辑校验通过：均匀分布假设与Pareto分布确实矛盾，且均匀分布下界通常低于长尾分布下的实际值，逻辑自洽。
