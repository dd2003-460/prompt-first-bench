# N289: Q_avg 的计算窗口与平滑处理：Q_avg 不应为简单7日均值，而应采用指数加权移动平均（EWMA）以捕捉趋势：Q_avg_t = λ * Q_t + (1-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

Q_avg 的计算窗口与平滑处理：Q_avg 不应为简单7日均值，而应采用指数加权移动平均（EWMA）以捕捉趋势：Q_avg_t = λ * Q_t + (1-λ) * Q_avg_{t-1}，其中 λ 取 0.2-0.3，以避免单日异常值（如大促）导致的区间剧烈波动。

## Corrected Claim

Q_avg 的计算窗口与平滑处理：Q_avg 不应为简单7日均值，而应采用指数加权移动平均（EWMA）以捕捉趋势：Q_avg_t = λ * Q_t + (1-λ) * Q_avg_{t-1}，其中 λ 取 0.2-0.3，以避免单日异常值（如大促）导致的区间剧烈波动。

## Evidence

先验知识/题面给定，逻辑校验通过：EWMA公式定义正确，λ取值0.2-0.3符合平滑与响应速度的工程惯例，能有效抑制单日异常值波动。

## Search Query

exponential weighted moving average inventory demand forecasting
