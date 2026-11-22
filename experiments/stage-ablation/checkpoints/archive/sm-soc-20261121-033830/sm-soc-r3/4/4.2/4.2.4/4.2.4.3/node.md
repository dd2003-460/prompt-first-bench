# N231: 候选B的采纳率-效用权衡：平台需最大化期望效用 U_platform = P(Adopt) * (Commission * P_suggest - Servic

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

候选B的采纳率-效用权衡：平台需最大化期望效用 U_platform = P(Adopt) * (Commission * P_suggest - Service_Cost)，其中 Service_Cost 为算法推荐带来的客服/技术支持成本；若 P(Adopt) 随 P_suggest 降低而指数上升，存在最优 P_suggest* 使得 U_platform 最大化，需求解 dU/dP_suggest = 0。

## Corrected Claim

候选B的采纳率-效用权衡：平台需最大化期望效用 U_platform = P(Adopt) * (Commission * P_suggest - Service_Cost)，其中 Service_Cost 为算法推荐带来的客服/技术支持成本；若 P(Adopt) 随 P_suggest 降低而指数上升，存在最优 P_suggest* 使得 U_platform 最大化，需求解 dU/dP_suggest = 0。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了一个标准的经济学/运筹学优化模型。效用函数 U = P(Adopt) * (Revenue - Cost) 结构合理；若 P(Adopt) 随 P_suggest 降低而指数上升（即 P(Adopt) 是 P_suggest 的单调递减凸函数或类似形态），而收益项 (Commission * P_suggest - Service_Cost) 随 P_suggest 线性增加，则乘积函数 U(P_suggest) 在定义域内通常存在内部极大值点，满足一阶条件 dU/dP_suggest = 0 是求解最优解的标准数学方法。逻辑自洽，量纲合理。
