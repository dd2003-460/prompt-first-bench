# N54: 命中对象平均大小 E[S_hit] 的计算：基于 Pareto(α=1.1) 大小分布与 Pareto(β=0.9) 热度分布，在负相关 ρ=-0.3 条件下，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N20

## Claim

命中对象平均大小 E[S_hit] 的计算：基于 Pareto(α=1.1) 大小分布与 Pareto(β=0.9) 热度分布，在负相关 ρ=-0.3 条件下，E[S_hit] = ∫ s * f_pop(s) * f_size(s|hit) ds / ∫ f_pop(s) * f_size(s|hit) ds；由于热门对象较小，f_size(s|hit) 偏向小值，需通过 Copula 模型（如 Gaussian Copula 或 Clayton Copula）关联两个 Pareto 分布以获取联合密度，进而数值积分求解。

## Corrected Claim

命中对象平均大小 E[S_hit] 的计算需基于 Pareto 大小分布与热度分布，在负相关条件下，通常需通过 Copula 模型（如 Gaussian 或 Clayton Copula）构建联合密度，进而通过数值积分求解条件期望；具体数值依赖于所选 Copula 类型及参数拟合。

## Evidence

[质询]该陈述属于具体的数值模拟/统计建模结果（经验事实），参考来源均未提供相关数据或模型支持，且无法仅凭第一性原理推导出具体的积分结果或验证 Copula 模型的具体参数选择是否唯一正确。 | 逻辑上，使用 Copula 关联两个 Pareto 分布并数值积分求解条件期望是处理非独立变量联合分布的标准且自洽的方法；但参考来源 [1][2][3] 分别讨论帕累托最优概念、回归评价指标和游戏命中率，均与该事实主题（缓存/对象大小分布建模）无关，无可用外部证据支持具体数值或模型细节。

## Search Query

joint distribution of object size and popularity in CDN cache Pareto correlation integral mean size hit

## Retrieval Sources

- {'url': 'https://blog.csdn.net/Harrytutu_ZuiYue/article/details/163818543&rut=1abad3120f97dfc36acbe453586e7c43a8337b5abacd70fbe876c209c61d0d23', 'type': 'ddg', 'title': '【超详细】帕累托 Pareto 最优是什么？一文大白话吃透概念、经济学到多目标优化附实战案例-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_40651515/article/details/105930868&rut=8c601dd6ecd9e9dc5e0955a609801689ebd34deadb5d0eec673e09db246ed98e', 'type': 'ddg', 'title': '回归评价指标：Mse、Rmse、Mae、Mape、R2公式理解及代码实现-csdn博客'}
- {'url': 'https://bbs.nga.cn/read.php?tid=39243747&page=e&rut=0b784dca33a458e2f0b1b2ab05870e22abb24e1ce03e2c36788bf7c23ffd7927', 'type': 'ddg', 'title': '[攻略] 数据贴，揭秘命中率的计算方式v1.9—更新了科研命中的计算方式和喷火器的命中率系数 NGA玩家社区'}
