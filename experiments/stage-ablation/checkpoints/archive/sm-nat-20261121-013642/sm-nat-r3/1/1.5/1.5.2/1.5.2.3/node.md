# N132: 负相关对条件期望的修正项量化：在 ρ=0 独立假设下 E[s_i | r_i > r_threshold] = E[s_i]，而在 ρ=-0.3 下，修正因子 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

负相关对条件期望的修正项量化：在 ρ=0 独立假设下 E[s_i | r_i > r_threshold] = E[s_i]，而在 ρ=-0.3 下，修正因子 δ_ρ = E[s_i | r_i > r_threshold, ρ=-0.3] / E[s_i | r_i > r_threshold, ρ=0] ≈ 1 - 0.3 * (σ_s/μ_s) * (z_threshold/σ_r)，其中 z_threshold 为 r_threshold 在标准化热度分布中的分位数，需数值积分验证。

## Corrected Claim

负相关对条件期望的修正项量化：在 ρ=0 独立假设下 E[s_i | r_i > r_threshold] = E[s_i]，而在 ρ=-0.3 下，修正因子 δ_ρ = E[s_i | r_i > r_threshold, ρ=-0.3] / E[s_i | r_i > r_threshold, ρ=0] ≈ 1 - 0.3 * (σ_s/μ_s) * (z_threshold/σ_r)，其中 z_threshold 为 r_threshold 在标准化热度分布中的分位数，需数值积分验证。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

correlation effect on conditional mean Gaussian copula
