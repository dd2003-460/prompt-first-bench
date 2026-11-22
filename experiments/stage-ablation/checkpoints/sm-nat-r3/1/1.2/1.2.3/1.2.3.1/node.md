# N121: 离散化误差对命中率计算的影响量化：由于 λ_i 的相对误差 ε_λ ≈ 2.2e-4，且字节命中率 H_byte = Σ p_i s_i / Σ_all p_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

离散化误差对命中率计算的影响量化：由于 λ_i 的相对误差 ε_λ ≈ 2.2e-4，且字节命中率 H_byte = Σ p_i s_i / Σ_all p_i s_i，在大小分布独立于热度的假设下，H_byte 的绝对误差 δH < ε_λ * (1 - H_byte)，若 H_byte ≈ 0.99，则 δH < 2.2e-6，证实连续近似在 0.01% 精度要求下可忽略。

## Corrected Claim

离散化误差对命中率计算的影响量化：由于 λ_i 的相对误差 ε_λ ≈ 2.2e-4，且字节命中率 H_byte = Σ p_i s_i / Σ_all p_i s_i，在大小分布独立于热度的假设下，H_byte 的绝对误差 δH < ε_λ * (1 - H_byte)，若 H_byte ≈ 0.99，则 δH < 2.2e-6，证实连续近似在 0.01% 精度要求下可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：误差传播公式 δH ≈ ε_λ * (1-H) 在大小分布独立假设下成立，数值量级 2.2e-4 * 0.01 = 2.2e-6 计算正确，符合 0.01% (1e-4) 精度要求。
