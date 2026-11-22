# N163: 随机源 ε_mkt,t 的时变特性：虽然 N59 定义了 ε_mkt 为高斯分布，但在短期（t=1,2,3）内，该随机源受季节性（如节假日）和宏观事件影响，其方

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

随机源 ε_mkt,t 的时变特性：虽然 N59 定义了 ε_mkt 为高斯分布，但在短期（t=1,2,3）内，该随机源受季节性（如节假日）和宏观事件影响，其方差 σ_mkt,t^2 并非恒定。需引入季节调整因子 S_t，使得 σ_mkt,t = S_t * σ_mkt_base，其中 S_t 在促销季可能升至 1.5 倍，导致短期 GMV 冲击的置信区间在特定月份需加宽 50%。

## Corrected Claim

随机源 ε_mkt,t 的时变特性：虽然 N59 定义了 ε_mkt 为高斯分布，但在短期（t=1,2,3）内，该随机源受季节性（如节假日）和宏观事件影响，其方差 σ_mkt,t^2 并非恒定。需引入季节调整因子 S_t，使得 σ_mkt,t = S_t * σ_mkt_base，其中 S_t 在促销季可能显著高于基准值，导致短期 GMV 冲击的置信区间在特定月份需相应加宽。

## Evidence

[质询]该陈述包含具体的经验性参数（如促销季因子升至1.5倍、置信区间加宽50%），这些数值并非从第一性原理或数学公理严格推导出的必然结果，而是基于特定市场环境的经验估计，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值参数无法从第一性原理推出）

## Search Query

marketplace GMV seasonality variance adjustment factor
