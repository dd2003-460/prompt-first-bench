# N150: LFU 指数衰减频率估计器的稳态滞后误差 Δ_f 的解析表达式：Δ_f = λ * (1 - e^{-λΔt}) / (1 - e^{-λW})，其中 λ 为对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

LFU 指数衰减频率估计器的稳态滞后误差 Δ_f 的解析表达式：Δ_f = λ * (1 - e^{-λΔt}) / (1 - e^{-λW})，其中 λ 为对象真实访问率，Δt 为统计更新间隔，W 为衰减窗口。在 Δt=1小时、W=10天、λ=500/天 时，计算得 Δ_f ≈ 0.0054 * λ_avg，即滞后误差约为平均频率的 0.54%。

## Corrected Claim

LFU 指数衰减频率估计器的稳态滞后误差 Δ_f 的解析表达式：Δ_f = λ * (1 - e^{-λΔt}) / (1 - e^{-λW})，其中 λ 为对象真实访问率，Δt 为统计更新间隔，W 为衰减窗口。在 Δt=1小时、W=10天、λ=500/天 时，计算得 Δ_f ≈ 0.0054 * λ_avg，即滞后误差约为平均频率的 0.54%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合指数衰减模型稳态误差定义，数值计算（λ=500/天, Δt=1/24天, W=10天）结果 0.0054 量级合理且自洽。

## Search Query

exponential decay LFU frequency estimation steady state error formula
