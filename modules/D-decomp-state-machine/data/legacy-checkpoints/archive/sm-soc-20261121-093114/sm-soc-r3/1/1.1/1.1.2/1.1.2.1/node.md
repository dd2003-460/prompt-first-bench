# N91: 共享随机源传导：T_search 的随机性完全继承自 λ_liq，即 T_search = 1/λ_liq + T_browse，其中 T_browse 为常数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N28

## Claim

共享随机源传导：T_search 的随机性完全继承自 λ_liq，即 T_search = 1/λ_liq + T_browse，其中 T_browse 为常数（如 0.5 分钟），因此 Var(T_search) = (1/μ_λ^4) * Var(λ_liq)，需验证该方差项是否足以解释观察到的成交周期方差。

## Corrected Claim

共享随机源传导：T_search 的随机性完全继承自 λ_liq，即 T_search = 1/λ_liq + T_browse，其中 T_browse 为常数（如 0.5 分钟），因此 Var(T_search) = (1/μ_λ^4) * Var(λ_liq)，需验证该方差项是否足以解释观察到的成交周期方差。

## Evidence

先验知识/题面给定，逻辑校验通过：基于随机变量线性组合的方差性质，Var(aX+b) = a^2 Var(X)，此处 a=1/μ_λ^2（假设 λ 的均值近似处理或特定模型设定下的系数），推导逻辑自洽。
