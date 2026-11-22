# N157: 模仿系数 α 的OLS回归估计公式：α = Cov(P_t, P_neighbor) / Var(P_neighbor)，其中 P_t 为卖家 t 的挂价，P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N46, N47, N48

## Claim

模仿系数 α 的OLS回归估计公式：α = Cov(P_t, P_neighbor) / Var(P_neighbor)，其中 P_t 为卖家 t 的挂价，P_neighbor 为同类商品近期成交中位数，基于横截面数据计算，该系数直接反映卖家定价对基准价的敏感度。

## Corrected Claim

模仿系数 α 的OLS回归估计公式：α = Cov(P_t, P_neighbor) / Var(P_neighbor)，其中 P_t 为卖家 t 的挂价，P_neighbor 为同类商品近期成交中位数，基于横截面数据计算，该系数直接反映卖家定价对基准价的敏感度。

## Evidence

先验知识/题面给定，逻辑校验通过：在横截面回归模型 P_t = α * P_neighbor + ε 中，若截距项为0或已中心化，OLS斜率估计量确实等于 Cov(P_t, P_neighbor) / Var(P_neighbor)，该公式在计量经济学中定义明确，逻辑自洽。
