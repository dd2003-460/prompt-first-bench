# N175: 似然函数 P(T|V) 的生成过程：假设成交时间 T 服从指数分布 Exp(λ(V))，其中成交率 λ(V) = β * exp(-γ * (V - P_ask

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

似然函数 P(T|V) 的生成过程：假设成交时间 T 服从指数分布 Exp(λ(V))，其中成交率 λ(V) = β * exp(-γ * (V - P_ask))，β为基准成交率，γ为价格敏感度系数，需通过历史数据回归估计 β 和 γ 的具体数值。

## Corrected Claim

似然函数 P(T|V) 的生成过程：假设成交时间 T 服从指数分布 Exp(λ(V))，其中成交率 λ(V) = β * exp(-γ * (V - P_ask))，β为基准成交率，γ为价格敏感度系数，需通过历史数据回归估计 β 和 γ 的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

exponential distribution time to sale price sensitivity coefficient estimation
