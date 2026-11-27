# N175: 价格收敛率 γ_transparency 的时间依赖性：该参数并非静态常数，而是随干预时间 t 呈指数衰减 γ(t) = γ_inf * (1 - e^(-k*

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

价格收敛率 γ_transparency 的时间依赖性：该参数并非静态常数，而是随干预时间 t 呈指数衰减 γ(t) = γ_inf * (1 - e^(-k*t))，其中 k 为市场适应速度，k=0.5 表示 3 个月内达到 78% 的收敛效果。

## Corrected Claim

价格收敛率 γ_transparency 的时间依赖性：该参数并非静态常数，而是随干预时间 t 呈指数衰减 γ(t) = γ_inf * (1 - e^(-k*t))，其中 k 为市场适应速度，k=0.5 表示 3 个月内达到 78% 的收敛效果。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 γ(t) = γ_inf * (1 - e^(-k*t)) 在 k=0.5, t=3 时，1 - e^(-1.5) ≈ 0.7769，与陈述中的 78% 一致，数学推导自洽。
