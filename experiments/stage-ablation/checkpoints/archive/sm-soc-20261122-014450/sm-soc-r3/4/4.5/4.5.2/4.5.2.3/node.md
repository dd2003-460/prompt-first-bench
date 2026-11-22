# N257: 干预即时效果覆盖率 P_fast 定义为 τ < 48小时（2天）的概率，公式为 P_fast = 1 - exp(-2λ_τ)；在 λ_τ = 0.2 时，P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

干预即时效果覆盖率 P_fast 定义为 τ < 48小时（2天）的概率，公式为 P_fast = 1 - exp(-2λ_τ)；在 λ_τ = 0.2 时，P_fast ≈ 33%，意味着仅三分之一卖家能在激励窗口内完成调整。

## Corrected Claim

干预即时效果覆盖率 P_fast 定义为 τ < 48小时（2天）的概率，公式为 P_fast = 1 - exp(-2λ_τ)；在 λ_τ = 0.2 时，P_fast ≈ 33%，意味着仅三分之一卖家能在激励窗口内完成调整。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_fast = 1 - exp(-2λ_τ) 在 λ_τ = 0.2 时计算结果为 1 - exp(-0.4) ≈ 0.3297，即约 33%，数值与逻辑自洽。
