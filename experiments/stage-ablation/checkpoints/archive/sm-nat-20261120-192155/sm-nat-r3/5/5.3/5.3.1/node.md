# N113: 工作点1（弱相关修正）：当 ρ = -0.1 时，修正因子 ε_ρ ≈ 1 - (-0.1)*sqrt(Var(log i))。对于 N=100000，Var(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

工作点1（弱相关修正）：当 ρ = -0.1 时，修正因子 ε_ρ ≈ 1 - (-0.1)*sqrt(Var(log i))。对于 N=100000，Var(log i) ≈ (ln(100000))^2/12 ≈ 13.8，sqrt(13.8) ≈ 3.7。ε_ρ ≈ 1 + 0.37 = 1.37。因此 k' ≈ 1.37 * k_independent。若 k_independent=50000，则 k'≈68500，提升37%。

## Corrected Claim

工作点1（弱相关修正）：当 ρ = -0.1 时，修正因子 ε_ρ ≈ 1 - (-0.1)*sqrt(Var(log i))。对于 N=100000，Var(log i) ≈ (ln(100000))^2/12 ≈ 13.8，sqrt(13.8) ≈ 3.7。ε_ρ ≈ 1 + 0.37 = 1.37。因此 k' ≈ 1.37 * k_independent。若 k_independent=50000，则 k'≈68500，提升37%。

## Evidence

先验知识/题面给定，逻辑校验通过：Var(log i)近似计算正确（(ln 10^5)^2/12 ≈ 13.8），sqrt(13.8)≈3.7，修正因子1+0.1*3.7=1.37，数值推导自洽。
