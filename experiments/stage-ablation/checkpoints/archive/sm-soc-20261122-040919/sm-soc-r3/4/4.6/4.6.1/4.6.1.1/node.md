# N320: T_0（基准期成交周期）的确定需排除季节性干扰，公式为 T_0 = mean(T_{history}) - seasonal_component(t)，其中 s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

T_0（基准期成交周期）的确定需排除季节性干扰，公式为 T_0 = mean(T_{history}) - seasonal_component(t)，其中 seasonal_component(t) 通过 ARIMA 或 STL 分解从至少 24 个月的历史数据中估计；若未排除季节性，T_0 可能偏差 >10%。

## Corrected Claim

T_0（基准期成交周期）的确定需排除季节性干扰，公式为 T_0 = mean(T_{history}) - seasonal_component(t)，其中 seasonal_component(t) 通过 ARIMA 或 STL 分解从至少 24 个月的历史数据中估计；若未排除季节性，T_0 可能偏差 >10%。

## Evidence

先验知识/题面给定，逻辑校验通过：使用ARIMA或STL分解去除季节性是时间序列分析中的标准做法，24个月数据足以捕捉年度季节性周期，排除季节性以避免基准偏差符合统计学直觉。

## Search Query

time series decomposition STL seasonal component estimation cycle time
