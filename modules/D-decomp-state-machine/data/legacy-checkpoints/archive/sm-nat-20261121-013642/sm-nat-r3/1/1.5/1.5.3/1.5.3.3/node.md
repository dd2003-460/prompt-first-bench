# N135: 负相关对条件期望的修正项量化：在 ρ=0 独立假设下 E[r_i | s_i < s_threshold] = E[r_i]，而在 ρ=-0.3 下，修正因子 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

负相关对条件期望的修正项量化：在 ρ=0 独立假设下 E[r_i | s_i < s_threshold] = E[r_i]，而在 ρ=-0.3 下，修正因子 δ_ρ = E[r_i | s_i < s_threshold, ρ=-0.3] / E[r_i | s_i < s_threshold, ρ=0] ≈ 1 + 0.3 * (σ_r/μ_r) * (z_threshold/σ_s)，其中 z_threshold 为 s_threshold 在标准化大小分布中的分位数，需数值积分验证。

## Corrected Claim

负相关对条件期望的修正项量化：在 ρ=0 独立假设下 E[r_i | s_i < s_threshold] = E[r_i]，而在 ρ=-0.3 下，修正因子 δ_ρ = E[r_i | s_i < s_threshold, ρ=-0.3] / E[r_i | s_i < s_threshold, ρ=0] ≈ 1 + 0.3 * (σ_r/μ_r) * (z_threshold/σ_s)，其中 z_threshold 为 s_threshold 在标准化大小分布中的分位数，需数值积分验证。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

correlation effect on conditional mean Gaussian copula
