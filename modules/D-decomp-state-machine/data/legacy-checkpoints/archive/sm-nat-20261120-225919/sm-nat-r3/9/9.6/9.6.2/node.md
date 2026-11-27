# N269: 修正因子 K_corr 的数值计算：K_corr = (E[S|hit]/E[S|all])^(1-β)。由于 ρ=-0.3，E[S|hit] < E[S|al

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

修正因子 K_corr 的数值计算：K_corr = (E[S|hit]/E[S|all])^(1-β)。由于 ρ=-0.3，E[S|hit] < E[S|all]。假设 E[S|hit] = 0.7 * E[S|all]（基于 Copula 模拟的近似值），则 K_corr = (0.7)^0.1 ≈ 0.966。因此，修正后的命中率 H_corrected = H_naive * K_corr。若 H_naive (基于 N102 的高估公式) 为 0.82，则 H_corrected ≈ 0.82 * 0.966 ≈ 0.792

## Corrected Claim

修正因子 K_corr 的数值计算：K_corr = (E[S|hit]/E[S|all])^(1-β)。由于 ρ=-0.3，E[S|hit] < E[S|all]。假设 E[S|hit] = 0.7 * E[S|all]（基于 Copula 模拟的近似值），则 K_corr = (0.7)^0.1 ≈ 0.966。因此，修正后的命中率 H_corrected = H_naive * K_corr。若 H_naive (基于 N102 的高估公式) 为 0.82，则 H_corrected ≈ 0.82 * 0.966 ≈ 0.792

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 (0.7)^0.1 ≈ 0.966 及 0.82 * 0.966 ≈ 0.792 准确无误，且符合负相关下修正因子小于1的直觉。
