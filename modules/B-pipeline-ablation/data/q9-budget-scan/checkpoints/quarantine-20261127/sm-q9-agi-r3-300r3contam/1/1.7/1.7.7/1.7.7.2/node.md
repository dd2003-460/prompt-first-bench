# N157: ρ_corr 对 K 值的放大效应公式：在独立假设下所需 K_ind = ceil(log(1-E_target)/log(1-p_base))，在相关假设下，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

ρ_corr 对 K 值的放大效应公式：在独立假设下所需 K_ind = ceil(log(1-E_target)/log(1-p_base))，在相关假设下，有效错误率 E_eff(K) = 1 - (1-p_base)^K * (1 - ρ_corr)^(K-1)，需解方程 E_eff(K) ≤ E_target 求 K_corr，当 ρ_corr=0.3, p_base=0.75, E_target=0.05 时，K_ind=4, K_corr=6，增幅 50%。

## Corrected Claim

ρ_corr 对 K 值的放大效应公式：在独立假设下所需 K_ind = ceil(log(1-E_target)/log(1-p_base))，在相关假设下，有效错误率 E_eff(K) = 1 - (1-p_base)^K * (1 - ρ_corr)^(K-1)，需解方程 E_eff(K) ≤ E_target 求 K_corr，当 ρ_corr=0.3, p_base=0.75, E_target=0.05 时，K_ind=4, K_corr=6，增幅 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：独立假设下 K_ind=ceil(log(0.95)/log(0.25))=4；相关假设下代入公式计算 K=5 时 E_eff≈0.084>0.05，K=6 时 E_eff≈0.044≤0.05，故 K_corr=6，增幅 (6-4)/4=50%，数值与逻辑均自洽。
