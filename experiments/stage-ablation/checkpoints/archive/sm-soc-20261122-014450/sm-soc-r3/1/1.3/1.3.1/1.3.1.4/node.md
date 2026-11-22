# N154: 重复博弈中 k 的动态调整方程：k_{t+1} = k_t + α_learning * (B_filter_t - C_signal_t * k_t)，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

重复博弈中 k 的动态调整方程：k_{t+1} = k_t + α_learning * (B_filter_t - C_signal_t * k_t)，其中 α_learning 为卖家学习率（通常 0.1-0.2）；需模拟 50 轮迭代后 k 是否收敛至 k* 以及收敛速度（半衰期 T_half = ln(2)/α_learning）。

## Corrected Claim

重复博弈中 k 的动态调整方程：k_{t+1} = k_t + α_learning * (B_filter_t - C_signal_t * k_t)，其中 α_learning 为卖家学习率（通常 0.1-0.2）；需模拟 50 轮迭代后 k 是否收敛至 k* 以及收敛速度（半衰期 T_half = ln(2)/α_learning）。

## Evidence

先验知识/题面给定，逻辑校验通过：该方程为标准的线性误差修正模型（EMA变体），其收敛性、稳态解 k* = B/(C*α) 及半衰期公式 T_half = ln(2)/α 均符合线性离散动力系统的基本数学性质，量纲与逻辑自洽。

## Search Query

dynamic signaling equilibrium convergence rate in repeated games
