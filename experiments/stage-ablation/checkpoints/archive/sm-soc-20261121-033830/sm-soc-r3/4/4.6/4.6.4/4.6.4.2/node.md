# N276: 长期价格稳定机制：T=365天内价格波动率 σ_P = std(P_t) / mean(P_t)，其中 P_t 为第 t 天的市场均价；需通过动态博弈模型模拟卖

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

长期价格稳定机制：T=365天内价格波动率 σ_P = std(P_t) / mean(P_t)，其中 P_t 为第 t 天的市场均价；需通过动态博弈模型模拟卖家定价策略的收敛过程，计算价格波动率是否随时间下降至稳态值 σ_P*。

## Corrected Claim

长期价格稳定机制：T=365天内价格波动率 σ_P = std(P_t) / mean(P_t)，其中 P_t 为第 t 天的市场均价；需通过动态博弈模型模拟卖家定价策略的收敛过程，计算价格波动率是否随时间下降至稳态值 σ_P*。

## Evidence

先验知识/题面给定，逻辑校验通过：价格波动率定义符合统计学标准（标准差/均值），动态博弈收敛分析是研究市场定价机制的合理方法论，量纲与逻辑自洽。

## Search Query

long-term price stability dynamic game model
