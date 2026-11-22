# N190: 计算头部K个对象（Top K）的热度阈值 h_min = p_K，基于 Pareto(β=0.9) 分布，h_min = C_β * K^{-0.9}，该阈值定

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

计算头部K个对象（Top K）的热度阈值 h_min = p_K，基于 Pareto(β=0.9) 分布，h_min = C_β * K^{-0.9}，该阈值定义了条件期望 E[S|Top K] 的积分下界。

## Corrected Claim

计算头部K个对象（Top K）的热度阈值 h_min = p_K，基于 Pareto(β=0.9) 分布，h_min = C_β * K^{-0.9}，该阈值定义了条件期望 E[S|Top K] 的积分下界。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的CDF逆函数（分位数函数）形式为 $x_p = C p^{-1/\alpha}$，此处 $\beta=0.9$ 对应指数 $-0.9$，且Top K的热度阈值确实由第K个分位数定义，作为条件期望积分的下界在数学上自洽。
