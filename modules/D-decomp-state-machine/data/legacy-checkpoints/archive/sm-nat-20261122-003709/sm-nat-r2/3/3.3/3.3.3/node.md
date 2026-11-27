# N57: 线性折扣效应的近似条件：D_eff ≈ 1 - λ_update * T_resident 仅在 λ_update * T_resident << 1 时成立。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

线性折扣效应的近似条件：D_eff ≈ 1 - λ_update * T_resident 仅在 λ_update * T_resident << 1 时成立。若 T_resident 较大（如 > 100 天），需使用精确指数公式 1 - exp(-λ*T)，线性近似误差超过 5%。

## Corrected Claim

线性折扣效应的近似条件：D_eff ≈ 1 - λ_update * T_resident 仅在 λ_update * T_resident << 1 时成立。若 T_resident 较大（如 > 100 天），需使用精确指数公式 1 - exp(-λ*T)，线性近似误差超过 5%。

## Evidence

先验知识/题面给定，逻辑校验通过：指数函数 $1-e^{-x}$ 在 $x \ll 1$ 时泰勒展开为 $x - x^2/2 + \dots$，线性近似误差主要项为 $x^2/2$。当 $x = \lambda T > 0.1$ 时，相对误差约为 $5\%$，与陈述中“误差超过 5%”的阈值及“需使用精确公式”的结论在数学上自洽且量级合理。
