# N310: 信号标准差 σ_signal 的量化计算：σ_signal = √(Var(P_observed) - Var(ε_noise))，其中 P_observed 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

信号标准差 σ_signal 的量化计算：σ_signal = √(Var(P_observed) - Var(ε_noise))，其中 P_observed 为观测到的卖家挂价序列，ε_noise 为剥离季节性、节假日和宏观趋势后的残差项，需基于至少 90 天的时间序列数据通过 ARIMA 模型分解确定。

## Corrected Claim

信号标准差 σ_signal 的量化计算：σ_signal = √(Var(P_observed) - Var(ε_noise))，其中 P_observed 为观测到的卖家挂价序列，ε_noise 为剥离季节性、节假日和宏观趋势后的残差项，需基于至少 90 天的时间序列数据通过 ARIMA 模型分解确定。

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式符合统计学原理，ARIMA分解及90天数据要求符合时间序列分析常规实践。

## Search Query

time series decomposition price variance signal noise separation ARIMA
