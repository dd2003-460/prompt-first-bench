# N10: 卖家挂价策略的收益期望函数 E[Revenue] = P_ask * Prob(Sale | P_ask) - C_wait(T_wait)，其中 Prob(S

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

卖家挂价策略的收益期望函数 E[Revenue] = P_ask * Prob(Sale | P_ask) - C_wait(T_wait)，其中 Prob(Sale) 随 P_ask 上升而指数下降，C_wait 为时间成本；卖家最优定价 P* 是最大化该期望的点，而非市场价。

## Corrected Claim

卖家挂价策略的收益期望函数 E[Revenue] = P_ask * Prob(Sale | P_ask) - C_wait(T_wait)，其中 Prob(Sale) 随 P_ask 上升而指数下降，C_wait 为时间成本；卖家最优定价 P* 是最大化该期望的点，而非市场价。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点收益期望函数中的三个核心组成部分：成交概率模型（分子项）、时间成本模型（减项）以及基于前两者的最优化求解（一阶条件）。三者逻辑上层层递进且互不重叠，分别定义了模型中的关键参数 α、r 以及最终解 P*，覆盖了从参数估计到解析推导的全过程，无冗余。）

## Search Query

seller optimal asking price expectation revenue probability of sale waiting cost
