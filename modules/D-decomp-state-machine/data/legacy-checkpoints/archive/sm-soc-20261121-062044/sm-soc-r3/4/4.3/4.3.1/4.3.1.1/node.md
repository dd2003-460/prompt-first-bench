# N204: 信号方差计算：Var(Signal) 定义为近期成交量加权平均价 P_avg 的时间序列方差，即 Var(P_avg) = (1/N) * Σ(P_avg_t 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

信号方差计算：Var(Signal) 定义为近期成交量加权平均价 P_avg 的时间序列方差，即 Var(P_avg) = (1/N) * Σ(P_avg_t - P_avg_mean)²，其中 P_avg_t 为第 t 期同类商品成交量加权均价，N 为观测期数，该指标反映市场基础价值的系统性波动幅度。

## Corrected Claim

信号方差计算：Var(Signal) 定义为近期成交量加权平均价 P_avg 的时间序列方差，即 Var(P_avg) = (1/N) * Σ(P_avg_t - P_avg_mean)²，其中 P_avg_t 为第 t 期同类商品成交量加权均价，N 为观测期数，该指标反映市场基础价值的系统性波动幅度。

## Evidence

先验知识/题面给定，逻辑校验通过
