# N239: 下游投影1：信号质量阈值判定条件。定义信号质量指数 Q = 1 - (Var(Noise_display) / Var(S_total))。当 n < 30 时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

下游投影1：信号质量阈值判定条件。定义信号质量指数 Q = 1 - (Var(Noise_display) / Var(S_total))。当 n < 30 时，Q < 0.9（假设 Var(S_old)=100, σ_p=100），信号质量下降；当 n > 100 时，Q > 0.98，信号质量显著提升。该阈值直接决定平台是否应向买家展示价格区间。

## Corrected Claim

下游投影1：信号质量阈值判定条件。定义信号质量指数 Q = 1 - (Var(Noise_display) / Var(S_total))。当 n < 30 时，Q < 0.9（假设 Var(S_old)=100, σ_p=100），信号质量下降；当 n > 100 时，Q > 0.98，信号质量显著提升。该阈值直接决定平台是否应向买家展示价格区间。

## Evidence

先验知识/题面给定，逻辑校验通过
