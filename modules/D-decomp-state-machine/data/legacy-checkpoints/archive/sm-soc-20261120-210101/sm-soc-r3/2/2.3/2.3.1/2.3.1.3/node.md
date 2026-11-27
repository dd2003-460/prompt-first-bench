# N186: 共享随机源 (ε_algo, τ_lag) 的下游投影：对买家感知价格 P_perceived 的影响。P_perceived = P_list + ε_pri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N51

## Claim

共享随机源 (ε_algo, τ_lag) 的下游投影：对买家感知价格 P_perceived 的影响。P_perceived = P_list + ε_price_algo，其中 ε_price_algo = σ_algo * P_ref * N(0,1)。若 σ_algo=0.1，买家感知价格的 95% 置信区间为 P_list ± 0.196 * P_ref。这解释了为何部分买家即使看到低价，仍因感知噪声而犹豫。

## Corrected Claim

共享随机源 (ε_algo, τ_lag) 的下游投影：对买家感知价格 P_perceived 的影响。P_perceived = P_list + ε_price_algo，其中 ε_price_algo = σ_algo * P_ref * N(0,1)。若 σ_algo=0.1，买家感知价格的 95% 置信区间为 P_list ± 0.196 * P_ref。这解释了为何部分买家即使看到低价，仍因感知噪声而犹豫。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布95%置信区间系数为1.96，σ=0.1时区间为±0.196*P_ref，数学推导正确

## Search Query

perceived price noise buyer decision making algorithm error
