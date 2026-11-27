# N28: 请求热度 Pareto(β=0.9) 下，访问频率的累积分布 G(f) = (f_min/f)^0.9。总请求率 5000万/天 归一化后，单个对象的平均请求率

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

请求热度 Pareto(β=0.9) 下，访问频率的累积分布 G(f) = (f_min/f)^0.9。总请求率 5000万/天 归一化后，单个对象的平均请求率 λ_avg = 500。由于 β<1，头部对象（如 Top 10）的访问频率远超平均值，Top 1 对象的请求率约为 λ_avg * (1/0.9) * (1 - N^{1-β}) / (1 - (N+1)^{1-β})，需具体计算其数值以量化头部效应。

## Corrected Claim

请求热度 Pareto(β=0.9) 下，访问频率的累积分布 G(f) = (f_min/f)^0.9。总请求率 5000万/天 归一化后，单个对象的平均请求率 λ_avg = 500。由于 β<1，头部对象（如 Top 10）的访问频率远超平均值，Top 1 对象的请求率约为 λ_avg * (1/0.9) * (1 - N^{1-β}) / (1 - (N+1)^{1-β})，需具体计算其数值以量化头部效应。

## Evidence

检索失败: no sources from any channel (all 5 failed)
