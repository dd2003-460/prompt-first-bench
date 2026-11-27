# N91: 独立假设下的尾部指数基准：若 S 与 F 独立，乘积 W=S*F 的尾部指数 γ_ind 近似为 min(α, β) = 0.9，此时 W 的期望 E[W] 在

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

独立假设下的尾部指数基准：若 S 与 F 独立，乘积 W=S*F 的尾部指数 γ_ind 近似为 min(α, β) = 0.9，此时 W 的期望 E[W] 在 N→∞ 时发散，导致字节命中率公式的分母不稳定。

## Corrected Claim

独立假设下的尾部指数基准：若 S 与 F 独立，乘积 W=S*F 的尾部指数 γ_ind 近似为 min(α, β) = 0.9，此时 W 的期望 E[W] 在 N→∞ 时发散，导致字节命中率公式的分母不稳定。

## Evidence

先验知识/题面给定，逻辑校验通过：独立随机变量乘积的尾部指数确为各分量尾部指数的最小值（min(α, β)），且当尾部指数 γ < 1 时，期望值发散，符合重尾分布的基本数学性质。
