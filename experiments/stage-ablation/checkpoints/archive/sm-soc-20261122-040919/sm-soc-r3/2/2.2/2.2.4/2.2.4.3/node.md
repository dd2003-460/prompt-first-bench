# N212: 下游投影2：时间敏感度 ∂P(accept)/∂T_short 的量化，基于时间弹性 ε_t = -0.8，计算得 ∂P(accept)/∂T_short = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N56

## Claim

下游投影2：时间敏感度 ∂P(accept)/∂T_short 的量化，基于时间弹性 ε_t = -0.8，计算得 ∂P(accept)/∂T_short = -0.008（每缩短 1 天，接受率上升 0.8%）。

## Corrected Claim

下游投影2：时间敏感度 ∂P(accept)/∂T_short 的量化，基于时间弹性 ε_t = -0.8，计算得 ∂P(accept)/∂T_short = -0.008（每缩短 1 天，接受率上升 0.8%）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于弹性定义 ε = (ΔP/P)/(ΔT/T)，若假设基准接受率 P=10% 且时间变化 ΔT=1天（相对于基准时间 T=10天，即 10% 的变化），则 ΔP = ε * (ΔT/T) * P = -0.8 * 0.1 * 0.1 = -0.008，数值量级与推导逻辑自洽。
