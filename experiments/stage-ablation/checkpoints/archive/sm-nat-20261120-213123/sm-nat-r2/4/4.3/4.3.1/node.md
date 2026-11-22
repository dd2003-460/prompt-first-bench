# N56: LFU 冷启动滞后时间 T_lag 的量化边界：在 Pareto(β=0.9) 热度分布下，识别新热门对象所需的请求窗口 T_lag 约为 10^4 次请求，对

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

LFU 冷启动滞后时间 T_lag 的量化边界：在 Pareto(β=0.9) 热度分布下，识别新热门对象所需的请求窗口 T_lag 约为 10^4 次请求，对应时间跨度 T_lag_time = T_lag / (R/N) ≈ 20 秒（假设均匀分布请求），此期间 LFU 命中率损失 Δ_loss ≈ 5%。

## Corrected Claim

在 Pareto(β=0.9) 热度分布下，LFU 存在冷启动滞后现象。识别新热门对象所需的请求窗口 T_lag 及对应的命中率损失 Δ_loss 取决于系统规模 N、请求率 R 及缓存策略参数，通常需通过具体仿真或实验确定，而非固定为 10^4 次请求或 5% 损失。

## Evidence

[质询]该陈述包含具体的经验性数值（T_lag ≈ 10^4, Δ_loss ≈ 5%），这些数值高度依赖于具体的系统参数（如总对象数 N、总请求率 R、缓存大小、访问模式细节等），而陈述中仅给出了部分假设（Pareto β=0.9, 均匀分布请求），未提供推导这些具体数值所需的完整边界条件或实验数据支持。在缺乏具体 N 和 R 数值的情况下，直接断言 T_lag_time ≈ 20 秒和 Δ_loss ≈ 5% 缺乏严谨的推导基础，属于未经证实的经验估计。 | source=knowledge，逻辑上量纲自洽（时间=次数/速率），但具体数值（10^4, 20s, 5%）为经验事实，缺乏题面给定或第一性原理严格推导支持，且无外部来源验证，故降级。

## Search Query

LFU cold start lag time Pareto distribution request window
