# N814: 在高频轮询场景（每 100ms 一次 GET）下，若 T_read_staleness > 100ms，则有效可用性降级系数 η_avail = 1 - (T_

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N303

## Claim

在高频轮询场景（每 100ms 一次 GET）下，若 T_read_staleness > 100ms，则有效可用性降级系数 η_avail = 1 - (T_staleness / Polling_Interval)^2；若 T_staleness=1.5s, Interval=100ms, η_avail = 1 - 225 = 负值（即完全失效），需调整轮询间隔至 > T_staleness 才能维持 η_avail > 0.5

## Corrected Claim

在高频轮询场景下，若 T_read_staleness > Polling_Interval，数据新鲜度不足可能导致可用性下降，但具体降级系数需基于实际业务需求和系统架构定义，不能简单套用 η_avail = 1 - (T_staleness / Polling_Interval)^2 公式。

## Evidence

[质询]公式 η_avail = 1 - (T_staleness / Polling_Interval)^2 缺乏任何公认的理论或工程标准支持，属于臆造公式；且根据该公式计算，当 T_staleness=1.5s, Interval=100ms 时，比值为 15，平方后为 225，η_avail = 1 - 225 = -224，而非陈述中声称的“负值（即完全失效）”这种模糊描述掩盖了数值的具体性，更严重的是，该公式本身在逻辑上不合理：可用性系数通常不应由这种简单的平方差定义，且当比值大于1时直接得出负值并解释为“完全失效”缺乏物理/经济直觉支撑。此外，调整轮询间隔至 > T_staleness 并不能保证 η_avail > 0.5，因为即使 Interval > T_staleness，比值小于1，但平方后仍可能接近1，导致 η_avail 接近0，例如 Interval=2s, T_staleness=1.5s，比值为0.75，平方为0.5625，η_avail=0.4375 < 0.5。 | 公式无来源支持且逻辑推导显示调整轮询间隔至 > T_staleness 不能保证 η_avail > 0.5，存在硬逻辑错误。
